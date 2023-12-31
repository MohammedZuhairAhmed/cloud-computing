def is_palindrome(word):
    return word == word[::-1]

user_input = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} is not a palindrome.")
