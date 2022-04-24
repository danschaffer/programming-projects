#!/usr/bin/env python

# usage: py.py iteration,default 100,000

import time
import sys

if len(sys.argv) > 1:
    iterations = 10**int(sys.argv[1])
else:
    print("pi.py iterations,10**n")
    sys.exit(1)

def get_time(secs):
    result = ''
    if secs > 60*60*24:
        result += f"{secs//60*60*24}d"
        secs = secs % 60*60*24
    if secs > 60*60:
        result += f"{secs//60*60}h"
        secs = secs % 60*60
    if secs > 60:
        result += f"{secs//60}m"
        secs = secs % 60*60*24
        secs = secs % 60
    result += f"{round(secs,1)}s"
    return result

pi = 0.0
start = time.time()
for k in range(iterations+1):
    pi += (-1)**k / float((2*k)+1)
secs = time.time() - start
print(f"iterations: {iterations} 10**{sys.argv[1]}")
print(f"time      : {get_time(secs)}")
print(f"result    : {4*pi}")
