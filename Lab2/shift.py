# function name: shift_cipher_encode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the encoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS
def shift_cipher_encode(string, n):

	# Lower - Case equation (ASCII - 97 + n) % 26
	# Upper - Case equation (ASCII - 65 + n) % 26

	ciphered = []
	# First do a loop that cycles through the letters of the string
	for characters in string:
		# Check to see if it is in the alphabet (if not then append and skip)
		if characters.isalpha():
			# If it is in the alphabet, check to see if its Upper or Lower

			if characters.isupper():
				# Upper then do Upper-Case equation and append
				x = ord(characters) - 65
				temp = ((x + n) % 26) + 65

			# Lower then do Lower-Case equation and append
			else:
				x = ord(characters) - 97
				temp = ((x + n) % 26) + 97

			ciph = chr(temp)
			ciphered.append(ciph)

		else:
			# This is to account for non-alphabetical .,*spaces etc.
			ciphered.append(characters)

	converted = ""
	for element in ciphered:
		converted += element

	return converted

# function name: shift_cipher_decode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the decoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS
def shift_cipher_decode(string, n):

	# Lower - Case equation (ASCII + 97 + n) % 26
	# Upper - Case equation (ASCII + 65 + n) % 26

	ciphered = []
	# First do a loop that cycles through the letters of the string
	for characters in string:
		# Check to see if it is in the alphabet (if not then append and skip)
		if characters.isalpha():
			# If it is in the alphabet, check to see if its Upper or Lower

			if characters.isupper():
				# Upper then do Upper-Case equation and append
				x = ord(characters) - 65
				temp = ((x - n) % 26) + 65

			# Lower then do Lower-Case equation and append
			else:
				# Basically translate it to equal 0-25 alphabet letters
				x = ord(characters) - 97
				# Then in the end add back 97 to get the shifted value
				temp = ((x - n) % 26) + 97

			ciph = chr(temp)
			ciphered.append(ciph)

		else:
			# This is to account for non-alphabetical .,*spaces etc.
			ciphered.append(characters)

	converted = ""
	for element in ciphered:
		converted += element

	return converted




