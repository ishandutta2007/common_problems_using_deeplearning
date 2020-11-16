import tensorflow as tf
from tensorflow import keras
import numpy as np
import add_numbers_data_creation as dc

print("dc.train_data:")
print(dc.train_data)
print("dc.train_targets:")
print(dc.train_targets)

model = keras.Sequential(
    [
        keras.layers.Flatten(input_shape=(2,)),
        keras.layers.Dense(20, activation=tf.nn.relu),
        keras.layers.Dense(20, activation=tf.nn.relu),
        keras.layers.Dense(1),
    ]
)

model.compile(optimizer="adam", loss="mse", metrics=["mae"])

model.fit(dc.train_data, dc.train_targets, epochs=50, batch_size=1)

test_loss, test_acc = model.evaluate(dc.test_data, dc.test_targets)
print("Test accuracy:", test_acc)
a = np.array([[2000, 2000], [5, 5], [15, 25], [2345, 4535], [24245, 5]])
print(model.predict(a))
