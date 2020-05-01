
import os
#suppress dll messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
#Disable TFv2
tf.compat.v1.disable_v2_behavior()
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
import tensorflow as tf
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10, 6)

'''
Lab2: Linear Regression with TensorFlow
'''

'''
Part1: Simple Linear Regression Model
'''

#Y=aX+b; where Y is dependent variable and X is independent

#Define X
X = np.arange(0.0, 5.0, 0.1)

#Set slope and intercept
a = 1
b = 0

#LR Model
Y = a * X + b
plt.plot(X,Y)
plt.title('Simple Linear Regression Model')
plt.ylabel('Dependent variable')
plt.xlabel('Independent variable')
plt.show()

'''
Part2: Linear Regression Model using car emission data
'''

'''
The following data set is ratings and estimated Carbon dioxide emissions for vehicles
'''

#Download data
#!wget -O FuelConsumption.csv https:/o/s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/ML0101ENv3/labs/FuelConsumptionCo2.csv

#Load data
data_file = pd.read_csv("Online_Courses\\IBM_DL0120EN\\lab\\data\\FuelConsumption.csv")
print(data_file.head())

#Use LR to predict C02 emissions based on Engine Size
train_y = np.asanyarray(data_file[['CO2EMISSIONS']])
train_x = np.asanyarray(data_file[['ENGINESIZE']]) 

#Let slope a and intercept b be a random guess
a = tf.Variable(20.0)
b = tf.Variable(30.2)
#define model
y = a * train_x + b

#define loss function to minimize
#tf.reduce_mean() finds the mean of a multidimensional tensor (result can be different shape)
loss = tf.compat.v1.reduce_mean(tf.compat.v1.square(y - train_y))

#use simple gradient decent as an optimizer
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.05)

#set optimizer to minimize loss function
train = optimizer.minimize(loss)

#initialize session
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

#Run graph
loss_values = []
train_data = []
print('\nStep\tLoss\ta_val\tb_val')
for step in range(100):
    _, loss_val, a_val, b_val = sess.run([train, loss, a, b])
    loss_values.append(loss_val)
    if step % 5 == 0:
        print('{: <7}\t{: <7}\t{: <7}\t{: <7}'.format(step, loss_val, a_val, b_val))
        train_data.append([a_val, b_val])

#Plot of loss values
plt.plot(loss_values, 'ro')
plt.show()

#Visualization on how a and b change overtime
cr, cg, cb = (1.0, 1.0, 0.0)
for f in train_data:
    cb += 1.0 / len(train_data)
    cg -= 1.0 / len(train_data)
    if cb > 1.0: cb = 1.0
    if cg < 0.0: cg = 0.0
    [a, b] = f
    f_y = np.vectorize(lambda x: a*x + b)(train_x)
    line = plt.plot(train_x, f_y)
    plt.setp(line, color=(cr,cg,cb))
plt.plot(train_x, train_y, 'ro')
green_line = mpatches.Patch(color='red', label='Data Points')
plt.legend(handles=[green_line])
plt.xlabel('Engine size')
plt.ylabel('CO2 emissions')
plt.title('LR Model fit over steps%5')
plt.show()
