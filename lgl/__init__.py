import sys
import os
import pathlib
import logging
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

def add_import(files):
    logging.info("add_import:"+str(files))
    path_ = sys.path + [os.getcwd()]
    index = importmagic.SymbolIndex()
    logging.info("add_import: build index")
    index.build_index(paths=path_)
    result=[]
    for file in files:
        filelist_ = filelist(file)
        if(isinstance(filelist_,list)):
            result=result+filelist_
    return get_unresolve.add_import(result,index)

def install_module(basefiles):
    result=[]
    for file in basefiles:
        filelist_ = filelist(file)
        if(isinstance(filelist_,list)):
            for file in filelist_:
                result=result+list_unresolved(file)
    return get_unresolve.install_module(result)

def run_():
    run.cmd()

def init_(args):
    init.cmd(args)
