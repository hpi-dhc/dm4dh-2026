#!/usr/bin/python3

# Author: Dr. Matthieu-P. Schapranow
# E-Mail: <schapranow@hpi.de>
# Example code for BWT implemenation following DM4DH class assumptions, i.e. input strings start with '*' and end with '#'.

import functools
from bwt_functions import *  
 
# step 1: create a list of rotations from input string
def create_rotations(input_text, len_text):
    # Array of structures to store rotations and their indexes
    rotation_arr = [(i+1, input_text[i:] + input_text[0:i]) for i in range(len_text)]
    return rotation_arr;

# step 2: sort rotations lexicographically
def sort_rotations(rotations):
    # Sorts rotations using comparison function defined above
    rotations.sort(key=functools.cmp_to_key(cmp_str_arr_func));
    return rotations;
 
# step 3: get last character from each list of sorted rotations and concatenate as string
def get_last_chars(sorted_rotations, len_text):
    return ''.join([sorted_rotations[i][1][-1] for i in range(len_text)]);
 
if __name__ == "__main__":

    input_text = input("Please enter the string to apply BWT to: ")
    if (input_text[0] != '*'):
        input_text = '*' + input_text
    if (input_text[-1] != '#'):
        input_text = input_text + '#'
    len_text = len(input_text);

    print("Input text:", input_text);

    rotations=create_rotations(input_text, len_text);
    print('1. Letter rotations:');
    pprint(rotations);

    # Computes the suffix array of our text
    sorted_rotations = sort_rotations(rotations);
    print('2. Lexicographically ordered rotations:');
    pprint(sorted_rotations);
     
    # Adds to the output array the last char of each rotation
    bwt_string = get_last_chars(sorted_rotations, len_text);
    print("3. Burrows Wheeler Transform:", bwt_string);
