import tensorflow as tf
import logval_dataset as lvd

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.025, shape=shape)
    return tf.Variable(initial)

def setup_variables():
    v = {}
    v['W_fc1'] = weight_variable([lvd.dim_x, 10])
    v['b_fc1'] = bias_variable([10])
    v['W_fc2'] = weight_variable([10, 10])
    v['b_fc2'] = bias_variable([10])
    v['W_fc3'] = weight_variable([10, lvd.dim_y])
    v['b_fc3'] = bias_variable([lvd.dim_y])
    v['keep_prob'] = tf.placeholder(tf.float32, name='keep_prob')
    return v

def setup_model(x, v):
    m = {}
    m['h_fc1'] = tf.nn.relu(tf.matmul(x, v['W_fc1']) + v['b_fc1'])
    m['h_fc2'] = tf.nn.relu(tf.matmul(m['h_fc1'], v['W_fc2']) + v['b_fc2'])
    m['h_fc2_dropout'] = tf.nn.dropout(m['h_fc2'], v['keep_prob'])
    m['y'] = tf.matmul(m['h_fc2_dropout'], v['W_fc3']) + v['b_fc3']
    return m

def setup_loss(x, y_, m):
    mse = tf.reduce_mean(tf.square(m['y'] - y_))
    return mse
