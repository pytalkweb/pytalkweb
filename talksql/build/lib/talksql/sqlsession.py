"""  
sqlstore
Simple module to keep toc and chuck objects with indices of toc
Copyright (c) Madhukumar Seshadri
our simple toc
slots is key and offset to map
map is array of offsets to file offsets
osize is size of object at map[map index]
hole - offset to map - holds previous erased objects
Note - we leave the file handle dirty so make sure you seek where it need to be
"""
import os
import re
import cPickle

persister=cPickle

