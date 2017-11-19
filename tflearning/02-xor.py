import tflearn
from numpy import array

# preprocess data
data_input = array([[1,1],[1,0],[0,1],[0, 0]])
data_output = array([[0],[1],[1],[0]])

print(data_input.shape)
print(data_output.shape)

# build NN
tnorm = tflearn.initializations.uniform(minval=-1.0, maxval=1.0)
net = tflearn.input_data(shape=[None, 2])
net = tflearn.fully_connected(net, 2, activation='sigmoid',  weights_init=tnorm)
net = tflearn.fully_connected(net, 1, activation='sigmoid',  weights_init=tnorm)
net = tflearn.regression(net, optimizer='sgd', learning_rate=2., loss='mean_square')

# train
model = tflearn.DNN(net)
model.fit(data_input, data_output, n_epoch=1000)

# predict
pred = model.predict([[0, 1]])
print(pred)

pred = model.predict([[1, 1]])
print(pred)
