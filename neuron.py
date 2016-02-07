import numpy as np
import random

class neuron():
	def __init__(self, inputs):
		inputs.append(-1)
		len_set_of_weighted_inputs = len(inputs)
		weights = []
		for i in range(len_set_of_weighted_inputs):
			weights.append(random.uniform(-1, 1))
		
		self.set_of_weighted_inputs = np.zeros(shape=(len_set_of_weighted_inputs,2))
		for i in range(len_set_of_weighted_inputs):
			self.set_of_weighted_inputs[i][0] = inputs[i]
			self.set_of_weighted_inputs[i][1] = weights[i]

	def adder(self):
		total = 0
		for i in range(len(self.set_of_weighted_inputs)):
			total += self.set_of_weighted_inputs[i][0] * self.set_of_weighted_inputs[i][1]
		return total

	def activation(self, total):
		threshold = 0
		if total > threshold:
			return 1
		else:
			return 0		

	def run_neuron(self):
		total = self.adder()
		result = self.activation(total)
		return result
