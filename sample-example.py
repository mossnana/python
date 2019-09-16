import time
from threading import Thread as TH

def myfunc(i):
    print("sleeping 1 sec from thread {}".format(i))
    time.sleep(1)
    print("finished sleeping from thread {}".format(i))

# Use Thread
for i in range(10):
    t = TH(target=myfunc, args=(i,))
    print("start thread declear in {}".format(i))
    t.start()
    print("finish thread declear in {}".format(i))

# Not Use Thread
for i in range(10):
    print("Loop {}".format(i))
    print("waiting for loop ....")
    myfunc(i)
    print("finish execute myfunc()")

# Use Thread Result
"""
start thread declear in 0
sleeping 1 sec from thread 0
finish thread declear in 0
start thread declear in 1
sleeping 1 sec from thread 1
finish thread declear in 1
start thread declear in 2
sleeping 1 sec from thread 2
finish thread declear in 2
start thread declear in 3
sleeping 1 sec from thread 3
finish thread declear in 3
start thread declear in 4
sleeping 1 sec from thread 4
finish thread declear in 4
start thread declear in 5
sleeping 1 sec from thread 5
finish thread declear in 5
start thread declear in 6
sleeping 1 sec from thread 6
finish thread declear in 6
start thread declear in 7
sleeping 1 sec from thread 7
finish thread declear in 7
start thread declear in 8
sleeping 1 sec from thread 8
finish thread declear in 8
start thread declear in 9
sleeping 1 sec from thread 9
finish thread declear in 9
finished sleeping from thread 2
finished sleeping from thread 6
finished sleeping from thread 3
finished sleeping from thread 1
finished sleeping from thread 5
finished sleeping from thread 4
finished sleeping from thread 0
finished sleeping from thread 7
finished sleeping from thread 8
finished sleeping from thread 9
"""

# Not Use Thread Result
"""
Loop 0
waiting for loop ....
sleeping 1 sec from thread 0
finished sleeping from thread 0
finish execute myfunc()
Loop 1
waiting for loop ....
sleeping 1 sec from thread 1
finished sleeping from thread 1
finish execute myfunc()
Loop 2
waiting for loop ....
sleeping 1 sec from thread 2
finished sleeping from thread 2
finish execute myfunc()
Loop 3
waiting for loop ....
sleeping 1 sec from thread 3
finished sleeping from thread 3
finish execute myfunc()
Loop 4
waiting for loop ....
sleeping 1 sec from thread 4
finished sleeping from thread 4
finish execute myfunc()
Loop 5
waiting for loop ....
sleeping 1 sec from thread 5
finished sleeping from thread 5
finish execute myfunc()
Loop 6
waiting for loop ....
sleeping 1 sec from thread 6
finished sleeping from thread 6
finish execute myfunc()
Loop 7
waiting for loop ....
sleeping 1 sec from thread 7
finished sleeping from thread 7
finish execute myfunc()
Loop 8
waiting for loop ....
sleeping 1 sec from thread 8
finished sleeping from thread 8
finish execute myfunc()
Loop 9
waiting for loop ....
sleeping 1 sec from thread 9
finished sleeping from thread 9
finish execute myfunc()
"""
