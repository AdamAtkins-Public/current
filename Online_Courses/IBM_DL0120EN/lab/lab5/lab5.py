import os
#suppress dll loading messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import tensorflow_datasets
tf.compat.v1.enable_eager_execution()
import numpy
import matplotlib.pyplot as plt

print(tf.executing_eagerly())

"""
Lab5: Convolutional Neural Network in TensorFlow using MNIST dataset
"""

"""
Part1: Classify MNIST using a simple model
"""

#Load data
print('Loading MNIST dataset')
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(path='mnist.npz')

#x_ uint8 arrays grayscale images shapes(num_samples,28,28)
#y_ uint8 arrays of digit labels (0-9) with shapes (num_samples)
#preprocess the data 
#x_train = x_train.reshape(60000, 784).astype('float32') / 255
#x_test = x_test.reshape(10000, 784).astype('float32') / 255

#y_train = y_train.astype('float32')
#y_test = y_test.astype('float32')

##Attempting to convert the TFV2 dataset resulted in production of an inaccurate model
#part1 = tf.Graph()
#with part1.as_default():
#    #placeholders
#    x = tf.compat.v1.placeholder(tf.float32, shape=[None,784])
#    y_ = tf.compat.v1.placeholder(tf.float32, shape=[None,10])
#    #weights
#    W = tf.Variable(tf.zeros([784,10], tf.float32))
#    #bias
#    b = tf.Variable(tf.zeros([10], tf.float32))

#    init = tf.compat.v1.global_variables_initializer()

#    #operation to add weights and bias to inputs
#    add = tf.matmul(x, W) + b

#    #using Softmax for classification of inputs
#    y = tf.compat.v1.nn.softmax(add)

#    #Costfunction to estimate the difference with correct labels and output of NN
#    cross_entropy = tf.reduce_mean(-tf.compat.v1.reduce_sum(y_ * tf.compat.v1.log(y), reduction_indices=[1]))

#    #Optimize by using GradientDescent
#    train_step = tf.compat.v1.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#    #create tf.Dataset for batch operations
#    train_set = tf.data.Dataset.from_tensor_slices((x_train, y_train))

#    #convert y shape
#    def convert_y(y_int):
#        array = numpy.zeros(10, dtype=numpy.uint8)
#        array[y_int] = 1
#        return array

##Train using batchsizes
#sess = tf.compat.v1.InteractiveSession(graph=part1)
#sess.run(init)
#batch = train_set.batch(50)
#batch_np = list(tensorflow_datasets.as_numpy(batch))
#for i in range(len(batch_np)):
#    train_batch = batch_np[i]
#    train_x = list()
#    train_y = list()
#    for sample in range(len(train_batch[0])):
#        train_x.append(train_batch[0][sample].flatten())
#        train_y.append(convert_y(train_batch[1][sample]))
#    train_step.run(feed_dict={x:train_x, y_:train_y})
##check accuracy
#correct_prediction = tf.compat.v1.equal(tf.argmax(y),tf.argmax(y_))
#accuracy = tf.reduce_mean(tf.cast(correct_prediction, dtype=tf.float32))
#test_set = list(tensorflow_datasets.as_numpy(tf.data.Dataset.from_tensor_slices((x_test, y_test))))
#test_x, test_y = list(), list()
#for sample in range(len(test_set)):
#    test_x.append(test_set[sample][0].flatten())
#    test_y.append(convert_y(test_set[sample][1]))
#acc = accuracy.eval(feed_dict={x:test_x, y_:test_y})*100
#print("Accuracy of MNIST classification: {0}".format(acc))

#Training a CNN using MNIST dataset

#Normalize images
x_train, x_test = x_train / 255.0, x_test / 255.0

#Verify data
plt.figure(figsize=(10,10))
plt.title('MNIST data verification')
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap='gray')
    plt.xlabel(str(y_train[i]))
plt.show()

##Determine shape of data
#print(tf.shape(x_train[0]))
#print(tf.shape(y_train[0]))

#(28,28) image to label ()

#build model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Reshape(input_shape = (28, 28), target_shape=(28, 28, 1)))
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28,28,1)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(10))
model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=10, 
                    validation_data=(x_test, y_test))
#visualize training
plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')
plt.show()

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print('Model accuracy: \n{0}'.format(test_acc))
