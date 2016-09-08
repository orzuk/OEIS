import os
import time
import math
import numpy as np
import tensorflow as tf
import xent_model
import oeis_io as oio
import oeis_filter as oif
import digit_mat_dataset as dmd
from xent_train_params import *

np.random.seed(seed)

# load digit_mats as a training and test set
oeis_dir = os.path.dirname(os.path.dirname(os.path.realpath('__file__')))
digit_mats_fn = os.path.join(oeis_dir, 'data', 'digit_mats')
digit_mats = oio.read_seq_digit_mats(digit_mats_fn)
digit_mats = oif.filter_short_digit_mats(digit_mats)
train, test = dmd.init_sets(digit_mats, train_ratio)

sess = tf.InteractiveSession()
x = tf.placeholder(tf.float32, shape=[None, dmd.dim_x])
y_ = tf.placeholder(tf.float32, shape=[None, dmd.dim_y])
v = xent_model.setup_variables()
m = xent_model.setup_model(x, v)
l = xent_model.setup_loss(x, y_, m)

saver = tf.train.Saver(max_to_keep=save_max_to_keep)
global_step = tf.Variable(0, trainable=False)
learning_rate = tf.train.exponential_decay(learning_rate_starter, global_step,
                                           learning_rate_decay_every,
                                           learning_rate_decay_coeff, staircase=True)
train_step = tf.train.MomentumOptimizer(learning_rate, momentum).minimize(l, global_step=global_step)
sess.run(tf.initialize_all_variables())

if load_step:
    restore_model = model_name + '-' + str(load_step)
    saver.restore(sess, restore_model)

t = time.time()
first_step = load_step if load_step else 0
for step in range(first_step, last_step+1):
    if (step+1) % save_every == 0:
        saver.save(sess, model_name, global_step=step+1)
    if (step+1) % test_every == 0:
        batch_train = train.next_batch(test_batch_sz)
        batch_test = test.next_batch(test_batch_sz)
        l_train = l.eval(feed_dict={x: batch_train['x'], y_: batch_train['y']})
        l_test = l.eval(feed_dict={x: batch_test['x'], y_: batch_test['y']})
        print("step %d, training loss %g, test loss %g, delta-time %g secs" % \
            (step+1, l_train, l_test, time.time() - t))
        t = time.time()
    batch_train = train.next_batch(train_batch_sz)
    train_step.run(feed_dict={x: batch_train['x'], y_: batch_train['y']})
