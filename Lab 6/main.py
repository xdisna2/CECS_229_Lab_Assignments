import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# For proper labeling of the axes and title
col_list = ["Gestation","Age (Mother)","Number of Cigarettes (Mother)",
            "Height (Mother)","Pre-Pregnancy Weight (Mother)",
            "Age (Father)", "Years of Education (Father)",
            "Number of Cigarettes (Father)","Height (Father)"]
# Initialize starting index
col_num = 0

# Get data from csv file
birth_data = pd.read_csv("birthweight.csv")

# We only want the x-axis data to be compared to be Birthweight
x_axis = birth_data['Birthweight'].to_numpy()

# Loop through the columns, exception of Birthweight skip
for col in birth_data:
    # Basically skip the first value and set the y_axis to be the data column
    if col != 'Birthweight':
        # Set the column of the data to the y_axis via Numpy
        y_axis = birth_data[col].to_numpy()

        # Plot the scatter graph
        plt.scatter(x_axis, y_axis, color='red')

        # Set the axis Labels
        plt.xlabel('Birthweight')
        plt.ylabel(col_list[col_num])

        # Set the title
        plt.title(f"Birthweight vs. {col_list[col_num]}")

        # Plot the graph
        plt.show()

        # Increment the col_num list index
        col_num += 1
