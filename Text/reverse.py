import sys

def reverse(string):
    return ''.join(string[i] for i in reversed(range(len(string))))

to_reverse = input('String to reverse: ')
print(reverse(to_reverse))


