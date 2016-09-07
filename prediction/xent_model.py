import tensorflow as tf
import digit_mat_dataset as dmd

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.025, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')
def avg_pool_2x2(x):
    return tf.nn.avg_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')

def setup_variables():
    v = {}
    v['W_conv1'] = weight_variable([5, 5, 1, 32])
    v['b_conv1'] = bias_variable([32])
    v['W_conv2'] = weight_variable([3, 3, 32, 64])
    v['b_conv2'] = bias_variable([64])
    v['W_fc1'] = weight_variable([8*8*64, 25])
    v['b_fc1'] = bias_variable([25])
    v['W_fc2'] = weight_variable([25, 25])
    v['b_fc2'] = bias_variable([25])
    v['W_fc3'] = weight_variable([25, dmd.dim_y_normed])
    v['b_fc3'] = bias_variable([dmd.dim_y_normed])
    return v

def setup_model(x, v):
    m = {}
    m['x_image'] = tf.reshape(x, [-1, dmd.digit_mat_sz[0], dmd.digit_mat_sz[1], 1])
    m['h_conv1'] = tf.nn.relu(conv2d(m['x_image'], v['W_conv1']) + v['b_conv1'])
    m['h_pool1'] = avg_pool_2x2(m['h_conv1'])
    m['h_conv2'] = tf.nn.relu(conv2d(m['h_pool1'], v['W_conv2']) + v['b_conv2'])
    m['h_pool2'] = avg_pool_2x2(m['h_conv2'])
    m['h_pool2_flat'] = tf.reshape(m['h_pool2'], [-1, 8*8*64])
    m['h_fc1'] = tf.nn.relu(tf.matmul(m['h_pool2_flat'], v['W_fc1']) + v['b_fc1'])
    m['h_fc2'] = tf.nn.relu(tf.matmul(m['h_fc1'], v['W_fc2']) + v['b_fc2'])
    m['h_fc3'] = tf.reshape(tf.matmul(m['h_fc2'], v['W_fc3']) + v['b_fc3'], [-1, 1, dmd.dim_y_normed])
    m['y'] = tf.reduce_sum(m['h_fc3'], 1)
    return m

def setup_loss(x, y_, m):
    cross_entropy = tf.nn.softmax_cross_entropy_with_logits(m['y'], y_)
    l = tf.reduce_mean(cross_entropy)
    return l
