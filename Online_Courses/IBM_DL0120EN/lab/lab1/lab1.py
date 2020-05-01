
import os
#suppress dll messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf

'''
lab1 of online course IBM DL0120EN
'''

'''
Part 1: TensorFlow introduction
'''
print("Lab1: Part1\n")
#TensorFlow uses a graph computational model
graph1 = tf.Graph()

#tf.Operation() are nodes, and tf.Tensor() are edges, in the graph
with graph1.as_default():
    a = tf.constant([2], name='a_constant')
    b = tf.constant([3], name='b_constant')

#printing value of a
sess = tf.compat.v1.Session(graph=graph1)
result = sess.run(a)
print(result)
sess.close()

#define function node
with graph1.as_default():
    c = tf.add(a, b)

sess = tf.compat.v1.Session(graph=graph1)
result = sess.run(c)
print(result)
sess.close()

#using with block to close Session automatically
with tf.compat.v1.Session(graph=graph1) as sess:
    result = sess.run(c)
    print(result)

'''
Part 2: Defining multidimensional arrays in TensorFlow
'''
print("\nLab1: Part2\n")
graph2 = tf.Graph()
with graph2.as_default():
    Scalar = tf.constant(2)
    Vector = tf.constant([5,6,2])
    Matrix = tf.constant([[1,2,3], [2,3,4], [3,4,5]])
    Tensor = tf.constant([[[1,2,3],[2,3,4],[3,4,5]],[[4,5,6],[5,6,7],[6,7,8]],[[7,8,9],[8,9,10],[9,10,11]]])
with tf.compat.v1.Session(graph=graph2) as sess:
    result = sess.run(Scalar)
    print("Scalar (1 entry):\n %s \n"%result)
    result = sess.run(Vector)
    print("Vector (3 entries):\n %s \n"%result)
    result = sess.run(Matrix)
    print("Matrix (3x3 entries):\n %s \n"%result)
    result = sess.run(Tensor)
    print("Tensor (3x3x3 entries):\n %s \n"%result)

#tf.shape returns the shape of the data structure
    print(tf.shape(Scalar))
    print(tf.shape(Vector))
    print(tf.shape(Matrix))
    print(tf.shape(Tensor))

print('\nMatrix addition:\n')
graph3 = tf.Graph()
with graph3.as_default():
    Matrix1 = tf.constant([[1,2,3],[2,3,4],[3,4,5]])
    Matrix2 = tf.constant([[2,2,2],[2,2,2],[2,2,2]])

    add_op1 = tf.add(Matrix1, Matrix2)
    add_op2 = Matrix1 + Matrix2

with tf.compat.v1.Session(graph=graph3) as sess:
    result = sess.run(add_op1)
    print('Result of TF add op:\n %s \n'%result)
    result = sess.run(add_op2)
    print('Result of Python add op:\n %s \n'%result)

print('\nMatrix multiplication:\n')
graph4 = tf.Graph()
with graph4.as_default():
    Matrix1 = tf.constant([[2,3],[3,4]])
    Matrix2 = tf.constant([[1,2],[2,3]])

    matrix_mul = tf.matmul(Matrix1, Matrix2)

with tf.compat.v1.Session(graph=graph4) as sess:
    result = sess.run(matrix_mul)
    print('Result of TF.matmul():\n %s \n'%result)

'''
Part 3: Variables
'''

#variables can be updated through successive session runs
#Must be initialized at runtime using: tf.global_variables_initializer()

print("\nLab1: Part3\n")

#A simple Counter, increments at each update
graph5 = tf.Graph()
with graph5.as_default():
    v = tf.Variable(0)

    update = tf.compat.v1.assign(v, v+1)
    init_op = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session(graph=graph5) as sess:
    print('\nVariable Counter output:\n')
    sess.run(init_op)
    for _ in range(4):
        print(sess.run(v))
        sess.run(update)

'''
Part 4: Placeholders
'''

#pass data to the model; predefined typed memory cells
print("\nLab1: Part4\n")

graph6 = tf.Graph()
with graph6.as_default():
    #declare placeholder
    a = tf.compat.v1.placeholder(tf.float32)
    #basic op
    b = a * 2

with tf.compat.v1.Session(graph=graph6) as sess:
    print('Simple Placeholder example:\n')
    result = sess.run(b,feed_dict={a:3.5})
    print(result)

dictionary = {a:[[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]]]}

with tf.compat.v1.Session(graph=graph6) as sess:
    print('\nExpanded dictionary Placeholder example:\n')
    result = sess.run(b,feed_dict=dictionary)
    print(result)
