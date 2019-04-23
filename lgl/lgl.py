import lgl
import argparse
import subprocess
import sys
import os
import logging

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--verbose','-v', action='count')
subparsers = parser.add_subparsers()

# run
def command_run (args):
    lgl.install_module(['.'+os.sep])
    lgl.add_import(['.'+os.sep])
    lgl.run_()
parser_run = subparsers.add_parser('run', help='see `run -h`')
parser_run.add_argument('args', nargs='*')
parser_run.set_defaults(handler=command_run)

# install
def command_install (args):
    lgl.install_module(args.file_names)

parser_install = subparsers.add_parser('install', help='see `install -h`')
parser_install.add_argument('file_names', nargs='*')
parser_install.set_defaults(handler=command_install)

# fmt
def command_fmt (args):
    lgl.add_import(args.file_names)

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
    if args.verbose:
        if args.verbose > 1:
            logging.basicConfig(level=logging.DEBUG)
        elif args.verbose > 0:
            logging.basicConfig(level=logging.INFO)
        logging.info("verbose level:"+str(args.verbose))
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()
