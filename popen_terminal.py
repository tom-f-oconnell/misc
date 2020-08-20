#!/usr/bin/env python3

from subprocess import Popen, check_output
import os
from os.path import join
from pprint import pprint
import pickle

import yaml


#  From mluebke's answer at https://stackoverflow.com/questions/568271
def is_pid_running(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def main():
    cmd = ("gnome-terminal -x bash -i -c 'cd ~/src/hong2p; "
        "echo PID=$$; sleep 5; echo test2; sleep 10; echo   test3; bash'"
    )
    path = '/home/tom/src/automate2p'
    '''
    with open(join(path, 'media-tom-Extreme_SSD_config.yaml'), 'r') as f:
        cmd = yaml.load(f)['run_if_anything_copied'][0]['cmd']
    '''

    # This seems to return a dict, rather than an os._Environ, like os.environ.
    # Trying to pprint os.environ directly does not format things in the dict
    # style, which I wanted.
    '''
    env = os.environ.copy()
    #print('env:')
    #pprint(env)

    with open(join(path, 'test_popen_env.p'), 'wb') as f:
        pickle.dump(env, f)
    '''

    with open(join(path, 'test_popen_env.p'), 'rb') as f:
        env = pickle.load(f)

    # just loading this so i can compare interactively
    with open('/home/tom/src/automate2p/service_env.p', 'rb') as f:
        senv = pickle.load(f)

    print('Environment vars only in saved env:')
    pprint(set(env.keys()) - set(senv.keys()))

    #'''
    print('cmd:')
    print(cmd)
    print('\nbefore Popen')
    proc = Popen(cmd, shell=True, env=senv)
    pid = proc.pid
    print('child pid running right after Popen?', is_pid_running(pid))

    #out = check_output(cmd, shell=True)
    print('after Popen')
    #print('output:')
    #print(out)

    print('parent python script pid:', os.getpid())

    #print('running before sleeping 1s?', is_pid_running(pid))
    #import time; time.sleep(1)

    # doesn't seem to block for command inside other terminal to finish...
    # some way to do that?
    print('running before wait?', is_pid_running(pid))
    print('pid of process launching new terminal:', pid)
    #retcode = proc.wait()
    #print('running after wait?', is_pid_running(pid))
    #'''

    # TODO how to also wait for any processes started by the pid of the process
    # subprocess starts? (/ capture their output / retcodes too if possible)
    # possible?

    #import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    main()

