import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # Shush runtime warnings
import tensorflow as tf
import numpy as np

# First, create a tensorflow constant
const = tf.constant(2.0, name="const")

# Create tensorflow variables
b = tf.Variable(2.0, name='b')
c = tf.Variable(1.0, name='c')

# Now create some opreations
d = tf.add(b, c, name='d')
e = tf.add(c, const, name='e')
a = tf.multiply(d, e, name='a')

# Set up the variable initialization
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
	#Initialize the variables
	sess.run(init_op)
	#a_out = sess.run(a)
	b = tf.placeholder(tf.float32, [None, 1], name='b')
	a_out = sess.run(a, feed_dict={b:np.arange(0,10)[:,np.newaxis]})
	print("Variable a is {}".format(a_out))

