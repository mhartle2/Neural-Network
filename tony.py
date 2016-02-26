import load_file as lf
import layer_of_neurons as ln
import network as net
import numpy as np
from sklearn import preprocessing

def main():
	# Load data files
	nRows_iris = 150
	nColumns_iris = 5
	num_epoch_iris = 1
	learning_rate_iris = .5
	nRows_diabetes = 768
	nColumns_diabetes = 9
	num_epoch_diabetes = 1
	learning_rate_diabetes = .5
	iris = lf.load_file("iris.csv", nRows_iris, nColumns_iris)
	diabetes = lf.load_file("diabetes.data", nRows_diabetes, nColumns_diabetes)

	# Collect target data before it is normalized
	iris_targets = []
	diabetes_targets = []

	for row in range(nRows_iris):
		iris_targets.append(iris[row][nColumns_iris - 1])

	for row in range(nRows_diabetes):
		diabetes_targets.append(diabetes[row][nColumns_diabetes - 1])

	# Normalize data files
	iris = preprocessing.normalize(iris)
	diabetes = preprocessing.normalize(diabetes)

	# Run Iris
	iris_num_layers_array = [1, 3] # Length is num_layers, each element is num_nodes	
	for i in range(num_epoch_iris):
		np.random.shuffle(iris)
		iris_net = net.network(iris_num_layers_array, nRows_iris, nColumns_iris, iris, "Iris", learning_rate_iris)
		iris_net.run_network()
		iris_net.generate_guesses()
		iris_net.update_weights()
		iris_net.print_accuracy(iris_targets)	
		if learning_rate_iris > .1:
			learning_rate_iris -= .001
		


	# Run Diabetes
	diabetes_num_layers_array = [1, 2]
	for i in range(num_epoch_diabetes):
		np.random.shuffle(diabetes)
		diabetes_net = net.network(diabetes_num_layers_array, nRows_diabetes, nColumns_diabetes, diabetes, "Diabetes", learning_rate_diabetes)
		diabetes_net.run_network()
		diabetes_net.generate_guesses()
		diabetes_net.update_weights()
		diabetes_net.print_accuracy(diabetes_targets)

		if learning_rate_diabetes > .1:
			learning_rate_diabetes -= .001


main()