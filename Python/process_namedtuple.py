from subprocess import Popen, PIPE
from collections import namedtuple

# ProcessInfo Class: inherits namedtuple
ProcessInfo = namedtuple('ProcessInfo', ['return_code', 'stdout', 'stderr'])

# Call an external command as a process
def Process(command):
    proc = Popen(command.split(), stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    return ProcessInfo(return_code=proc.returncode, stdout=out, stderr=err)

# Testing
p_info = Process('ls -lrt')
print '\nreturn code: ' + str(p_info.return_code)
print 'stdout:\n' + p_info.stdout
print 'stderr:\n' + p_info.stderr
