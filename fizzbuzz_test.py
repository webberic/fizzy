'''
Unit tests for the fizzbuzz program
'''

# import the code to be tested
from fizzbuzz import fizz, buzz, fizzbuzz

def describe_a_fizzbuzz_program_that():

    def has_a_smoke_test():
        '''
        The purpose of a smoke test is to give us
        confidence that our testing infrastructure
        is set up correctly. We do that by creating
        a test that should ALWAYS pass.
        '''
        assert True

    def takes_a_numeric_input_and_returns_fizz_if_it_is_a_multiple_of_3():
        '''
        We need a function that can take a single input and that 
        returns a value which could either be "fizz" or just whatever
        the input was to begin with.
        '''
        assert fizz(3) == 'fizz'
        assert fizz(3.0) == 'fizz'
        assert fizz(4) == 4
        assert fizz(9) == 'fizz'
        assert fizz(17) == 17
        assert fizz(15) == 'fizz'
        assert fizz(5) == 5

    def takes_a_numeric_input_and_returns_buzz_if_it_is_a_multiple_of_5():
        '''
        We need a function that can take a single input and that 
        returns a value which could either be "buzz" or just whatever
        the input was to begin with.
        '''
        assert buzz(5) == 'buzz'
        assert buzz(4) == 4
        assert buzz(10) == 'buzz'
        assert buzz(17) == 17
        assert buzz(3) == 3
        assert buzz(15) == 'buzz'

    def takes_a_numeric_input_and_returns_buzz_if_it_is_a_multiple_of_15():
        '''
        We need a function that can take a single input and that 
        returns a value which could either be "fizzbuzz" or just whatever
        the input was to begin with.
        '''
        assert fizzbuzz(15) == 'fizzbuzz'
        assert fizzbuzz(4) == 4
        assert fizzbuzz(30) == 'fizzbuzz'
        assert fizzbuzz(17) == 17
        assert fizzbuzz(3) == 3
    def passes_non_numeric_inputs_through_as_is():
        '''
        
        '''
        assert fizz('abc') == 'abc'
        assert buzz('abc') == 'abc'
        