import os
import pkgutil
import sys
import subprocess
import logging

import importmagic
import toml


def list_unresolved (path):
    with open(path) as f:
        python_source = f.read()
    scope = importmagic.Scope.from_source(python_source)
    unresolved, unreferenced = scope.find_unresolved_and_unreferenced_symbols()
    return list(unresolved)

def add_import (paths,index):
    logging.info("add_import :"+str(paths))
    path_ = sys.path + [os.getcwd()]
    for path in paths:
        with open(path) as f:
            python_source = f.read()
        scope = importmagic.Scope.from_source(python_source)
        unresolved, unreferenced = scope.find_unresolved_and_unreferenced_symbols()
        python_source = importmagic.update_imports(python_source, index, unresolved, unreferenced)
        with open(path, 'w') as f:
            f.write(python_source)

def get_proper_module_name(name):
    file=os.path.expanduser("~")+os.path.sep+".lgl"+os.path.sep+"pydic"+os.path.sep+"info.toml"
    with open(file) as f:
        toml_src = f.read()
    parsed_toml = toml.loads(toml_src)
    return parsed_toml['dict'].get(name) or name

def filter_modules(mods):
    logging.info("filter_modules origin:"+str(mods))
    for m in pkgutil.iter_modules():
        if m.name in mods:
            mods.remove(m.name)
    logging.info("filter_modules pkgutil:"+str(mods))
    for m in mods:
        if m in sys.builtin_module_names:
            mods.remove(m)
    logging.info("filter_modules result:"+str(mods))
    return mods

def install_module(modules):
    logging.info("install_module origin:"+str(modules))
    mlist = list(dict.fromkeys([x.split(".")[0] for x in modules]))
    logging.info("install_module mlist:"+str(mlist))
    mlist = filter_modules(mlist)
    mlist = list(get_proper_module_name(x) for x in mlist)
    if mlist:
        subprocess.run(["conda","install","-y"]+mlist)
