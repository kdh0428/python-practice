import sys
import signal
 
class TimeoutException(Exception): 
    pass 
 
def get_name():
    def timeout_handler(signum, frame):
        raise TimeoutException()
 
    signal.signal(signal.SIGALRM, timeout_handler)  
    try: 
        signal.setitimer(signal.ITIMER_REAL,0.1)
        print "Please enter a name: ",
        name = sys.stdin.readline()

    except TimeoutException:
        signal.alarm(0) 

 
if __name__ == '__main__':
    name = get_name()
    print "Got: %s" % name,
