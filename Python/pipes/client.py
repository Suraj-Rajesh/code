import os, time, sys
pipe = '/var/tmp/simple_pipe'

def client():
    no = 1

    pipeout = open(pipe, 'w')
    pipeout.write('Number %03d\n' % no)

####### Alternate ########

#   pipeout = os.open(pipe, os.O_WRONLY)
#   os.write(pipeout, 'Number %03d\n' % no)

if __name__ == '__main__':
    client()
