import os
import sys
import subprocess
import toml

import importmagic

def list_unresolved (path):
    with open(path) as f:
        python_source = f.read()
    scope = importmagic.Scope.from_source(python_source)
    unresolved, unreferenced = scope.find_unresolved_and_unreferenced_symbols()
    return list(unresolved)

def add_import (paths,index):
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

def install_module(modules):
    mlist = list(dict.fromkeys([get_proper_module_name(x.split(".")[0]) for x in modules]))
    if mlist:
        subprocess.run(["conda","install","-y"]+mlist)
