from __future__ import print_function

import imp
from . import config

print('** config loaded **')

print(config.FOO)
print(config.BAR)

config = imp.load_source('config', 'altconfig.py')
print('** altconfig loaded **')

print(config.FOO)
print(config.BAR)
