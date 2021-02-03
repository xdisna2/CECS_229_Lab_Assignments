# funtion name: to_decimal
# input: num (a non-negative non-decimal int as string)- ex: 11101, 7712, ABC
		#base (the number system you're converting from as an int)- ex: 2, 8, 16
# output: decimal representation of num AS INTEGER 
# restrictions: you are NOT allowed to use the Python int function
				# that will convert it to decimal for you. You should use
				# implement the algorithm discussed in class
# assumptions: num will always be non-negative
			#  num will always be a valid number ex: 31112 (base2) won't be an input
			#. if num has letters, they will always be captialized
			#  base will be 2, 8, or 16
def to_decimal(num, base):
	pass




# funtion name: to_base
# input: dec_num (a positive decimal integer)- ex: 1, 6, 10, 68, 102...
		#base (the number system you're converting from as an int)- ex: 2, 8, 16
# output: non-base-10 representation of dec_num AS STR
# restrictions: you are NOT allowed to use the Python int function
				# that will convert it for you. You should use
				# implement the algorithm discussed in class
# assumptions: dec_num will always be non-negative
			#  base will be 2, 8, or 16				
def to_base(dec_num, base):
	pass





# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
print(to_decimal('101', 2)) # 5
print(to_decimal('1110', 2)) #14
print(to_decimal('642', 8)) #418
print(to_decimal('1342', 8)) #738
print(to_decimal('65', 16)) #101
print(to_decimal('57A', 16)) #1402

print(to_base(123, 2)) # '1111011'
print(to_base(400, 2)) # '110010000'
print(to_base(3424, 8)) # '6540'
print(to_base(5212, 8)) # '12134'
print(to_base(16423, 16)) # '4027'
print(to_base(15967, 16)) # '3E5F'





