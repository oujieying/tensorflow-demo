from __future__ import print_function
import tensorflow as tf
import os

welcome = tf.constant('Welcome to TensorFlow World!')

with tf.Session() as sess:
    print("output: ", sess.run(welcome))
    sess.close()

tf.app.flags.DEFINE_string('log_dir', os.path.dirname(os.path.abspath(__file__)) + '/logs',
                           'Directory where event logs are written to')
FLAGS = tf.app.flags.FLAGS

a = tf.constant(5.0, name="a")
b = tf.constant(10.0, name="b")

x = tf.add(a, b, name="add")
y = tf.div(a, b, name="div")

with tf.Session() as sess:
    writer = tf.summary.FileWriter(os.path.expanduser(FLAGS.log_dir), sess.graph)
    print("Output: ", sess.run([a, b, x, y]))
    #writer.close()
    #sess.close()
