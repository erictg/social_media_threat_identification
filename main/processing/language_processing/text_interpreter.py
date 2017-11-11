import tensorflow as tf

batch_size = 2
num_steps = 3
ltsm_size = 1


words = tf.placeholder(tf.int32, [batch_size, num_steps])

#ltsm = rnn_cell
