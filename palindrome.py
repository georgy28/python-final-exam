def is_palindrome(word):
    word_lower = word.lower()
    w_len = len(word_lower)
    for index in range(w_len//2):
        if (word_lower[index] != word_lower[-1-index]):
            return False
    return True


# A few test cases
print(is_palindrome('Deleveled'))
print(is_palindrome('apapapaPAPAPAPA'))
print(is_palindrome('YOU ARE -- era uOY'))

print(is_palindrome('123-321'))
print(is_palindrome('AQ'))
print(is_palindrome('A'))
print(is_palindrome('Father'))
