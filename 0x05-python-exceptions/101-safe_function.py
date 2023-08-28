#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as j:
        import sys
        print("Exception: {}".format(j), file=sys.stderr)
        return None
