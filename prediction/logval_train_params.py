model_name = 'snapshots/logval_train'

seed = 12345
train_ratio = 0.9

last_step = 500000
load_step = None

save_max_to_keep = 1000
save_every = 10000
test_every = 1000
test_batch_sz = 500
train_batch_sz = 100

learning_rate_starter = 5e-4
learning_rate_decay_every = 40000
learning_rate_decay_coeff = 0.9
momentum = 0.9
