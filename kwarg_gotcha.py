#!/usr/bin/env python3

"""
Demonstrates unexpected behavior of mutable kwargs.
"""

def set_kwarg(v, s=set()):
    s.add(v)
    print(s)

def list_kwarg(v, s=list()):
    s.append(v)
    print(s)

def tuple_kwarg(v, s=tuple()):
    # This syntax alone illustrates there will not really be the same
    # behavior... tuples are not modifiable
    s = s + (v,)
    print(s)


def main():
    print('set kwarg:')
    set_kwarg(1)
    set_kwarg(2)
    # Note that set elements in first call persist into second call.

    print('list kwarg:')
    list_kwarg(1)
    list_kwarg(2)

    print('tuple kwarg:')
    tuple_kwarg(1)
    tuple_kwarg(2)


if __name__ == '__main__':
    main()

