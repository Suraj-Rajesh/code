import os
import signal

def send_signal(proc_id, sig):
    os.kill(proc_id, sig)


def get_procid(proc):
    pass


if __name__ == '__main__':
    # sending SIGHUP
    send_signal(1234, signal.SIGHUP)
