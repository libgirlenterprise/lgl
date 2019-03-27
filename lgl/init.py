import sys
import os

def gen_setuppy(pwd,name):
    with open(pwd+os.path.sep+'setup.py', 'w') as f:
        f.write("""from setuptools import setup

setup(name='"""+name+"""',
      version='0.1',
      description='none',
      license='MIT',
      packages=['"""+name+"""'],
      zip_safe=False,
      entry_points = {
        'console_scripts': ['"""+name+'='+name+'.'+name+""":main'],
      },
    )
""")
    

def gen_entrypoint(pwd,name):
    os.makedirs(pwd+os.path.sep+name)
    with open(pwd+os.path.sep+name+os.path.sep+name+'.py', 'w') as f:
        f.write("""import sys

def main():
    print(sys.argv)
""")

def cmd(args):
    cwd=os.getcwd()
    pwd=cwd+os.path.sep+args.name
    if not(os.path.isdir(pwd)):
        os.makedirs(pwd)
        gen_setuppy(pwd,args.name)
        gen_entrypoint(pwd,args.name)
    else:
        print("already exist "+args.name)
