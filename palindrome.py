# C-like style
def is_palindrome(word):
    word_lower = word.lower()
    w_len = len(word_lower)
    for index in range(w_len//2):
        if (word_lower[index] != word_lower[-1-index]):
            return False
    return True


# fast way using slicing even though we check the whole strings (while half would be enough)

def is_palindrome2(word):
    l_word = word.lower()
    return l_word == l_word[::-1]

###################### CODE ENDS HERE ####################

############### EXAMPLES #################


# A few test cases
print(is_palindrome('Deleveled'))
print(is_palindrome2('apapapaPAPAPAPA'))

print(is_palindrome('YOU ARE -- era uOY'))
print(is_palindrome2('123-321'))

print(is_palindrome('AQ'))
print(is_palindrome2('A'))

print(is_palindrome('Father'))
print(is_palindrome2('Mother'))
