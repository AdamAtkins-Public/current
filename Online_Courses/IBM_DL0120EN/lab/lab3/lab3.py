
import os
#suppress dll messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
#disable eager execution to resolve compilation errors
tf.compat.v1.disable_eager_execution()
import pandas as pd
import numpy as np
import time
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

'''
Lab3: Logistic Regression with TensorFlow
'''

'''
LR is a probablistitic classification model: theta(y) = exp(y)/(1+exp(y))
    theta(y): logistic function; ex. a sigmoid curve
'''

'''
Part1: Iris dataset
'''

'''
Independent Variable: petal width, petal length, sepal width, sepal length
Dependent Variable: Iris setosa, Iris virginica, Iris versicolor
'''
#load data from sklearn dataset
iris = load_iris()
iris_X, iris_y = iris.data[:-1,:], iris.target[:-1]
iris_y= pd.get_dummies(iris_y).values
trainX, testX, trainY, testY = train_test_split(iris_X, iris_y, test_size=0.33, random_state=42)

# numFeatures is the number of features in our input data.
# In the iris dataset, this number is '4'.
numFeatures = trainX.shape[1]

# numLabels is the number of classes our data points can be in.
# In the iris dataset, this number is '3'.
numLabels = trainY.shape[1]

'''
Part2: LR Model
'''
#create placeholders to use during model training
# 'None' means TensorFlow shouldn't expect a fixed number in that dimension
X = tf.compat.v1.placeholder(tf.float32, [None, numFeatures]) # Iris has 4 features, so X is a tensor to hold our data.
yGold = tf.compat.v1.placeholder(tf.float32, [None, numLabels]) # This will be our correct answers matrix for 3 classes.

#set model weights and bias
#W = tf.Variable(tf.zeros([4, 3]))  # 4-dimensional input and  3 classes
#b = tf.Variable(tf.zeros([3])) # 3-dimensional output [0,0,1],[0,1,0],[1,0,0]

#Randomly sample from a normal distribution with standard deviation .01
weights = tf.Variable(tf.compat.v1.random_normal([numFeatures,numLabels],
                                                 mean=0,
                                                 stddev=0.01,
                                                 name="weights"))

bias = tf.Variable(tf.compat.v1.random_normal([1,numLabels],
                                              mean=0,
                                              stddev=0.01,
                                              name="bias"))

#explicitly define components of LR model: y_hat = sigmoid(WX + b)
apply_weights_OP = tf.matmul(X, weights, name="apply_weights")
add_bias_OP = tf.add(apply_weights_OP, bias, name="add_bias") 
activation_OP = tf.nn.sigmoid(add_bias_OP, name="activation")

'''
Part3: Training
'''
#Goal is to find best weight vector W by optimizing an error/cost mesure
#Least-Squares Linear Regression cannot be used; Gradient Decent will minimize loss function

#define training parameters
# Number of Epochs in our training
numEpochs = 700

# Defining our learning rate iterations (decay)
learningRate = tf.compat.v1.train.exponential_decay(learning_rate=0.0008,
                                                    global_step= 1,
                                                    decay_steps=trainX.shape[0],
                                                    decay_rate= 0.95,
                                                    staircase=True)

#cost function utilizes Squared Mean Error loss function
cost_OP = tf.nn.l2_loss(activation_OP-yGold, name="squared_error_cost")

#Defining our Gradient Descent
training_OP = tf.compat.v1.train.GradientDescentOptimizer(learningRate).minimize(cost_OP)

#Start session; course uses TF 1.X so eager execution not available
# Create a tensorflow session
sess = tf.compat.v1.Session()
# Initialize our weights and biases variables.
init_OP = tf.compat.v1.global_variables_initializer()
# Initialize all tensorflow variables
sess.run(init_OP)

#Operations to track model efficiency over time
# argmax(activation_OP, 1) returns the label with the most probability
# argmax(yGold, 1) is the correct label
correct_predictions_OP = tf.equal(tf.argmax(activation_OP,1),tf.argmax(yGold,1))
# If every false prediction is 0 and every true prediction is 1, the average returns us the accuracy
accuracy_OP = tf.reduce_mean(tf.cast(correct_predictions_OP, "float"))
# Summary op for regression output
activation_summary_OP = tf.compat.v1.summary.histogram("output", activation_OP)
# Summary op for accuracy
accuracy_summary_OP = tf.compat.v1.summary.scalar("accuracy", accuracy_OP)
# Summary op for cost
cost_summary_OP = tf.compat.v1.summary.scalar("cost", cost_OP)
# Summary ops to check how variables (W, b) are updating after each iteration
weightSummary = tf.compat.v1.summary.histogram("weights", weights.eval(session=sess))
biasSummary = tf.compat.v1.summary.histogram("biases", bias.eval(session=sess))
# Merge all summaries
merged = tf.compat.v1.summary.merge([activation_summary_OP, accuracy_summary_OP, cost_summary_OP, weightSummary, biasSummary])
# Summary writer
writer = tf.compat.v1.summary.FileWriter("summary_logs", sess.graph)

#Perform training
# Initialize reporting variables
cost = 0
diff = 1
epoch_values = []
accuracy_values = []
cost_values = []

# Training epochs
for i in range(numEpochs):
    if i > 1 and diff < .0001:
        print("change in cost %g; convergence."%diff)
        break
    else:
        # Run training step
        step = sess.run(training_OP, feed_dict={X: trainX, yGold: trainY})
        # Report occasional stats
        if i % 10 == 0:
            # Add epoch to epoch_values
            epoch_values.append(i)
            # Generate accuracy stats on test data
            train_accuracy, newCost = sess.run([accuracy_OP, cost_OP], feed_dict={X: trainX, yGold: trainY})
            # Add accuracy to live graphing variable
            accuracy_values.append(train_accuracy)
            # Add cost to live graphing variable
            cost_values.append(newCost)
            # Re-assign values for variables
            diff = abs(newCost - cost)
            cost = newCost

            #generate print statements
            print("step %d, training accuracy %g, cost %g, change in cost %g"%(i, train_accuracy, newCost, diff))

# How well do we perform on held-out test data?
print("final accuracy on test set: %s" %str(sess.run(accuracy_OP, 
                                                     feed_dict={X: testX, 
                                                                yGold: testY})))

