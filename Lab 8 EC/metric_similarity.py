import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math



# function name: most_similar_cosine
# inputs: file_name- name of the csv file that holds classes
		# test_vec- vector that you are trying to classify
# output: a string that states what class the function is
# task: return the best class (AS A STRING) by using the cosine similarity metric
# assumptions: The csv file will not have headers!
			# Each row of the csv file is a data vector for each class
			# The last column will represent the classes. The remaining columns hold the data
def most_similar_cosine(file_name, test_vec):

	# Gather data from csv file (This has no headers, so we set header = None)
	vector_data = pd.read_csv(file_name, header=None)

	# Change the data to np_arrays
	np_all = vector_data.values

	# Calculate each angle of the vectors in correlation to the test vector
	sim_numbers = []

	# Loop through each of the indexes of the vectors excluding the string at the end

	# Basically loop for each row or vector of the shape dimension of the array
	# Use the test vector index length to calculate the degrees (this will exclude the string)
	for row in range(np_all.shape[0]):

		# For every change in the csv vector erase these variables
		dot_ab = 0
		mag_a = 0
		mag_b = 0

		for i in range(len(test_vec)):
			# Find the dot products and magnitude sums

			# A = test vector
			# B = csv vector

			# Find A * B
			dot_ab += test_vec[i] * np_all[row, i]

			# Find Magnitude of A and B (without the square root)
			mag_a += test_vec[i] ** 2
			mag_b += np_all[row, i] ** 2

		# Use the sums to find the rest of the variables

		# This section will be ran ONCE per row on the np_array vectors
		# Take the square root
		mag_a = math.sqrt(mag_a)
		mag_b = math.sqrt(mag_b)

		# Use equation to calculate cos(theta) (cos_theta represents the similarity)
		cos_theta = dot_ab / (mag_a * mag_b)

		degree = math.degrees(math.acos(cos_theta))
		# Since we need to find the similarities store in a list
		sim_numbers.append(degree)

	# See which vector has the smallest angle (most similar) and return the row location of the vector
	sim_string_index = sim_numbers.index(min(sim_numbers))

	# Return the string of the class that was the most similar
	return np_all[sim_string_index, -1]

# function name: most_similar_euclid
# inputs: file_name- name of the csv file that holds classes
		# test_vec- vector that you are trying to classify
# output: a string that states what class the function is
# task: return the best class (AS A STRING) by using the euclidean distance metric
# assumptions: The csv file will not have headers!
			# Each row of the csv file is a data vector for each class
			# The last column will represent the classes. The remaining columns hold the data
def most_similar_euclid(file_name, test_vec):

	# Gather data from csv file (This has no headers, so we set header = None)
	vector_data = pd.read_csv(file_name, header=None)

	# Change the data to np_arrays
	np_all = vector_data.values

	# Calculate each distance of the vectors in correlation to the test vector
	distances_calc = []

	# Loop through each of the indexes of the vectors excluding the string at the end

	# Basically loop for each row or vector of the shape dimension of the array
	# Use the test vector index length to calculate the degrees (this will exclude the string)
	for row in range(np_all.shape[0]):

		# For every change in the csv vector erase these variables
		difference_ab = 0

		for i in range(len(test_vec)):
			# Find the difference between A and B between the test vector and csv vector

			# A = test vector
			# B = csv vector

			# Find A - B
			difference_ab += test_vec[i] - np_all[row, i]

		# For each csv vector do these operations once
		# Find the distance
		distance = math.sqrt(difference_ab ** 2 )

		# Append to list for similarity check
		distances_calc.append(distance)

	# See which vector has the smallest distance (most similar)
	sim_string_index = distances_calc.index(min(distances_calc))

	# Return the string of the class that was the most similar
	return np_all[sim_string_index, -1]


############### TEST CASES ###############
test_file = 'classes.csv'

test_vec1 = [5.1, 3.4, 1.5, 0.2]
test_vec2 = [6.0, 3.4, 4.5, 1.6]
test_vec3 = [6.5, 3.0, 5.5, 1.8]

print(most_similar_cosine(test_file, test_vec1)) # Iris-setosa
print(most_similar_euclid(test_file, test_vec1)) # Iris-setosa

print(most_similar_cosine(test_file, test_vec2)) # Iris-versicolor
print(most_similar_euclid(test_file, test_vec2)) # Iris-versicolor

print(most_similar_cosine(test_file, test_vec3)) # Iris-virginica
print(most_similar_euclid(test_file, test_vec3)) # Iris-virginica
