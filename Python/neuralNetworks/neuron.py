import matplotlib.pylab as plt
import numpy as np

# A single Logistic neuron
x = np.arange(-8,8,0.1)
f = 1 / (1 + np.exp(-x))
plt.plot(x,f)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# Introducing weights
w1 = 0.5
w2 = 1.0
w3 = 3.0
l1 = 'w = 0.5'
l2 = 'w = 1.0'
l3 = 'w = 3.0'
for w, l in [(w1, l1), (w2, l2), (w3,l3)]:
	f = 1 / (1 + np.exp(-x*w))
	plt.plot(x,f,label=l)
plt.xlabel('x')
plt.ylabel('h_w(x)')
plt.legend(loc=2)
plt.show()

# Introducing different biases to a single weight
w = 5.0
b1 = -8.0
b2 = 0.0
b3 = 8.0
l1 = 'b1 = -8.0'
l2 = 'b2 = 0.0'
l3 = 'b3 = 8.0'
for b, l in [(b1, l1), (b2, l2), (b3, l3)]:
	f = 1 / (1+ np.exp(-x*w + b))
	plt.plot(x, f, label=l)


plt.xlabel('x')
plt.ylabel('h_wb(x)')
plt.legend(loc=2)
plt.show()