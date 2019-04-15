from setuptools import setup
import os

def read_file(filename):
    filepath = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), filename)
    if os.path.exists(filepath):
        return open(filepath).read()
    else:
        return ''

setup(name='lgl',
      version='0.1',
      description='launch python.',
      long_description=read_file('readme.md'),
      long_description_content_type="text/markdown",
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
