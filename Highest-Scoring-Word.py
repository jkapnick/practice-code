# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

words = 'aa c'

def highest_scoring_word(words):

    import string
    alphabet = string.ascii_lowercase
    sentence = words.split()
    high_total = 0
    high_score_word = ''

    for word in sentence:
        total = 0
        for pos in word:
            if pos in alphabet:
                total += ord(pos) -96
    
        if total > high_total:
            high_total = total
            high_score_word = word
            
    return high_score_word, high_total

print(highest_scoring_word(words))