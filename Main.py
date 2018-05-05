import tensorflow as tf
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# generation some house sizes between 1000 and 3500 (typical sq ft of house)

num_house = 160
np.random.seed(42)
house_size = np.random.randint(low=1000, high=3500, size=num_house)

# Generate house prices from house size with a random noise added.

np.random.seed(42)
house_price = house_size * 100.0 + np.random.randint(low=20000, high=70000, size=num_house)

#plot generated house and size

plt.plot(house_size, house_price, "bx") # bx - blue x
plt.ylabel("Price")
plt.xlabel("Size")
plt.show()

# you need to normalize values to event under

def normalize(array):
    return (array - array.mean()) / array.std()

# define number of trainning samples, 0.7 = 70%. We can take the first 70% since the values
# are randomized

num_train_samples = math.floor(num_house * 0.7)

#  define training data

train_house_size = np.asarray(house_size[:num_train_samples])
train_price = np.asanyarray(house_price[:num_train_samples:])

train_house_size_norm = normalize(train_house_size)
train_price_norm = normalize(train_price)

#set up the tensorflow placeholders that get updated as we descend down the gradient

tf_house_size = tf.placeholder("float", name="house_size")
tf_price = tf.placeholder("float", name="price")

# Define the variables holding the size_factor and price we set during training.
# Me initialize then to sone random values based on the normal distribution-
tf_size_factor = tf.variable(np.random.randn(), name="size_factor")
tf_price_offset = tf.variable(np.random.randn(), name="price_offset")

# 3. Define the Loss function (how much error) - Mean squared error
tf_cost = tf.reduce_sum(tf.pow(tf_price_pred-tf_price, 2))/(2*num_train_samples)

# Optimizer learning rate. The size of the steps down the gradient

learning_rate = 0.1

# 4. define a gradient descent optimize that will minimize the loss defined in the operation
# "cost".

optimize = tf.train.GradientDescentOptimizer(learning_rate).minimize(tf_cost)

# initializing the variables

init = tf.global_variables_initializer()

# launch the graph in the session

with tf.Session() as sess:
    sess.run(init)

    # set how often to display training progress and number of training iterations
    display_every = 2
    num_training_iter = 58

   # keep iterating the training data

    for iteration in range(num_training_iter):

        # fit all training data

            for (x, y) in zip(train_house_size_norm, train_price_norm):
                sess.run(optimize, feed_dict={tf_house_size: x, tf_price: y})

        # Display current status

            if (iteration + 1) % display_every == 0:
                c = sess.run(tf_cost, feed_dict={tf_house_size: train_house_size_norm, tf_price:train_price_norm})
                print("iteration #:", '%04d' % (iteration + 1), "cost=", "{:.9f", format(c), \)



