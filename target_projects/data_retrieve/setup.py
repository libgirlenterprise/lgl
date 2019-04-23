from setuptools import setup

setup(name='data_retrieve',
      version='0.1',
      description='none',
      license='MIT',
      packages=['data_retrieve'],
      zip_safe=False,
      entry_points = {
        'console_scripts': ['data_retrieve=data_retrieve.data_retrieve:main'],
      },
    )
