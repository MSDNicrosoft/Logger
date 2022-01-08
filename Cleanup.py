from shutil import rmtree as remove
import os

dist = 'dist'
egg = 'msdnicrosoft_logger.egg-info'
if os.path.exists(dist) and os.path.ispath(dist):
    remove(dist)
if os.path.exists(egg) and os.path.ispath(egg):
    remove(egg)
remove('__pycache__')
print('Done!')
