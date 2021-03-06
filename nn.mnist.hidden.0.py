
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD
from keras.datasets import mnist
from keras.utils import np_utils
import keras
import time



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



# Logistic regression model   - no hidden layers
model = Sequential()
model.add(Dense(units=10, input_shape=(784,), activation='softmax', kernel_initializer='normal'))
model.compile(optimizer=SGD(lr=0.05), loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()


start = time.time()
history = model.fit(X_train, Y_Train, epochs=nb_epoch, batch_size=batch_size, verbose=2)


# Evaluate
end = time.time()
print ("Time to build model %.1f seconds" % (end - start,) )
evaluation = model.evaluate(X_test, Y_Test, verbose=2)
print('Summary: Loss over the test dataset: %.2f, Accuracy: %.2f' % (evaluation[0], evaluation[1]))

