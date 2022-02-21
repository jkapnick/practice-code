# You are going to be given a word. 
# Your job will be to make sure that each character in that word has the exact same number of occurrences. 
# You will return true if it is valid, or false if it is not.

word = "1233"

def character_counter(word):
    char_count = {}
    result = True

    for character in word:
        if character.casefold() in char_count:
            char_count[character.casefold()] += 1
        else:
            char_count[character.casefold()] = 1

    compare_char = list(char_count.values())[0]
    for count in char_count:
        if char_count[count] != compare_char:
            result = False

    return result

print(character_counter(word))