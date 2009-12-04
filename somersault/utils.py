_debug = True

def debug(msg):
    if _debug:
        print msg

def error(msg):
    import sys
    print msg
    sys.exit(0)
    
