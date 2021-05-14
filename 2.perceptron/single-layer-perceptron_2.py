import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import Dense, InputLayer
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.activations import sigmoid
from tensorflow.keras.losses import BinaryCrossentropy
gpu_devices = tf.config.experimental.list_physical_devices('GPU')
for device in gpu_devices:
    tf.config.experimental.set_memory_growth(device, True)

x = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
y = np.array([[0], [1], [1], [1]])

model = Sequential()
model.add(InputLayer(input_shape=(2, )))
model.add(Dense(units = 1, activation=sigmoid))
print(model.summary())

model.compile(optimizer=SGD(learning_rate= 0.1), loss=BinaryCrossentropy())
history = model.fit(x, y, epochs=1000)
print("{} => {}".format(x, model.predict(x)))
plt.plot(history.history['loss'], label='train loss')
plt.show()