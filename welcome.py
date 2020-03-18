from __future__ import print_function
import tensorflow as tf
import os

welcome = tf.constant('Welcome to TensorFlow World!')

with tf.Session() as sess:
    print("output: ", sess.run(welcome))
    sess.close()

