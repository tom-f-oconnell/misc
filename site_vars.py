#!/usr/bin/env python3

from __future__ import print_function
import sys
import site


# See also output of `python -m site` (some of below + sys.path)
sys_vars = [
    'sys.prefix',
    'sys.exec_prefix',
    'sys.base_prefix',
    'sys.base_exec_prefix',
    'site.USER_BASE',
    'site.USER_SITE'
]
for v in sys_vars:
    print(v + ': ', end='')
    try:
        print(eval(v))
    except AttributeError:
        # (python2)
        print('undefined for this python version')

