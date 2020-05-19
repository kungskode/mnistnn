import numpy as np

# get data, convert to matrix and transpose for easier usage
mnist_data = np.transpose(np.genfromtxt("./data/mnist_test.csv", delimiter=','))

# split matrix to input set and label set
labels = mnist_data[0,:]
inputs = mnist_data[1:,:]

# initialize parameters
W1 = np.random.randn(64,784)
b1 = np.zeros((64,1))
W2 = np.random.rand(64,64)
b2 = np.zeros((64,1))
W3 = np.random.rand(10,64)
b3 = np.zeros((10,1))

