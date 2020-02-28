def is_palindrome(string):
    if string.lower() == string.lower()[::-1] :
        return True

print(is_palindrome('a man a plan a canal Panama'))
