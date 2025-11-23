from collections import deque


def is_palindrome(user_input):
    s = user_input.strip().lower()
    deq = deque(s)
    while len(deq) > 1:
        if deq.popleft() != deq.pop():
            return False

    return True


user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("Palindrome")
else:
    print("Not a palindrome")