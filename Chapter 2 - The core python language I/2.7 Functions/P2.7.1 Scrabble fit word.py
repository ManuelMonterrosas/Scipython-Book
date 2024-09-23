"""
The word game Scrabble is played on a 15 x 15 grid of squares referred to
by a row index letter (A–O) and a column index number (1–15). Write a function to
determine whether a word will fit in the grid, given the position of its first letter as a
string (e.g. 'G7') a variable indicating whether the word is placed to read across or
down the grid and the word itself.
"""

def will_it_fit(first_coord: str, orientation: str, word: str):
    """ Return True or False to know if a word will fit in scrabble board.
        Give the first coordinate of the string, the orientation ('across' or 'down'), and the word itself.
    """
    # The first letter of first_coord fives us the row index
    row_ind = first_coord[0]
    # To make this index a number I could write a letter to number dictionary/function
    # Or I found this function ord('a') which returns the integer that represents the character 'a'
    row_ind = ord(row_ind.upper()) - 64  # this makes sure that 'A' is mapped to 1 and 'O' is mapped to 15. Caveat is that they NEED to be capital
    # The column is given by either one or two numbers in the end of the string
    col_ind = int(first_coord[1:])
    len_word = len(word)
    if orientation == 'across':
        return col_ind + len_word - 1 <= 15
    elif orientation == 'down':
        return row_ind + len_word - 1 <= 15
    else:
        print("Invalid orientation")
        return
    # return row_ind, col_ind


# These should return False
print(will_it_fit('A1', 'across', 16*'A'))
print(will_it_fit('A1', 'down', 16*'A'))
print(will_it_fit('O15', 'across', 'AA'))
print(will_it_fit('O15', 'down', 'AA'))
print(will_it_fit('A15', 'across', 'AA'))

print(40*'-')

# These should return True
print(will_it_fit('A1', 'across', 15*'A'))
print(will_it_fit('A1', 'down', 15*'A'))
print(will_it_fit('O15', 'across', 'A'))
print(will_it_fit('O15', 'down', 'A'))
print(will_it_fit('A15', 'down', 'AA'))