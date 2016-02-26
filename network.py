import layer_of_neurons as ln
class network():
	def __init__(self, num_layers_array, num_rows, num_columns, data_set, name_of_data_set, learning_rate):
		self.num_layers_array = num_layers_array
		self.str_results = []
		len_num_layers_array = len(num_layers_array)
		self.layers = []
		#Go through each layer
		end_of_num_layers_array = False
		for num_nodes in range(len_num_layers_array): 
			if (num_nodes == len_num_layers_array - 1):
				end_of_num_layers_array = True
			else:
				end_of_num_layers_array = False

			if num_nodes == 0:
				temp_layer = ln.layer_of_neurons(num_rows, num_columns, data_set, name_of_data_set, self.num_layers_array[num_nodes], end_of_num_layers_array, num_nodes, learning_rate)
			else:
				results_of_last_layer = temp_layer.results_of_run
				temp_layer = ln.layer_of_neurons(num_rows, 1, results_of_last_layer, name_of_data_set, self.num_layers_array[num_nodes], end_of_num_layers_array, num_nodes, learning_rate)

			self.layers.append(temp_layer)

	def run_network(self):
		for layer in range(len(self.layers)):
			self.layers[layer].run_neurons()

	def print_layer_results(self):
		len_self_layers = len(self.layers)
		for layer in range(len_self_layers):
			if layer == len_self_layers - 1:
				self.layers[layer].print_results()

	def generate_guesses(self):
		for layer in self.layers:
			layer.generate_guesses()

	def print_accuracy(self, target_values):
		len_self_layers = len(self.layers)
		for layer in range(len_self_layers):
			if layer == len_self_layers - 1:
				self.layers[layer].print_accuracy(target_values)

	def update_weights(self):
		len_self_layers = len(self.layers)
		for num_layer in range(len_self_layers):
			if num_layer < len_self_layers - 1:
				self.layers[num_layer].update_weights(self.layers[num_layer - 1], self.layers[num_layer + 1])