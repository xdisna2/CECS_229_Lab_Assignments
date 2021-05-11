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

	# Gather data from csv file

	# Calculate each angle of the vectors in correlation to the test vector

	# See which vector has the smallest angle (most similar)

	# Return the string of the class that was the most similar

	pass



# function name: most_similar_euclid
# inputs: file_name- name of the csv file that holds classes
		# test_vec- vector that you are trying to classify
# output: a string that states what class the function is
# task: return the best class (AS A STRING) by using the euclidean distance metric
# assumptions: The csv file will not have headers!
			# Each row of the csv file is a data vector for each class
			# The last column will represent the classes. The remaining columns hold the data
def most_similar_euclid(file_name, test_vec):

	# Gather data from csv file

	# Calculate each distance of the vectors in correlation to the test vector

	# See which vector has the smallest distance (most similar)

	# Return the string of the class that was the most similar

	pass


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
