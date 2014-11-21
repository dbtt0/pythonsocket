from time import sleep,ctime
import thread

def loop0():
    print 'start loop 0 at: ',ctime()
    sleep(4)
    print 'loop 0 done at: ',ctime()

def loop1():
    print 'start loop 1 at: ',ctime()
    sleep(4)
    print 'loop 1 done at: ',ctime()

def loop2():
    print 'start loop 2 at: ',ctime()
    sleep(4)
    print 'loop 2 done at: ',ctime()

def loop3():
    print 'start loop 3 at: ',ctime()
    sleep(4)
    print 'loop 3 done at: ',ctime()

def loop4():
    print 'start loop 4 at: ',ctime()
    sleep(4)
    print 'loop 4 done at: ',ctime()

def main():
    print 'starting at: ',ctime()
    thread.start_new_thread(loop0,())
    thread.start_new_thread(loop1,())
    thread.start_new_thread(loop2,())
    thread.start_new_thread(loop3,())
    thread.start_new_thread(loop4,())
    sleep(6)
    print 'ALL DONE AT: ',ctime()

if __name__=='__main__':
    main()
