import neuron as n
import itertools
class layer_of_neurons():
	def __init__(self, num_rows, num_columns, data_set, name_of_data_set, num_nodes, end_of_num_layers_array, layerNumber, learning_rate):
		self.data_set = data_set
		self.num_rows = num_rows
		self.num_columns = num_columns
		self.list_of_neurons = []
		for row in range(num_rows):
			inputs = []
			for column in range(num_columns):
				if column != num_columns - 1:
					inputs.append(data_set[row][column])
			for i in range(num_nodes):
				the_neuron = n.neuron(inputs, end_of_num_layers_array, layerNumber, learning_rate)
				self.list_of_neurons.append(the_neuron)

		self.name_of_data_set = name_of_data_set
		self.results_of_run = []
		self.num_nodes = num_nodes
		self.str_results_of_run = []

	def run_neurons(self):
		for i in range(len(self.list_of_neurons)):
			result = self.list_of_neurons[i].run_neuron()
			if self.list_of_neurons[i].isOuterLayer == True:
				self.results_of_run.append(result)

	def max(self, results, num_results):
		biggest_number = results[0]
		for i in range(len(results)):
			if results[i] > biggest_number:
				biggest_number = results[i]
		location = 0
		for i in range(len(results)):
			if results[i] == biggest_number:
				location = i
		return location


	def generate_guesses(self):
		len_of_results = len(self.results_of_run)
		if (self.name_of_data_set == "Iris"):
			for i in range(0, len_of_results, 3):
				the_max = self.max(self.results_of_run[i:i+3], 3)
				guess = "0"
				if the_max == 0:
					guess = "0"
				elif the_max == 1:
					guess = "1"
				else:
					guess = "2"

				self.str_results_of_run.append(guess)

		elif (self.name_of_data_set == "Diabetes"):
			for i in range(0, len_of_results, 2):
				the_max = self.max(self.results_of_run[i:i+2], 2)
				guess = "0"
				if the_max == 0:
					guess = "0"
				else:
					guess = "1"

				self.str_results_of_run.append(guess)





	def print_results(self):
		print(self.name_of_data_set, " results:__________________")
		for i in range(len(self.str_results_of_run)):
			print(self.str_results_of_run[i])


	def print_accuracy(self, target_values):
		total_right = 0
		len_target_values = len(target_values)
		for i in range(len_target_values):
			temp_str = target_values[i]
			if temp_str == float(self.str_results_of_run[i]):
				total_right += 1
		accuracy = float(total_right) / float(len_target_values)
		print(accuracy)


	def update_weights(self, layer_left, layer_right):
		lNumNodes = layer_left.list_of_neurons
		rNumNodes = layer_right.list_of_neurons
		print(len(lNumNodes))
		print(len(rNumNodes))