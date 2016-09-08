model_name = 'snapshots/xent_train'

seed = 12345
train_ratio = 0.9

last_step = 50000
load_step = None

save_max_to_keep = 1000
save_every = 2000
test_every = 100
test_batch_sz = 200
train_batch_sz = 50

learning_rate_starter = 5e-4
learning_rate_decay_every = 4000
learning_rate_decay_coeff = 0.9
momentum = 0.9
