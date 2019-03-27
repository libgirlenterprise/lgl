import lgl
import argparse
import subprocess
import sys
import os

parser = argparse.ArgumentParser(description=__doc__)
subparsers = parser.add_subparsers()

# run
def command_run (args):
    lgl.run_()
parser_run = subparsers.add_parser('run', help='see `run -h`')
parser_run.add_argument('args', nargs='*')
parser_run.set_defaults(handler=command_run)

# install
def command_install (args):
    result=[]
    for file in args.file_names:
        filelist = lgl.filelist(file)
        if(isinstance(filelist,list)):
            for file in filelist:
                print(result)
                result=result+lgl.list_unresolved(file)
    lgl.install_module(result)

parser_install = subparsers.add_parser('install', help='see `install -h`')
parser_install.add_argument('file_names', nargs='*')
parser_install.set_defaults(handler=command_install)

# fmt
def command_fmt (args):
    result=[]
    for file in args.file_names:
        filelist = lgl.filelist(file)
        if(isinstance(filelist,list)):
            result=result+filelist
    lgl.add_import(result)

parser_fmt = subparsers.add_parser('fmt', help='see `fmt -h`')
parser_fmt.add_argument('file_names', nargs='*')
parser_fmt.set_defaults(handler=command_fmt)

# init
def command_init (args):
    result=[]
    lgl.init_(args)

parser_init = subparsers.add_parser('init', help='see `init -h`')
parser_init.add_argument('name')
parser_init.add_argument('args', nargs='*')
parser_init.set_defaults(handler=command_init)

def ensure_initdir():
    pwd=os.path.expanduser("~")+os.path.sep+".lgl"
    if not(os.path.isdir(pwd)):
        os.makedirs(pwd)
    gitdir=pwd+os.path.sep+"pydic"
    if not(os.path.isdir(gitdir)):
        try:
            subprocess.check_call(["git","clone","https://github.com/libgirlenterprise/pydic",gitdir])
        except:
            print("subprocess.check_call() failed")

def main():
    ensure_initdir()
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()
