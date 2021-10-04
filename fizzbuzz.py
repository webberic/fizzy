'''
A fizzbuzz program
'''

#utility class for determining if a variable is numeric
from numbers import Number

def fizz(x):
    '''
    Takes a single input, returns 'fizz' if that
    input is a multiple of 3, and just returns the
    input "as is" if it is not a multiple of 3.
    '''
    return 'fizz' if isinstance(x, Number) and x % 3 == 0 else x

def buzz(x):
    '''
    Takes a single input, returns 'buzz' if that
    input is a multiple of 5, and just returns the
    input "as is" if it is not a multiple of 5.
    '''
    return 'buzz' if isinstance(x, Number) and x % 5 == 0 else x

def fizzbuzz(x):
    '''
    Takes a single input, returns 'fizzbuzz' if that
    input is a multiple of 15, and just returns the
    input "as is" if it is not a multiple of 15.
    '''
    return 'fizzbuzz' if isinstance(x, Number) and x % 15 == 0 else x

for x in range(1,101):
    print(fizz(buzz(fizzbuzz(x))))