## Author: Dustin Hu
##Date: 17-02-2014

##Function: TImer. Intake a given time, when given time starts off, it outputs it.

import time

def timer():
    intTime = int(raw_input("Time in integer seconds please.\n> "))
    print "Recieved %s" % intTime
    print "Now timing"
    time.sleep(intTime)
    print "ITS OVER"

timer()