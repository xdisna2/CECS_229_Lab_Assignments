# hash table
class hash_table:

	# constructor
	# inputs: size (defaults to 8 if no arguments are provided)
	def __init__(self, size = 8):
		# self.table: empty hash table of indicated size
		self.table = (None,) * size
		# self.size: number of positions in table
		self.size = size

	# Already completed function!
	# INSERTS value INTO HASHTABLE AT index
	# example: insert(5, 10) will place 5 into index#10
	def insert(self, value, index):
		temp = list(self.table)
		temp[index] = value
		self.table = tuple(temp)

	# function name: linear_probe
	# input: value- value to be inserted
			#start_index- where linear probing starts
	# output: returns the index of the hash_table that the value should be 
		#	inserted after linear probing
	# assumptions: value will always be an integer
		#	your table will always be big enough
	def linear_probe(self, value, start_index):

		found = False

		for i in range(start_index, self.size):
			if self.table[i] == None:
				found = True
				return i

		if not found:
			for i in range(start_index + 1):
				if self.table[i] == None:
					return i

	# function name: insert
	# input: value- value to be inserted
	# output: Do not return anything. Just insert value into the proper position
		#	in self.table. Utilize linear_probe and insert in this function
	# assumptions: value will always be an integer
		#	your table will always be big enough
	def hash(self, value):

		index_start = value % self.size

		insertion_index = self.linear_probe(value, index_start)

		self.insert(value, insertion_index)

	# Already completed function!
	def get_table(self):
		return self.table

	# Already completed function!
	def __str__(self):
		return str(self.table)








