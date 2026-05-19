#/usr/bin/python3

# Author: Dr. Matthieu-P. Schapranow
# E-Mail: <schapranow@hpi.de>
# Shared functions for BWT implementations following DM4DH class assumptions.

# compares two chars using rules defined in class, e.g. * and # at the end of the alphabet.
def cmp_char_func(x,y):
    # handle special chars
    if (x == '*'):
            x_ord = 256;
    elif (x == '#'):
            x_ord = 257;
    else:
        x_ord = ord(str.lower(x));

    if (y == '*'):
            y_ord = 256;
    elif (y == '#'):
            y_ord = 257;
    else:
        y_ord = ord(str.lower(y));

    return (x_ord > y_ord) - (x_ord < y_ord)

# compares two given strings lexicographically as defined in class.
def cmp_str_arr_func(x, y):
    # transform to lowercase for comparison
    # get legth of strings, only use the smaller one
    x=x[1];
    x_len=len(x);

    y=y[1];
    y_len=len(y)

    # continue to do character-based comparison if no char difference was detected
    for i in range(min(x_len, y_len)):
        res=cmp_char_func(x[i], y[i]);
        if (res != 0):
            break; 

    return res;


def pprint(array):
    for i in array:
       print(i);
