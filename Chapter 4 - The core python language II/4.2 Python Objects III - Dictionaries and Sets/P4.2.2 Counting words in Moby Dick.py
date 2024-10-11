""" The novel Moby-Dick is out of copyright and can be downloaded as a text
file from the Project Gutenberg website at www.gutenberg.org/2/7/0/2701/. Write a
program to output the 100 words most frequently used in the book by storing a count of
each word encountered in a dictionary.
Hint: use Python's string methods to strip out any punctuation. It suffices to replace
any instances of the following characters with the empty string: !?":;,()'.*[]. When
you have a dictionary with words as the keys and the corresponding word counts as the
values, create a list of (count, word) tuples and sort it.
Bonus exercise: compare the frequencies of the top 2000 words in Moby-Dick with
the prediction of Zipf's law:
                log f(w) = log C - a*log r(w);
where f(w) is the number of occurrences of word w, r(w) is the corresponding rank
(1 = most common, 2 = second most common, etc.) and C and a are constants. In the
traditional formulation of the law, C = log f (w1) and a = 1, where w1 is the most
common word, such that r(w1) = 1.
"""