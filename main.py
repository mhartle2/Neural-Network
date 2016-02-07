import load_file as lf
import layer_of_neurons as ln
import normalize as norm

def main():
	# Load data files
	nRows_iris = 150
	nColumns_iris = 5
	nRows_diabetes = 768
	nColumns_diabetes = 9
	iris = lf.load_file("iris.csv", nRows_iris, nColumns_iris)
	diabetes = lf.load_file("diabetes.data", nRows_diabetes, nColumns_diabetes)

	# Normalize data files
	iris = norm.normalize_iris(iris)
	diabetes = norm.normalize_diabetes(diabetes)

	# Feed inputs into neurons
	layer_of_iris = ln.layer_of_neurons(nRows_iris, nColumns_iris, iris, "Iris")
	layer_of_iris.run_neurons()
	layer_of_iris.print_results()

	layer_of_diabetes = ln.layer_of_neurons(nRows_diabetes, nColumns_diabetes, diabetes, "Diabetes")
	layer_of_diabetes.run_neurons()
	layer_of_diabetes.print_results()


main()