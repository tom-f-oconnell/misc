#!/usr/bin/env python3

import timeit
import random

def foo():
    for i in range(random.randrange(10000)):
        j = i * 2


def main():
    # OK so it doesn't seem possible to get the best time from this interface.
    # It just returns the total time it took to repeat foo <number> times.
    # Kwargs: stmt, setup, timer, number, globals
    '''
    print(timeit.timeit(stmt=foo, number=10))
    print(timeit.timeit(stmt=foo, number=100))
    print(timeit.timeit(stmt=foo, number=10000))
    '''

    # Note: need to divide by "number" value to get time per run.

    # TODO if using setup kwarg, is that evaluated once or once for each of 
    # <number> repeats? is that sorta why <number> exists? or is it also just
    # to put really fast stuff in units easily readable in seconds? something
    # else?

    # Possible kwargs: stmt, setup, timer, globals
    timer = timeit.Timer(stmt=foo)
    # TODO something i don't understand: why not just increase repeat kwarg
    # to repeat fn, keeping number constant? why ever use number? why is that
    # what timeit takes?
    num, t1s = timer.autorange()
    t2 = timer.timeit(number=10000)
    t3 = timer.repeat(repeat=5, number=num)

    print(t1s)
    print(num)
    print(t2)
    print(t3)

    print('Time per run (seconds): {}'.format(t1s / num))
    print('Best time per run: {}'.format(min(t3) / num))

    # TODO and how does the globals kwargs work? how would i use it to pass
    # arguments to a fn as normal (*args and **kwargs)?
    #import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    main()

