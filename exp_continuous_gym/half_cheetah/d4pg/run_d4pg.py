import os
from drl_implementation import D4PG

algo_params = {
    'prioritised': True,
    'memory_capacity': int(1e6),
    'actor_learning_rate': 0.001,
    'critic_learning_rate': 0.001,
    'Q_weight_decay': 0.0,
    'update_interval': 1,
    'batch_size': 256,
    'optimization_steps': 1,
    'tau': 0.005,
    'discount_factor': 0.99,
    'discard_time_limit': False,
    'warmup_step': 2500,
    'observation_normalization': False,
    'num_atoms': 51,
    'value_max': 50,
    'value_min': -50,
    'reward_scaling': 0.1,

    'num_workers': 4,
    'learner_steps': int(1e6),
    'learner_upload_gap': int(1e3),  # in optimization steps
    'worker_update_gap': 3,  # in episodes
    'replay_queue_size': 64,
    'priority_queue_size': 64,
    'batch_queue_size': 10,

    'training_episodes': 101,
    'testing_gap': 10,
    'testing_episodes': 10,
    'saving_gap': 50,
}
seeds = [11]
path = os.path.dirname(os.path.realpath(__file__))
for seed in seeds:
    seed_path = path + '/seed'+str(seed)
    agent = D4PG(algo_params,
                 env_name="HalfCheetahBulletEnv-v0",
                 env_source="pybullet_envs",
                 path=seed_path,
                 seed=10)
    agent.run()
    del agent
