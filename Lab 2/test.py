string = "This is a 2nd test bench :)))"
n = 1
for characters in string:
    if characters.isalpha():
        if characters.isupper():
            x = ord(characters) - 65
            temp = (x + 1) % 26
            print(chr(temp+65))


