from numpy import exp, array, random, dot
from inspect import getmembers
from pprint import pprint


#Models a layer of a neuronal network
class NNLayer():
  def __init__(self, inputs):
    self.weights = 2 * random.random((inputs,1)) - 1


#Models a neuronal network
class NN():

  def __init__(self, layers, inputs):
    #initialize class members
    self.inputs = []
    self.layers = []
    for x in xrange(layers):
      self.layers.append(NNLayer(inputs))
    self.outputs = []

    #Seed  the random number generator, so it generates the same numbers
    # every time the program runs
    random.seed(1)

  #sigmoid
  def __sigmoid(self, x):
    return 1 / (1 + exp(-x))

  #gradient of the sigmoid curve
  def __sigmoid_derivative(self, x):
    return x * (1-x)

  #trains the neural network
  def train(self, training_set_inputs, training_set_outputs, number_of_training_iterations):
    for iteration in xrange(number_of_training_iterations):

      #predict on the training set
      output = self.predict(training_set_inputs)

      #calculates the error
      error = training_set_outputs - output

      #adjust weights layer by layer
      for l in reversed(self.layers):
        #multiply the error by input and again by the gradient of the sigmoid curve
        adjustment = dot(training_set_inputs.T, error * self.__sigmoid_derivative(output))

        #adjust the weights of layer l
        l.weights += adjustment


  #predicts an outputgvgv
  def predict(self, inputs):
    prediction = []
    for l in self.layers:
      prediction = self.__sigmoid(dot(inputs, l.weights))
    
    return prediction


#main program
if __name__ == '__main__':

  #creates a new neuronal network
  nn = NN(layers=1, inputs=3)
  
  #training set
  training_set_inputs = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
  training_set_outputs = array([[0,1,1,0]]).T

  #training
  nn.train(training_set_inputs, training_set_outputs, 100)

  #predicts a non trained value
  print(nn.predict(array([1,0,0])))
  
  #debug
  #pprint(nn.layers[0].weights)