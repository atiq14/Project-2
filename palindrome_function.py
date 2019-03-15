# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 18:11:17 2019
Objective:
    To explore the Spyder IDE
    Python Basic try out
    Test cases
    Static code analysis
Description:
    Palindrome sequence: if character are same after reversing them
    on char list
    positive number is Palindrome, if reversing the number position
@author: Atiqur Rahman Bhuiyan
Version:SW-P_0015
Date: 13/03/19
Testcases:
    is_int_number_palindrome() verified with positive, negative and zero value
    is_palindrome() verified with different input char such as letter, number,
    symbol etc.

"""


def is_palindrome(user_input):
    """Whether user giving input char's are same, after reversing them .
       Print the result
    Args:
        user_input: the user input from console.

    Returns:
        The return value is True/False.

    """
    user_input_rev = reversed(user_input)
    if list(user_input) == list(user_input_rev):
        print('True, it is a palindrome input')
        return True
    else:
        print("False, this isn't a plindrome input")
        return False


def is_int_number_palindrome(user_given_number):
    """Whether integer number is palindrome.
       Print the result
    Args:
        user_given_number: input number.

    Returns:
        The return value is None.
    """
    temp_number = user_given_number
    reverse_number = 0
    while user_given_number > 0:
        reminder = user_given_number % 10
        reverse_number = reverse_number * 10 + reminder
        user_given_number = user_given_number // 10
    if temp_number == reverse_number:
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")
def user_input_request_for_characters():
    """
    Asking user to give any characters as INPUT.
    Args:No Arguments.
    Returns:The return value of User Input.
    """
    print("Please type whatever you want and after that press ENTER key")
    user_input = input()
    return user_input
def user_input_request_for_positive_numbers():
    """
    Asking user to give only positive numbers as INPUT.
    Args:No Arguments.
    Returns:The return value of User number input.
    """
    user_given_number = int(input("Enter any positive number you want:"))
    return user_given_number
#Function Calling Block
#=============================================================================


INPUT = user_input_request_for_characters()
OUTPUT = is_palindrome(INPUT)
print("Boolean Output:")
print(OUTPUT)

NUMBER_INPUT = int(user_input_request_for_positive_numbers())
is_int_number_palindrome(NUMBER_INPUT)
#=============================================================================

#Test Case Block
TESTINPUT = [121, 123, 0, -123, -121]
is_int_number_palindrome(TESTINPUT[0])
is_int_number_palindrome(TESTINPUT[1])
is_int_number_palindrome(TESTINPUT[2])
is_int_number_palindrome(TESTINPUT[3])
is_int_number_palindrome(TESTINPUT[4])

TESTINPUT1 = ['als', 'asas', '121', 'w§w', '  2  ']
is_palindrome(TESTINPUT1[0])
is_palindrome(TESTINPUT1[1])
is_palindrome(TESTINPUT1[2])
is_palindrome(TESTINPUT1[3])
is_palindrome(TESTINPUT1[4])
