import numpy as np
import random

train_data = np.array([[1.0, 1.0]])
train_targets = np.array([2.0])
for i in range(3, 10000, 2):
    s = random.randint(i, 3 * i)
    i2 = s - i
    train_data = np.append(train_data, [[i, i2]], axis=0)
    train_targets = np.append(train_targets, [s])

print("train_data")
print(train_data)
print("train_targets")
print(train_targets)

test_data = np.array([[2.0, 2.0]])
test_targets = np.array([4.0])
for i in range(4, 8000, 4):
    s = random.randint(i, 2 * i)
    i2 = s - i
    test_data = np.append(test_data, [[i, i2]], axis=0)
    test_targets = np.append(test_targets, [s])

print("test_data")
print(test_data)
print("test_targets")
print(test_targets)
