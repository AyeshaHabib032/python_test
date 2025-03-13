def reverse_string(word):
    return ''.join(reversed(word))

def test_reverse_string():
    input_str = "TripleTen"

    reversed_str = reverse_string(input_str)
    print(reversed_str)
    assert reversed_str == "neTelpirT"
    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)


def is_palindrome(word):
    # Reverse the string using reversed() and join().
    reversed_str = ''.join(reversed(word))
    return word == reversed_str


# Test. Verification of is_palindrome function
def test_is_palindrome():
    input_str = "racecar"
    result = is_palindrome(input_str)
    assert result == True
    print("Test Passed! '" + input_str + "' is a palindrome.")

import math

def compute_factorial(number):
       return math.factorial(number)
def test_compute_factorial():
    input_number = 6
    result = compute_factorial(input_number)
    assert result == 720
    print("Test Passed! The factorial of " + str(input_number) + " is " + str(result))