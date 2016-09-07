model_name = 'snapshots/xent_train'
data_dir = '../data/'

last_step = 4000000
load_step = 340000

save_max_to_keep = 1000
save_every = 20000
test_every = 1000
test_batch_sz = 1000
train_batch_sz = 100

learning_rate_starter = 5e-4
learning_rate_decay_every = 40000
learning_rate_decay_coeff = 0.9
momentum = 0.9
