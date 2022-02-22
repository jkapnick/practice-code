# You are given a string of n lines, each substring being n characters long. For example:
# s = "abcd\nefgh\nijkl\nmnop"
# We will study the "horizontal" and the "vertical" scaling of this square of strings.
#A k-horizontal scaling of a string consists of replicating k times each character of the string (except '\n').
# Example: 2-horizontal scaling of s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"
# A v-vertical scaling of a string consists of replicating v times each part of the squared string.
# Example: 2-vertical scaling of s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"
# Function scale(strng, k, v) will perform a k-horizontal scaling and a v-vertical scaling.
import string 
strng = "abcd\nefgh\nijkl\nmnop"
k = 4
v = 3

def scale(strng, k, v):
    horizontal_string = ''
    for char in strng:
        for n in range(k):
            horizontal_string = horizontal_string + char

    split_string = horizontal_string.splitlines()
    while("" in split_string) :
        split_string.remove("")

    repeat_string = ''
    for word in split_string:
        for lines in range(v):
            repeat_string = repeat_string + word + '\n'

    repeat_string = repeat_string.rstrip('\n')
    return repeat_string

print(scale(strng, k, v))