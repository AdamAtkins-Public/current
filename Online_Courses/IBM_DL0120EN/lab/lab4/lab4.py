
import os
import numpy
from scipy import signal
#suppress dll loading messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
import requests
from io import BytesIO
from PIL import Image
import matplotlib
import matplotlib.pyplot as plt

"""
Understanding Convolution Neural Networks
"""

"""
Part1.a: 1d operation with Python
"""
print('Part 1\n')
#Let h represent an image and x the kernel
h = [2, 1, 0]
x = [3, 4, 5]

y = numpy.convolve(x, h)
#verify y[n] = sum_(k -> -inf to inf) (x[k] * h[n - k]) [discrete convolution]
conv_h = str()
for i in range(len(h)+len(x)-1): conv_h += y[i].__str__() + " "
print("1d convolution of image h = [2, 1, 0] and kernel x = [3, 4, 5]:\n{0}\n".format(conv_h))

"""
Part1.b: Convolution with 'full' padding
"""

#Let h represent an image and x the kernel
x = [6, 2]
h = [1, 2, 5, 4]

y = numpy.convolve(x, h, 'full')

#The convolution includes zero padding around the image 0 [1, 2, 5, 4] 0
conv_h = str()
for i in range(len(h)+len(x)-1): conv_h += y[i].__str__() + " "
print("Convolution of image h = [1, 2, 5, 4] and kernel x = [6, 2] with 'full' padding:\n{0}\n".format(conv_h))

"""
Part1.c: Convolution with 'same' padding
"""

#Let h represent an image and x the kernel
x = [6, 2]
h = [1, 2, 5, 4]

y = numpy.convolve(x, h, 'same')

#Convolution is identical to 'full' with the exception that it returns
# a result that is of dimension max(x,h)
conv_h = str()
for i in range(max(len(x),len(h))): conv_h += y[i].__str__() + " "
print("Convolution of image h = [1, 2, 5, 4] and kernel x = [6, 2] with 'same' padding:\n{0}\n".format(conv_h))

"""
Part1.d: Convolution with 'valid' padding
"""

#Let h represent an image and x the kernel
x = [6, 2]
h = [1, 2, 5, 4]

y = numpy.convolve(x, h, 'valid')

#Convolution does not include zero padding and reduces the dimensions of output
conv_h = str()
for i in range(max(len(x),len(h))-min(len(x),len(y))+1): conv_h += y[i].__str__() + " "
print("Convolution of image h = [1, 2, 5, 4] and kernel x = [6, 2] with 'valid' padding:\n{0}\n".format(conv_h))

"""
Part2: Convolution 2d operation with Python/Numpy
"""
print('\n\nPart 2\n')
#2d Convolution defined as I'=sum_u,v( I(x-u, y-v)g(u,v) )

I = [[255, 7, 3],
     [212, 240, 4],
     [218, 216, 230]]

g = [[-1,1]]

#Convolution of image I and kernel g
print('Convolution of image {0} with kernel {1} without zero padding:'.format(I, g))
print('{0}\n'.format(signal.convolve(I, g, 'valid')))

print('Convolution of image {0} with kernel {1} with zero padding:'.format(I, g))
print('{0}\n'.format(signal.convolve(I, g)))

#increasing the dimension of the kernel g
g = [[-1, 1],
     [2, 3]]

#Convolution using the newly defined kernel
print('Convolution of image {0} with kernel {1} without zero padding:'.format(I, g))
print('{0}\n'.format(signal.convolve(I, g, 'valid')))

print('Convolution of image {0} with kernel {1} with zero padding:'.format(I, g))
print('{0}\n'.format(signal.convolve(I, g)))

print('Convolution of image {0} with kernel {1}with same zero padding:'.format(I, g))
print('{0}\n'.format(signal.convolve(I, g, 'same')))

"""
Part3: Convolution of images with TensorFlow
"""

print('\n\nPart3\n')

#let filter be a 4d tensor: [width, height, channels, number of filters]
#let input represent and image 4d tensor: [batch size, height, width, number of channels]
lab4_part3 = tf.compat.v1.Graph()
with lab4_part3.as_default():

    filter = tf.Variable(tf.compat.v1.random_normal([3,3,1,1])) 
    input = tf.Variable(tf.compat.v1.random_normal([1,10,10,1])) 

    op = tf.compat.v1.nn.conv2d(input, filter, strides=[1,1,1,1], padding='VALID')
    op2 = tf.compat.v1.nn.conv2d(input, filter, strides=[1,1,1,1], padding='SAME')

    init = tf.compat.v1.global_variables_initializer()

with tf.compat.v1.Session(graph=lab4_part3) as sess:
    sess.run(init)

    print('Image input:\n\n{0}\n'.format(input.eval()))
    print('Filter/Kernel:\n\n{0}\n'.format(filter.eval()))
    result = sess.run(op)
    print('\nConvolution of image without zero padding:\n\n{0}\n'.format(result))
    result = sess.run(op2)
    print('\nConvolution of image with zero padding:\n\n{0}\n'.format(result))


"""
Part4: Convolution applied to images
"""

print('\n\nPart4\n')

"""
Part4.a: Edge detection on a bird image
"""

#Load image from URL
image_url = 'https://www.sciencemag.org/sites/default/files/styles/article_main_large/public/bird_16x9_3.jpg?itok=PjlMM1pn'
image_data = requests.get(image_url).content

#Load image data
image = Image.open(BytesIO(image_data))

#Convert image to black and white
image_gr = image.convert("L")

#Convert image to array of 0 to 255 uint8
image_arr = numpy.asarray(image_gr)

#plot image
image_plot = plt.imshow(image_arr)
image_plot.set_cmap('gray')
plt.title('Grayscale Bird Image')
plt.show(block=image_plot)

#Define an edge detector kernel
kernel = numpy.array([[0,1,0],
                      [1,-4,1],
                      [0,1,0]])

grad = signal.convolve2d(image_arr, kernel, mode='same', boundary='symm')

#plot convolution
fig, aux = plt.subplots(figsize=(10, 10))
aux.imshow(numpy.absolute(grad), cmap='gray')
plt.title('Edge Detection Convolution')
plt.show(block=fig)

#Note: CNNs automatically modify kernel to determine features that best describe data

#When dealing with CNNs pixels are generally converted to values between 0 to 1
# in a process called 'Normalization'

grad_biases = numpy.absolute(grad) + 100
grad_biases[grad_biases > 255] = 255

fig, aux = plt.subplots(figsize=(10, 10))
aux.imshow(numpy.absolute(grad_biases), cmap='gray')
plt.title('Gradient Magnitude Convolution')
plt.show(block=fig)

"""
Part4.b: Edge detection on a digit image
"""

#load image
image_url = 'https://ibm.box.com/shared/static/vvm1b63uvuxq88vbw9znpwu5ol380mco.jpg'
image_data = requests.get(image_url).content
image = Image.open(BytesIO(image_data))
image_gr = image.convert('L')
image_arr = numpy.array(image_gr)

#plot source image
fig, aux = plt.subplots(figsize=(10, 10))
image_plot = plt.imshow(image_arr)
image_plot.set_cmap('gray')
plt.title('Original Digit Image')
plt.show(block=image_plot)

#convolve using edge detection kernel
grad = signal.convolve2d(image_arr, kernel, mode='same', boundary='symm')

#plot convolution
fig, aux = plt.subplots(figsize=(10, 10))
aux.imshow(numpy.absolute(grad), cmap='gray')
plt.title('Edge Detection of Digit Image')
plt.show(block=fig)
