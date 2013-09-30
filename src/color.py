# -*- coding:utf-8 -*-
from __future__ import print_function

# ---- GREEN
GREEN = '\033[32m'
BLUE = '\033[34m'

# ---- END
ENDC = '\033[0m'


def green_print(pstring):
    pstring = GREEN + pstring + ENDC
    print(pstring)


def blue_print(pstring):
    pstring = BLUE + pstring + ENDC
    print(pstring)
