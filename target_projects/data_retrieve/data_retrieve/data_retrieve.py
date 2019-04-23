
# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
    dataX, dataY = [], []
    for i in range(len(dataset)-look_back-1):
        a = dataset[i:(i+look_back), 0]
        dataX.append(a)
        dataY.append(dataset[i + look_back, 0])
    return numpy.array(dataX), numpy.array(dataY)

def get_trainX_and_testX():
    obj = json.loads(os.environ.get('SM_TRAINING_ENV'))
    obj = obj['channel_input_dirs']['training'] + '/prices.csv'

    prices_dataset = pandas.read_csv(obj, header=0)

    wltw = prices_dataset[prices_dataset['symbol']=='WLTW']

    wltw_stock_prices = wltw.close.values.astype('float32')

    wltw_stock_prices = wltw_stock_prices.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    wltw_stock_prices = scaler.fit_transform(wltw_stock_prices)

    train_size = int(len(wltw_stock_prices) * 0.67)
    test_size = len(wltw_stock_prices) - train_size
    train, test = wltw_stock_prices[0:train_size,:], wltw_stock_prices[train_size:len(wltw_stock_prices),:]

    return train, test


def get_train_data():
    train, test = get_trainX_and_testX()
    look_back = 1

    trainX, trainY = create_dataset(train, look_back)
    testX, testY = create_dataset(test, look_back)
    
    # reshape into X=t and Y=t+1
    trainX = numpy.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
    testX = numpy.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
    
    return {
        'train': {
            'x_train': trainX,
            'y_train': trainY
        },
        'test': {
            'x_test': testX,
            'y_test': testY
        }
        
    }

def get_eval_data():

    return get_train_data()['test']

def main():
    print("hello world")
