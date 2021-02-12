# function name: shift_cipher_encode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the encoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS
def shift_cipher_encode(string, n):
	# First do a loop that cycles through the letters of the string
	# Check to see if it is in the alphabet (if not then append and skip)
	# If it is in the alphabet, check to see if its Upper or Lower
	# Lower then do Lower-Case equation and append
	# Upper then do Upper-Case equation and append


	# Lower - Case equation (ASCII - 97 + n) % 26
	# Upper - Case equation (ASCII - 65 + n) % 26

	pass



# function name: shift_cipher_decode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the decoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS
def shift_cipher_decode(string, n):
	# First do a loop that cycles through the letters of the string
	# Check to see if it is in the alphabet (if not then append and skip)
	# If it is in the alphabet, check to see if its Upper or Lower
	# Lower then do Lower-Case equation and append
	# Upper then do Upper-Case equation and append

	# Lower - Case equation (ASCII + 97 + n) % 26
	# Upper - Case equation (ASCII + 65 + n) % 26



	pass


# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run

# Wmfauw ak yjwsl! :)
print(shift_cipher_encode("Eunice is great! :)", 18)) 
# Qobkbny sc qbokd dyy!!!
print(shift_cipher_encode("Gerardo is great too!!!", 10)) 
# Gjwsfwit nx fqxt lwjfy! :I
print(shift_cipher_encode("Bernardo is also great! :D", 5)) 
# WYWM229 cm nby vymn wfumm un WMOFV
print(shift_cipher_encode("CECS229 is the best class at CSULB", 20)) 

# This is the 2nd lab.
print(shift_cipher_decode("Qefp fp qeb 2ka ixy.", 23))
# ThErE r m@ny m0rE Labs 2 come!
print(shift_cipher_decode("KyViV i d@ep d0iV Crsj 2 tfdv!", 17))
# s0 B prepared!
print(shift_cipher_decode("y0 H vxkvgxkj!", 6))
# pineapples
print(shift_cipher_decode("buzqmbbxqe", 12))




