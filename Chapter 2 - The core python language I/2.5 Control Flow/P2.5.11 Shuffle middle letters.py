"""
Write a program to take a string of text (words, perhaps with punctuation,
separated by spaces) and output the same text with the middle letters shuffled randomly.
Keep any punctuation at the end of words. For example, the string:
Four score and seven years ago our fathers brought forth on this continent a new nation, conceived
in liberty, and dedicated to the proposition that all men are created equal.
might be rendered:
Four sorce and seevn yeras ago our fhtaers bhrogut ftroh on this cnnoientt a new noitan, cvieecond
in lbrteiy, and ddicetead to the ptosoiporin that all men are cetaerd euaql.
Hint: random.shuffle shuffles a list of items in place. See Section 4.5.1.
"""
from random import shuffle

sample_string = "Four score and seven years ago our fathers brought forth on this continent a new nation, conceived in liberty, and dedicated to the proposition that all men are created equal."
# sample_string = "a.."
punctuation = [",", "."]
words = sample_string.split(' ')
shuffled_string = []
for i in range(len(words)):  # for each word, I have to ignore punctuation marks and first and last letters
    current_word = words[i]
    current_word = list(current_word)  # makes the word a list so that I can shuffle it
    for j in range(len(current_word)):
        if current_word[j] in punctuation:
            break  # j contains the punctuation mark index. Assuming they are always in the end of a word.
        if j == len(current_word) - 1: # in the case we didn't find a punctuation mark, sum 1
            j += 1
    print(j)
    to_shuffle = current_word[1:j-1]
    shuffle(to_shuffle)  # shuffle the word
    if j>1:  # just when the string is long enough. prevents a -> aa
        current_word = current_word[:1] + to_shuffle + current_word[j-1:]
    current_word = ''.join(current_word)  # makes the word a string again
    shuffled_string.append(current_word)  # stores the string in a list
print(' '.join(shuffled_string))