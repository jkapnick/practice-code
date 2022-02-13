# You are going to be given a word. Your job is to return the middle character of the word. 
# If the word's length is odd, return the middle character. 
# If the word's length is even, return the middle 2 characters.

word = "middle"

def Get_Middle(word):
    middle = len(word) / 2
    remainder = len(word) % 2
    if remainder > 0:
        return word[round(middle) - 1]
    else:
        return word[int(middle) - 1] + word[int(middle)]

print(Get_Middle(word))
