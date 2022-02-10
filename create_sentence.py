# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence.
# You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word.
# Be careful, there shouldn't be a space at the beginning or end of a sentence.

words = ['hello', 'world', 'this', 'is', 'great']

def create_sentence(words):
    sentence = " ".join(words).strip()

    return sentence

print(create_sentence(words))