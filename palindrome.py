def is_palindrome(word):
    return word == word[::-1]

user_input = raw_input("Enter a word to check if it's a palindrome: ")
if is_palindrome(user_input):
    print("{} is a palindrome!".format(user_input))
else:
    print("{} is not a palindrome.".format(user_input))
