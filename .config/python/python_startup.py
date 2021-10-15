#!/usr/bin/env python

# Configuration section

import os
import atexit
import rlcompleter
import readline
import numpy as np
from matplotlib import pyplot as plt

max_size_bytes = 1000000
max_size_lines = 10000


if 'PYTHONHISTFILE' in os.environ:
    hist_file = os.path.expanduser(os.environ['PYTHONHISTFILE'])
elif 'XDG_DATA_HOME' in os.environ:
    hist_file = os.path.join(os.path.expanduser(os.environ['XDG_DATA_HOME']),
                             'python', 'python_history')
else:
    hist_file = os.path.join(os.path.expanduser('~'), '.local', 'share',
                             'python', 'python_history')

hist_file = os.path.abspath(hist_file)
_dir = os.path.dirname(hist_file)
os.makedirs(_dir, exist_ok=True)


# Code section, no need to modify this
def reset_file(size, max_size, reason):
    try:
        print("Resetting history file %s because it exceeded %s %s; it has %s.\n" % (hist_file, max_size, reason, size,))
        f = open(hist_file, 'w')
        f.close()
    except IOError as e:
        print("Couldn't reset history file %s [%s].\n" % (hist_file, e,))


def safe_getsize(hist_file):
    try:
        size = os.path.getsize(hist_file)
    except OSError:
        size = 0
    return size


lines = 0
size = safe_getsize(hist_file)

if size > max_size_bytes:
    reset_file(size, max_size_bytes, "bytes")
else:
    try:
        readline.read_history_file(hist_file)
        lines = readline.get_current_history_length()
        if lines > max_size_lines:
            try:
                readline.clear_history()
            except NameError as e:
                print("readline.clear_history() not supported (%s), please delete history file %s by hand.\n" % (e, hist_file,))
            reset_file(lines, max_size_lines, "lines")
    except IOError:
        try:
            f = open(hist_file, 'a')
            f.close()
        except IOError:
            print("The file %s can't be created, check your hist_file variable.\n" % hist_file)

size = safe_getsize(hist_file)

print("Current history file (%s) size: %s bytes, %s lines.\n" % (hist_file, size, readline.get_current_history_length(),))

readline.parse_and_bind("tab: complete")

atexit.register(readline.write_history_file, hist_file)
