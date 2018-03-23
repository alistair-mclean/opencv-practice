import numpy as np 
w1 = np.array([[0.2, 0.2, 0.2], [0.4, 0.4, 0.4], [0.6, 0.6, 0.6]])
w2 = np.zeros((1,3))
w2[0,:] = np.array([0.5, 0.5, 0.5])


b1 = np.array([0.8, 0.8, 0.8])
b2 = np.array([0.2])

# Define the activation function
def f(x):
	return 1 / (1 + np.exp(-x))

# Simple output calculation of a feed forward neural network
# UNVECTORIZED AND INEFFICIENT - SEE BELOW FOR VECTORIZED AND EFFICIENT METHOD
def simple_looped_nn_calc(n_layers, x, w, b):
	for l in range(n_layers-1):
		# Setup the input array which the weights will be multiplied by for each l
		# If it's the first layer, the input array will be the x input vector
		# If it's not the first layer, the input to the next layer will be the output 
		#of the previous one.
		if l == 0:
			node_in = x
		else:
			node_in = h
		# Setup the output array for the nodes in layer l + 1
		h = np.zeros((w[l].shape[0],))
		# Loop through the rows of the weight array
		for i in range(w[l].shape[0]):
			f_sum = 0

			for j in range(w[l].shape[1]):
				f_sum += w[l][i][j] * node_in[j]
			# Add the bias
			f_sum += b[l][i]
			# Finally, use the activation function to calculate the i-th output i.e. h1, h2, h3
			h[i] = f(f_sum)
	return h

# Increases the efficiency by 500 fold 
def matrix_feed_forward(n_layers, x, w, b)
	for l in range(n_layers-1)
		if l == 0:
			node_in = x
		else:
			node_in = h
		z = w[l].dot(node_in) + b[l]
		h = f(z)
	return h

w = [w1, w2]
b = [b1, b2]
x = [1.5, 2.0, 3.0]
H1 = simple_looped_nn_calc(3, x, w, b)
print(H1)
H2 = matrix_feed_forward(3, x, w, b)
print(H2)