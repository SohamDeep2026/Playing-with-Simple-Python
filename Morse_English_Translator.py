# This is a choice-based program translates user-input Morse code to English, and generates Morse code of an English user-input.
# The considered Morse code is the International Morse Code:
# 1. Length of a dot and a dash are 1 and 3 units respectively(This hasn't been required in the program though)
# 2. There are 1 space between parts of same letter, 3 spaces between different letters but same word, and 7 spaces between letters of different words.

# Sample test cases:
# Morse 1: . - - .   - . - -       . .   . . .       . . - .   . . -   - .
# English 1: py is fun
# Morse 2: . - - .   - . - -   -   . . . .   - - -   - .       . . . - -       . .   . . .       . . - .   . . -   - .
# English 2: python 3 is fun

morse_code = (
    ("a", ". -"),
    ("b", "- . . ."),
    ("c", "- . - ."),
    ("d", "- . ."),
    ("e", "."),
    ("f", ". . - ."),
    ("g", "- - ."),
    ("h", ". . . ."),
    ("i", ". ."),
    ("j", ". - - -"),
    ("k", "- . -"),
    ("l", ". - . ."),
    ("m", "- -"),
    ("n", "- ."),
    ("o", "- - -"),
    ("p", ". - - ."),
    ("q", "- - . -"),
    ("r", ". - ."),
    ("s", ". . ."),
    ("t", "-"),
    ("u", ". . -"),
    ("v", ". . . -"),
    ("w", ". - -"),
    ("x", "- . . -"),
    ("y", "- . - -"),
    ("z", "- - . ."),
    ("0", "- - - - -"),
    ("1", ". - - - -"),
    ("2", ". . - - -"),
    ("3", ". . . - -"),
    ("4", ". . . . -"),
    ("5", ". . . . ."),
    ("6", "- . . . ."),
    ("7", "- - . . ."),
    ("8", "- - - . ."),
    ("9", "- - - - ."),
)

choice = input("Enter 0 to translate from English to Morse,\nEnter 1 to translate from Morse to English\n")

if choice == "0":
    eng_input = input("Enter the English sentence to be translated.\n").lower().split(" ")

    eng_words = []
    for i in range(len(eng_input)):
        eng_words.append(eng_input[i])
        eng_words.append(" ")
    eng_words.pop()

    eng_letters = []
    for i in eng_words:
        eng_letters.append(list(i))

    translation = ""
    for i in eng_letters:
        for j in i:
            if j != " ":
                for k in range(len(morse_code)):
                    if j == morse_code[k][0]:
                        translation += morse_code[k][1]
                translation += "   "
            else:
                translation += "    "

    print("Translation in Morse:\n", translation, sep="")

elif choice == "1":
    morse_input = input("Enter the morse code to be translated.\n").lower().split("       ")

    morse_words = []
    for i in range(len(morse_input)):
        morse_words.append(morse_input[i])
        morse_words.append(" ")
    morse_words.pop()

    morse_letters = []
    for i in morse_words:
        morse_letters.append(i.split("   "))
    translation = ""
    for i in morse_letters:
        for j in i:
            if j != " ":
                for k in range(len(morse_code)):
                    if j == morse_code[k][1]:
                        translation += morse_code[k][0]
            else:
                translation += " "

    print("Translation in English:\n", translation, sep="")

else:
    print("Invalid choice")
