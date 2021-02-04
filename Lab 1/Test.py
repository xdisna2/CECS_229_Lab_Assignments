converted = ''
string = 12

number_range = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

# If its a hex number value beyond 9, then use this list
x = 1
stop = True

while stop:
    # Take the dec_num and divide by base floored
    number = string // 2

    # Find the remainder
    remainder = string % 2

    # Theoretically take the index of the remainder and concatenate to converted string
    converted += number_range[number_range.index(str(remainder))]

    string = number

    if number == 0:
        stop = False

print(converted)