import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
#sys.path.insert(0,parentdir)

#Change System Path To Parent Level
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import config

WorkDir=(config.INVDIR)

print(parentdir)
print(config.DBDIR)

print(WorkDir)
