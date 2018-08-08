from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.datasets import mnist
from keras.utils import np_utils
import time

import matplotlib.pyplot as plt
import numpy

batch_size = 128
nb_classes = 10
nb_epoch = 100

# Load MNIST dataset
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
Y_Train = np_utils.to_categorical(y_train, nb_classes)
Y_Test = np_utils.to_categorical(y_test, nb_classes)

# Multilayer Perceptron model
model = Sequential()
model.add(Dense(output_dim=625, input_dim=784, init='normal', activation='linear'))
model.add(Dense(output_dim=625, input_dim=625, init='normal', activation='linear'))
model.add(Dense(output_dim=10, input_dim=625, init='normal', activation='softmax'))
model.compile(optimizer=SGD(lr=0.05), loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train
start = time.time()
history = model.fit(X_train, Y_Train, validation_split=0.33, nb_epoch=nb_epoch, batch_size=batch_size, verbose=2)
end = time.time()
print ("Time to build model %.1f seconds" % (end - start,) )

# Evaluate
evaluation = model.evaluate(X_test, Y_Test, verbose=2)
print('Summary: Loss over the test dataset: %.4f, Accuracy: %.4f' % (evaluation[0], evaluation[1]))

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
