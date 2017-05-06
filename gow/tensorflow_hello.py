import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf

task =  tf.constant("Hello Gowtham")

sess = tf.Session()

print(sess.run(task))