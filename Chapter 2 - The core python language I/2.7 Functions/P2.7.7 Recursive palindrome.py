"""
Write a function that determines if a string is a palindrome (that is, reads the
same backward as forward) using recursion.
"""

def recursive_palindrome(word):
    """ Return True if word is a palindrome, or False otherwise.
    """
    # The strategy is as follows
    if len(word)<2:
        return True
    return word[0] == word[-1] and recursive_palindrome(word[1:-1])

words = ["kayak", "hannah", "kayaki", "hannahi"]

for test_word in words:
    if recursive_palindrome(test_word):
        print(f"{test_word} is a palindrome.")
    else:
        print(f"{test_word} is NOT a palindrome.")