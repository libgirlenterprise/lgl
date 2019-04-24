import importlib
import os
import sys

import lgl.traverse
import lgl

def cmd():
    project_home=lgl.project_home()
    sys.path.append(project_home)
    setuppy = lgl.traverse.read_setuppy(project_home+os.sep+"setup.py")
    entry_points = setuppy.get('entry_points')
    version = setuppy.get('version')
    if(not(entry_points)):
        print("no entry_point in setup.py")
        sys.exit(1)
    console_scripts=entry_points.get('console_scripts')
    del sys.argv[0:2]

    binname= console_scripts[0].split("=")[0]
    modname= console_scripts[0].split("=")[1].split(":")
    sys.argv=[os.getcwd()+os.sep+binname]+sys.argv
    m=importlib.import_module(modname[0])
    f=eval("m."+modname[1])
    sys.exit(f())
#    sys.exit(
#        load_entry_point(modname+'=='+version, 'console_scripts', binname)()
#    )
