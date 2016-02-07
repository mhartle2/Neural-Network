import load_file as lf
import layer_of_neurons as ln
import neuron as n

def main():
	# Load data files
	nRows_iris = 150
	nColumns_iris = 5
	nRows_diabetes = 768
	nColumns_diabetes = 9
	iris = lf.load_file("iris.csv", nRows_iris, nColumns_iris)
	diabetes = lf.load_file("diabetes.data", nRows_diabetes, nColumns_diabetes)

	# Normalize data files

	# Feed inputs into neurons
	layer_of_iris = ln.layer_of_neurons(nRows_iris)
	for row in range(nRows_iris):
		iris_inputs = []
		for column in range(nColumns_iris):
			if column != nColumns_iris - 1:
				iris_inputs.append(iris[row][column])
		iris_neuron = n.neuron(iris_inputs)
		layer_of_iris.add_neuron(iris_neuron)
	print("Iris Results:________________________")
	layer_of_iris.run_neurons()
	layer_of_iris.print_results()


	layer_of_diabetes = ln.layer_of_neurons(nRows_diabetes)
	for row in range(nRows_diabetes):
		diabetes_inputs = []
		for column in range(nColumns_diabetes):
			if column != nColumns_diabetes - 1:
				diabetes_inputs.append(diabetes[row][column])
		diabetes_neuron = n.neuron(diabetes_inputs) 
		layer_of_diabetes.add_neuron(diabetes_neuron)
	print("Diabetes Results:___________________")
	layer_of_diabetes.run_neurons()
	layer_of_diabetes.print_results()


main()