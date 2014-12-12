from __future__ import print_function
print('abcd', end='5\n')


modname = 'test2'
some = __import__(modname)

from reloadall import * 
import os

#reload_all(os)



if __name__ == '__main__':
    some.a1()
    print('I\'m cool')