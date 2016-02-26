import numpy as np
import random
import math

class neuron():
	def __init__(self, inputs, outerlayer, layerNumber, learning_rate):
		self.isOuterLayer = outerlayer
		self.layerNumber = layerNumber
		self.result = 0
		inputs.append(-1)
		len_set_of_weighted_inputs = len(inputs)
		weights = []
		for i in range(len_set_of_weighted_inputs):
			weights.append(random.uniform(-1, 1))
		
		self.set_of_weighted_inputs = np.zeros(shape=(len_set_of_weighted_inputs,2))
		for i in range(len_set_of_weighted_inputs):
			self.set_of_weighted_inputs[i][0] = inputs[i]
			self.set_of_weighted_inputs[i][1] = weights[i]


		self.old_weights = []
		self.new_weights = []
		for i in range(len_set_of_weighted_inputs):
			self.old_weights.append(self.set_of_weighted_inputs[i][1])

		self.new_weights = self.old_weights



	def adder(self):
		total = 0
		for i in range(len(self.set_of_weighted_inputs)):
			total += self.set_of_weighted_inputs[i][0] * self.set_of_weighted_inputs[i][1]
		return total

	def activation(self, total):
		return (1 / (1 + math.exp(-total)))


	def run_neuron(self):
		total = self.adder()
		result = self.activation(total)
		self.result = result
		return result
