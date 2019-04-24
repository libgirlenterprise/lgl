import ast
import os

import setuptools


setup__ = ""

def setup(**kwargs):
    global setup__
    setup__ = kwargs

setuptools.setup = setup

def read_setuppy (path):
    setuptools.setup = setup
    content = open(path).read()
    exec(content)
    return setup__

def read_initpy (path):
    with open(path) as f:
        src = f.read()
    ast.dump(ast.parse(src))

def read_package (path):
    initpy=path+"__init__.py"
    if(os.path.isfile(initpy)):
        read_initpy(initpy)
        return [path]
    else:
        return []

def file_traverse(dir):
    result = []
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            if file[0]=='.':
                continue
            if os.path.isdir(dir+file):
                result = result + file_traverse(dir+file+os.sep)
            else:
                if os.path.splitext(file)[1] == '.py':
                    result = result + [dir+file]
        return result
    return [dir]

def traverse (path):
    setuppy = read_setuppy (path+'setup.py')
    packages = setuppy.get('packages')
    files = []
    if(packages):
        for package in packages:
            files = files + file_traverse(path+package+os.sep)
    return files
