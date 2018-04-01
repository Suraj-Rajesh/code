import sys, time
from os import system
from daemon import Daemon


def ac_enabled_users():
    return []


class AccessCheck(Daemon):
    def __init__(self, pidfile, ac_users):
        self.ac_users = ac_users
        super(AccessCheck, self).__init__(pidfile)

    def run(self):
        while True:
            system('echo %s >> /home/suraj/abc' % str(self.ac_users))
            time.sleep(1)

if __name__ == '__main__':
    ac_users = ac_enabled_users()

    daemon = AccessCheck('/tmp/access_check.pid', ac_users)
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print 'Unknown command'
            sys.exit(2)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
