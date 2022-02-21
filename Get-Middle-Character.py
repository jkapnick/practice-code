# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

word = "testing"

def Get_Middle(word):
    length = len(word)
    if length == 1:
        middle = 1
    else:
        middle = length / 2
    remainder = len(word) % 2
    
    if remainder > 0:
        middle += .5
        return word[int(middle) - 1]
    else:
        return word[int(middle) - 1] + word[int(middle)]

print(Get_Middle(word))
