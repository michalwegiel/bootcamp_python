def is_palindrome(data):
    if type(data) is not str:
        raise ValueError

    d = ""
    for letter in data:
        if letter.isalpha():
            d += letter
    d = d.lower()
    return d == d[::-1]

