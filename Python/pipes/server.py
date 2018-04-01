import os, time, sys
pipe = '/var/tmp/simple_pipe'

def server():
    if not os.path.exists(pipe):
        os.mkfifo(pipe)

    pipein = open(pipe, 'r')
    
    while True:
        # :-1 in readline to remove '\n' read
        line = pipein.readline()[:-1]
        if line:
            os.system('echo %s >> /home/suraj/tamper_check' % line)
            print 'Parent %d got %s at %s' % (os.getpid(), line, time.time())
            
if __name__ == '__main__':
    server()
