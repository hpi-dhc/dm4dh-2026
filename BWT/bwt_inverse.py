#!/usr/bin/python3

# Author: Dr. Matthieu-P. Schapranow
# E-Mail: <schapranow@hpi.de>
# Example code for BWT implemenation following DM4DH class assumptions, i.e. input strings start with '*' and end with '#'.

import functools
import string
from bwt_functions import *

# recursive lookup function
def lookup(bwt_arr, bwt_sorted, res, len_bwt, k):
    # stop condition
    if len(res) >= len_bwt:
        return res

    # lookup index i of the requested element k in bwt_arr
    i = bwt_arr.index(k)
    # retrieve new lookup key from bwt_sorted
    k = bwt_sorted[i]
    print (bwt_arr[i], "->", k)
    res += k[1]
    res=lookup(bwt_arr, bwt_sorted, res, len_bwt, k)

    return res

# step 1: transform input string to array 
def create_arr(input_text, len_text):
    rotation_arr = [(i+1, input_text[i:i+1]) for i in range(len_text)]
    return rotation_arr;

# step 2: sort rotations lexicographically
def sort_rotations(rotations):
    # Sorts rotations using comparison function defined above
    rotations.sort(key=functools.cmp_to_key(cmp_str_arr_func))
    return rotations;

# step 3: invert the given arrays
def invert(bwt_arr, bwt_sorted, len_bwt):

    # find initial index for reconstruction by looking up "#" in bwt array 
    for i in range(len_bwt):
        if (bwt_arr[i][1] == '#'):
            break

    res=""
    res=lookup(bwt_arr, bwt_sorted, res, len_bwt, bwt_arr[i])

    return res

if __name__ == "__main__":
    bwt_string = input("Please enter to BWT-encoded string to perform the inverse BWT operation on (use * = start and # = end of the string): ")
    len_text = len(bwt_string)
    print('Burrows - Wheeler Transform:', bwt_string)

    bwt_arr=create_arr(bwt_string, len_text)
    bwt_sorted=sort_rotations(bwt_arr.copy())
    print('1. BWT table:')
    pprint(bwt_arr)

    print('2. Lexicographically ordered BWT table:')
    pprint(bwt_sorted)

    print('3. Reconstructing path through BWT table:')
    input_str=invert(bwt_arr, bwt_sorted, len_text)
    print('Inverse of Burrows - Wheeler Transform:', input_str)

