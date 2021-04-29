import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# function name: least_sq
# inputs: file_name- name of the csv file 
# output: m(slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY! return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!!!!
# assumptions: The csv file will always have headers in the order of: x, y
def least_sq(file_name):

	# Get matrix X and Y
	# Get matrix X^2
	# Get matrix XY

	# Find the Sum of all three above

	# Find the Slope using the equation given in the PDF

	# Find the Y-Intercept given in the PDF

	# Round to 4 decimal places for both values calculated

	# Return those two values

	pass


# function name: mat_least_sq
# inputs: file_name- name of the csv file 
# output: m (slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY! return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!
# assumptions: The csv file will always have headers in the order of: x, y
def mat_least_sq(file_name):

	# Get the x-coordinates Matrix

	# Make a column of ONES that's equal of size to x-coordinate Matrix

	# Concatenate the two matrices into the X matrix

	# Find the slope and y-intercept using the equation in the PDF

	# Round to 4 decimal places for both values calculated

	# Return those two values


	pass



# function name: plot_reg
# inputs: mat - file_name- name of the csv file
		# using_matrix: True if you are plotting the linear equation from mat_least_Sq
		# 				False if you are plotting the linear equation from least_sq
# output: NA
# task: given file_name, compute the linear equation using least_sq or mat_least_sq and graph results
	#	your graph should have the following: labeled x and y axes, title, legend
# assumptions: The csv file will always have headers in the order of: x, y
def plot_reg(file_name, using_matrix):

	# Get data from the file_name
	# Configure using to_numpy() (Look at Lab 6 Main for reference)
	# Plot using SCATTER



	# Determine what type of plot we are graphing
	# True = mat_least_Sq
	# False = least_sq

	# If True, then call the mat_least_Sq and pass the file_name

	# Receive the slope and Y-intercept
	# Take the smallest and largest x-coordinate and plug it into the equation
	# Plot those two points using the regular plot

	# If False, do the same process just with a different function

	# Receive the slope and Y-intercept
	# Take the smallest and largest x-coordinate and plug it into the equation
	# Plot those two points using the regular plot

	pass

######## TEST CASES ########
csv_file = "data.csv"

m1, b1 = least_sq(csv_file)
print("Slope using algebraic least squares:", m1)
print("y-intercept using algebraic least squares:", b1)
print()

m2, b2 = mat_least_sq(csv_file)
print("Slope using linear algebra least squares:", m2)
print("y-intercept using linear algebra least squares:", b2)

plot_reg(csv_file, True)

plot_reg(csv_file, False)

