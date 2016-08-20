import tensorflow as tf
from scipy.io import loadmat
import numpy as np
import oeis_filter


cur_sample = 0

def next_batch(data, minibatch_size):
    global cur_sample
    X = np.zeros((minibatch_size,371))
    Y = np.zeros((minibatch_size,10))
    for i in np.arange(minibatch_size):
        # print(i)
        # print(data[cur_sample+i,30,0])
        if(cur_sample+i < len(data)):
            x_cur = data[cur_sample+i,:30,:].flatten()
            x_cur = np.append(x_cur,data[cur_sample+i,30,1:])
            X[i,:] = x_cur
            Y[i,data[cur_sample+i,30,0]] = 1
    cur_sample += minibatch_size

    return (X,Y)

def train(data, num_epochs = 100):
    train_size = int(len(data)*0.9)
    # print(train_size)

    sess = tf.InteractiveSession()
    x = tf.placeholder(tf.float32, shape=[None, 371])
    y_ = tf.placeholder(tf.float32, shape=[None, 10])

    W = tf.Variable(tf.zeros([371,10]))
    b = tf.Variable(tf.zeros([10]))
    y = tf.nn.softmax(tf.matmul(x, W) + b)

    sess.run(tf.initialize_all_variables())

    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

    train_step = tf.train.GradientDescentOptimizer(0.02).minimize(cross_entropy)

    # data_dict = loadmat(data_path)
    # data = data_dict['seq_digit_mats']
    train_data = data[:train_size,:,:]
    for it in range(num_epochs):
        train_data = np.random.permutation(train_data)
        global cur_sample
        cur_sample = 0
        num_minibatches = 100
        for i in range(num_minibatches):
            batch = next_batch(data,int(train_size/num_minibatches))
            # print(batch[0])
            if(i%10 == 0):
                # print(cross_entropy.eval(feed_dict={x: batch[0], y_: batch[1]}))
                print("------------")
                # print(W.eval())
                print("------------")
                print(b.eval())
                # print(y.eval(feed_dict={x: batch[0], y_: batch[1]}))
            train_step.run(feed_dict={x: batch[0], y_: batch[1]})


def load_data(data_path = "../data/digit_mats.mat"):
    data_dict = loadmat(data_path)
    data = oeis_filter.filter_short_digit_mats(data_dict['seq_digit_mats'])
    return data

if __name__ == "__main__":
    data = load_data(data_path = "../data/trivial_digit_mats.mat")
    type(data)
    train(data)
