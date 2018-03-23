import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2' # Shush runtime warnings
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# Python optimization variables 
learning_rate = 0.0001
epochs = 10
batch_size = 50

#declare the training data placeholders
# input x - for 28 x 28 pixels = 784 - this is a flattened image 
# that is drawn from mnist.train.nextbatch() 

x = tf.placeholder(tf.float32, [None, 784])
# dynamically reshape the input
x_shaped = tf.reshape(x, [-1, 28, 28, 1])
# now declare the output data placeholder - 10 digits
y = tf.placeholder(tf.float32, [None, 10])


def create_new_conv_layer(input_data, num_input_channels, num_filters, filter_shape, pool_shape, name):
	#Set up the filter input shape for the tf.nn.conv_2d
	conv_filt_shape = [filter_shape[0], filter_shape[1], num_input_channels, num_filters]

	# Initialize weights and bias for the filter 
	weights = tf.Variable(tf.truncated_normal(conv_filt_shape, stddev=0.03), name=name+'_W')
	bias = tf.Variable(tf.truncated_normal([num_filters]), name=name+'_b')

	# setup the convolutional layer operation
	out_layer = tf.nn.conv2d(input_data, weights, [1, 1, 1, 1], padding='SAME')

	# add the bias
	out_layer += bias
	# apply a RELU non-linear activation
	out_layer = tf.nn.relu(out_layer)

	# now perform max pooling
	ksize = [1, pool_shape[0], pool_shape[1], 1]
	strides = [1, 2, 2, 1]
	out_layer = tf.nn.max_pool(out_layer, ksize=ksize, strides=strides, padding='SAME')

	return out_layer

layer1 = create_new_conv_layer(x_shaped, 1, 32, [5,5], [2,2], name='layer1')
layer2 = create_new_conv_layer(layer1, 32, 64, [5,5], [2,2], name='layer2')

flattened = tf.reshape(layer2, [-1, 7*7*64])

wd1 = tf.Variable(tf.truncated_normal([7*7*64, 1000], stddev=0.3), name='wd1')
bd1 = tf.Variable(tf.truncated_normal([1000], stddev=0.01), name='bd1')
dense_layer1 = tf.matmul(flattened, wd1) + bd1
dense_layer1 = tf.nn.relu(dense_layer1)

wd2 = tf.Variable(tf.truncated_normal([1000, 10], stddev=0.3), name='wd2')
bd2 = tf.Variable(tf.truncated_normal([10], stddev=0.01), name='bd2')
dense_layer2 = tf.matmul(dense_layer1, wd2) + bd2
y_ = tf.nn.softmax(dense_layer2)

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=dense_layer2, labels=y))

# -----------------------------------
# Training the CNN using mini-batches
# Steps:
# - Create an optimizer
# - Create correct prediction and accuracy evaluation operations
# - Initialize the operations
# - Determine the number of batch runs within a training epoch
# - For each point:
#   + For each batch:
#     ~ Extract the batch data
#	  ~ Run the optimizer and cross-entropy operations
#     ~ Add to the average cost
#   + Calculate the current test accuracy
#   + Print out some results
# - Calculate the final test accuracy and print

# Add the optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cross_entropy)

# Define an accuracy assessment operation
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax	(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# Setup the initialisation operator
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
	# initialize the variables
	sess.run(init_op)
	total_batch = int(len(mnist.train.labels)/batch_size)
	for epoch in range(epochs):
			avg_cost = 0
			for i in range(total_batch):
				batch_x, batch_y = mnist.train.next_batch(batch_size = batch_size)
				_,c = sess.run([optimizer, cross_entropy],
								feed_dict={x:batch_x, y:batch_y})
				avg_cost += c / total_batch
			test_acc = sess.run(accuracy, feed_dict	= {x:mnist.test.images, y:mnist.test.labels	})
			print("Epoch: ", (epoch + 1), "cost =", "{:,.3f}".format(avg_cost), "test accuracy	=", "{:,.3f}".format(test_acc))
	print("\nTraining completed!")
	print(sess.run(accuracy, feed_dict	= {x:mnist.test.images, y:mnist.test.labels	}))



