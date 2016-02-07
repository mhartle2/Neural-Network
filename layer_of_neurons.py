class layer_of_neurons():
	def __init__(self, num_neurons):
		self.list_of_neurons = []
		self.results_of_run = []

	def add_neuron(self, neuron_to_add):
		self.list_of_neurons.append(neuron_to_add)

	def run_neurons(self):
		for i in range(len(self.list_of_neurons)):
			result = self.list_of_neurons[i].run_neuron()
			self.results_of_run.append(result)

	def print_results(self):
		for i in range(len(self.results_of_run)):
			print(self.results_of_run[i])



