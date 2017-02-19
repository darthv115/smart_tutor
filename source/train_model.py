
import mnist_loader
import network
import numpy as np
import cPickle as pickle

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = network.Network([784, 30, 10])

print "Training starting....."
# As of now, the test_data is passed as an arguement to figure out the accuracy of the model
# But at a later stage, we can only print the final accuracy of the model
net.SGD(training_data, 20,10,3.0, test_data)

with open('../assets/model/trained_model.pkl', 'wb') as output:
	trained_model = net
	pickle.dump(trained_model, output, pickle.HIGHEST_PROTOCOL)

del net