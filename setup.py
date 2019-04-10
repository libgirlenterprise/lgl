from setuptools import setup

setup(name='lgl',
      version='0.1',
      description='launch python.',
      url='https://github.com/libgirlenterprise/lgl',
      author='Team Libgirl',
      author_email='team@libgirl.com',
      license='Apache License 2.0',
      packages=['lgl'],
      zip_safe=False,
      test_suite='tests',
      install_requires= [
        'toml',
        'importmagic'
      ],
      entry_points = {
        'console_scripts': ['lgl=lgl.lgl:main'],
      },
)
