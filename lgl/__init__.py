import sys
import os
import pathlib
import lgl.run
import lgl.init
import lgl.traverse
import lgl.get_unresolve

import importmagic

def project_home():
    cwd = os.getcwd()
    while not os.path.exists(cwd+os.sep+"setup.py"):
        cwd = pathlib.Path(os.getcwd()).resolve().parents[0]
    if os.path.exists(cwd+os.sep+"setup.py"):
        return cwd

def filelist(path):
    if os.sep==path[len(path)-1]:
        return traverse.traverse(path)
    else:
        return [path]

def list_unresolved(path):
    return get_unresolve.list_unresolved(path)

def add_import(paths):
    path_ = sys.path + [os.getcwd()]
    index = importmagic.SymbolIndex()
    index.build_index(paths=path_)
    return get_unresolve.add_import(paths,index)

def install_module(module):
    return get_unresolve.install_module(module)

def run_():
    run.cmd()

def init_(args):
    init.cmd(args)
