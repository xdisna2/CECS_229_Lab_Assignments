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
	# Read file data from csv
	data_xy = pd.read_csv(file_name)

	# Get matrix X and Y
	mat_x = data_xy['x'].to_numpy()
	mat_y = data_xy['y'].to_numpy()

	# Get matrix X^2
	mat_x2 = mat_x**2

	# Get matrix XY
	mat_xy = mat_x * mat_y

	# Find the Sum of all three above
	sum_x = sum(mat_x)
	sum_y = sum(mat_y)
	sum_x2 = sum(mat_x2)
	sum_xy = sum(mat_xy)

	# Find the Slope using the equation given in the PDF
	pair_size = mat_x.size

	slope = ((pair_size * sum_xy) - (sum_x * sum_y)) / ((pair_size * sum_x2) - (sum_x**2))
	# Find the Y-Intercept given in the PDF

	y_cept = (sum_y - (slope * sum_x)) / pair_size

	# Round to 4 decimal places for both values calculated
	slope = round(slope, 4)
	y_cept = round(y_cept, 4)

	# Return those two values

	return slope, y_cept

# function name: mat_least_sq
# inputs: file_name- name of the csv file 
# output: m (slope), b(y-intercept) (IN THAT EXACT ORDER!!!)
		# LITERALLY! return m, b (both rounded 4 decimal places)
		# YOU HAVE BEEN WARNED! YOU WILL GET IT WRONG IF YOU DO NOT RETURN THE CORRECT THINGS IN THE CORRECT ORDER!
# assumptions: The csv file will always have headers in the order of: x, y
def mat_least_sq(file_name):

	# Read Data from CSV
	data_xy = pd.read_csv(file_name)

	# Get the x-coordinates and y-coordinates Matrix
	mat_x = data_xy['x'].to_numpy()
	mat_y = data_xy['y'].to_numpy()

	# Make a column of ONES that's equal of size to x-coordinate Matrix
	pair_size = mat_x.size
	col_one = np.ones(pair_size)

	# Concatenate the two matrices into the X matrix
	X_mat = np.column_stack((mat_x, col_one))

	# Find the slope and y-intercept using the equation in the PDF
	X_trans = X_mat.T
	Xt_X = X_trans.dot(X_mat)
	inverse_Xt = np.linalg.inv(Xt_X)
	Xt_y = X_trans.dot(mat_y)

	slop_inter = inverse_Xt.dot(Xt_y)

	# Round to 4 decimal places for both values calculated
	# Return those two values
	slope = round(slop_inter[0], 4)

	y_inter = round(slop_inter[1], 4)

	return slope, y_inter



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
	df_xy = pd.read_csv(file_name)

	# Configure using to_numpy() (Look at Lab 6 Main for reference)
	main_x = df_xy['x'].to_numpy()
	main_y = df_xy['y'].to_numpy()

	# Plot using SCATTER
	plt.scatter(main_x, main_y, color='red', label='data points')

	plt.xlabel("X-Coordinates")
	plt.ylabel("Y-Coordinates")

	# Determine what type of plot we are graphing
	# True = mat_least_Sq
	# False = least_sq

	# If True, then call the mat_least_Sq and pass the file_name
	if using_matrix:
		# Receive the slope and Y-intercept
		slope, y_inter = mat_least_sq(file_name)

		# Based on the type of graph change the titles
		# Concatenate the legend_label as well
		plt.title("Using Matrix Least Squares")
		legend_label = "y=" + str(slope) + "x+" + str(y_inter)

	# If False, do the same process just with a different function
	else:
		# Receive the slope and Y-intercept
		slope, y_inter = least_sq(file_name)

		# Based on the type of graph change the titles
		# Concatenate the legend_label as well
		plt.title("Using Algebra Least Squares")
		legend_label = "y=" + str(slope) + "x+" + str(y_inter)

	# Take the smallest and largest x-coordinate and plug it into the equation
	min_x, max_x = min(main_x), max(main_x)

	# Find the corresponding y-coordinate
	min_y = (min_x * slope) + y_inter
	max_y = (max_x * slope) + y_inter

	# Place into list
	x_coords = [min_x, max_x]
	y_coords = [min_y, max_y]

	# Plot those two points using the regular plot
	plt.plot(x_coords, y_coords, color='blue', label=legend_label)

	# Show the legend and plot at the end
	plt.legend()
	plt.show()

######## TEST CASES ########
csv_file = "data2.csv"

m1, b1 = least_sq(csv_file)
print("Slope using algebraic least squares:", m1)
print("y-intercept using algebraic least squares:", b1)
print()

m2, b2 = mat_least_sq(csv_file)
print("Slope using linear algebra least squares:", m2)
print("y-intercept using linear algebra least squares:", b2)

plot_reg(csv_file, True)
plot_reg(csv_file, False)

