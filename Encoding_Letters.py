# This program encodes the letters of a given string placed at even places by shifting them by their
# unicode by decreasing or incresing their unicode according to user input, while the rest of the string
# is printed without changes. Given string is at first transformed to lower case.

word = input().lower()
n = int(input())
if n % 26 == 0:
    print(word)
else:
    while n < 0:
        n += 26
    while n > 26:
        n -= 26
    for pos, i in enumerate(word):
        if pos % 2 == 1 and i.isalpha():
            if chr(ord(i) + n).isalpha():
                print(chr(ord(i) + n), end="")
            else:
                print(chr(ord(i) + n - 26), end="")
        else:
            print(i, end="")
