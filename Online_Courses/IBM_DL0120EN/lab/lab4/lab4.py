
import numpy

"""
Understanding Convolution Neural Networks
"""

"""
Part1.a: 1d operation with Python
"""

#Let h represent an image and x the kernel
h = [2, 1, 0]
x = [3, 4, 5]

y = numpy.convolve(x, h)
#verify y[n] = sum_(k -> -inf to inf) (x[k] * h[n - k]) [discrete convolution]
conv_h = str()
for i in range(len(h)+len(x)-1): conv_h += y[i].__str__() + " "
print("1d convolution of image h = [2, 1, 0] and kernel x = [3, 4, 5]:\n{0}".format(conv_h))

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
print("Convolution of image h = [1, 2, 5, 4] and kernel x = [6, 2] with 'full' padding:\n{0}".format(conv_h))

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
print("Convolution of image h = [1, 2, 5, 4] and kernel x = [6, 2] with 'same' padding:\n{0}".format(conv_h))

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
print("Convolution of image h = [1, 2, 5, 4] and kernel x = [6, 2] with 'valid' padding:\n{0}".format(conv_h))
