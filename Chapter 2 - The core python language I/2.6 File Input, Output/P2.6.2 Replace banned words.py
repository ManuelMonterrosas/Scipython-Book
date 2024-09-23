"""
Write a program to read in a text file and censor any words in it that are on a
list of banned words by replacing their letters with the same number of asterisks. Your
program should store the banned words in lower case but censor examples of these
words in any case. Assume there is no punctuation.
As a bonus exercise, handle text that contains punctuation. For example, given the
list of banned words: ['C', 'Perl', 'Fortran'] the sentence
'Some alternative programming languages to Python are C, C++, Perl , Fortran and
Java.'
becomes
'Some alternative programming languages to Python are *, C++, ****, ******* and
Java.'
"""

banned_words = ['C', 'Perl', 'Fortran']
banned_text = []  # I need to treat the text as a list first
option = 2
if option == 1:  # first without punctuation marks
    file_to_test = r'C:\Users\manym\Documents\Coding\Scipython-book\Chapter 2 - The core python language I\2.6 File Input, Output\sample-text-to-ban-A.txt'
    f = open(file_to_test, 'r')
    for line in f.readlines():
        sentence = line.split(' ')
        for word in sentence:
            if word in banned_words:
                banned_text.append(len(word)*'*')
            else:
                banned_text.append(word)
if option == 2:  # now with punctuation marks
    file_to_test = r'C:\Users\manym\Documents\Coding\Scipython-book\Chapter 2 - The core python language I\2.6 File Input, Output\sample-text-to-ban-B.txt'
    f = open(file_to_test, 'r')
    punctuation = [',', '.']
    for line in f.readlines():
        sentence = line.split(' ')
        for word in sentence:
            # remove punctuation marks, but remember what they were and where they were
            word = list(word)
            removed_index = []
            removed_string = []
            for i in range(len(word)-1, -1, -1): # go backwards to keep original index
                if word[i] in punctuation:
                    removed_index.append(i)
                    removed_string.append(word.pop(i))
            # now without punctuation marks, check if the words are banned
            # and return the puntuation marks if there was any
            if ''.join(word) in banned_words:
                word = list(len(word)*'*')
            for i in range(len(removed_index)-1, -1, -1):
                word.insert(removed_index[i], removed_string[i])
            banned_text.append(''.join(word))
f.close()
banned_text = ' '.join(banned_text)
print(banned_text)