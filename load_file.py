import numpy as np
def load_file(file_name, num_rows, num_columns):
	the_file = open(file_name, "r")
	array_to_return = np.zeros(shape=(num_rows, num_columns))
	row = 0
	for line in the_file:
		line_to_append = line.split(",")
		for column in range(len(line_to_append)):
			array_to_return[row][column] = line_to_append[column]
		row += 1

	return array_to_return