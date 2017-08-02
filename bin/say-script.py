#!/usr/bin/env python

# No Relative Import. Script just imports `dumbpack` however it is in our path.
# In this case, since we installed using `pip install -e .`
# it follows a symlink back to the source dir in my `projects` dir

import dumbpack
import sys

try:
    val = sys.argv[1]
except IndexError:
    val = sys.argv[0]

print dumbpack.sayHello(val)