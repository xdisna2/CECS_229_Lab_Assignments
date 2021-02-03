# Convert to Decimal from Hex

# Loop through each variable in List
for num in temp_list:
    print(num)
    # If this string is a DIGIT
    if num.isdigit():

        # Make that element to an integer and multiply by the 16 power of its index
        value = int(num) * (16 ** temp_list.index(num))
        # Add to the total
        sum += value

    # If this string is NOT A DIGIT
    else:
        value = (hex_letters.index(num) + 10) * (16 ** temp_list.index(num))
        sum += value

    print(value)
    print(sum)