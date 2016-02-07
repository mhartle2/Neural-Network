import neuron as n
class layer_of_neurons():
	def __init__(self, num_rows, num_columns, data_set, name_of_data_set):
		self.list_of_neurons = []
		for row in range(num_rows):
			inputs = []
			for column in range(num_columns):
				if column != num_columns - 1:
					inputs.append(data_set[row][column])
			the_neuron = n.neuron(inputs)
			self.list_of_neurons.append(the_neuron)

		self.name_of_data_set = name_of_data_set
		self.results_of_run = []

	def run_neurons(self):
		for i in range(len(self.list_of_neurons)):
			result = self.list_of_neurons[i].run_neuron()
			self.results_of_run.append(result)

	def print_results(self):
		print(self.name_of_data_set, " results:__________________")
		for i in range(len(self.results_of_run)):
			print(self.results_of_run[i])



