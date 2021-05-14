#tensorflow 약간

import tensorflow as tf
import numpy as np
def sigmoid(x):
    return 1 / (1 + np.math.exp(-x))

x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
y = np.array([[0], [1], [1], [1]])
w = tf.random.normal([2], 0, 1)
b = tf.random.normal([1], 0, 1)
for i in range(1000):
    for j in range(4):
        output = sigmoid(np.dot(x[j], w) + b)
        error = y[j] - output
        w = w + x[j] * 0.1 * error
        b = b + 0.1 * error
    if i % 100 == 99:
        print(i, error, w, output)

for j in range(4):
    print("{} => {}".format(x[j], sigmoid(np.dot(x[j], w) + b)))