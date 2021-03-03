import os
import plot
import pybullet_envs
from drl_implementation import SACDrQ

drq_params = {
    'image_crop_size': 140,
    'image_resize_size': 84,
    'frame_stack': 3,
    'prioritised': False,
    'memory_capacity': int(1e5),
    'actor_learning_rate': 0.001,
    'critic_learning_rate': 0.001,
    'update_interval': 1,
    'batch_size': 128,
    'optimization_steps': 1,
    'tau': 0.01,
    'discount_factor': 0.99,
    'discard_time_limit': False,

    'alpha': 0.1,
    'actor_update_interval': 2,
    'critic_target_update_interval': 2,
    'warmup_step': 1000,
    'q_regularisation_k': 2,

    'max_env_step': 200000,
    'testing_gap': 10000,
    'testing_episodes': 10,
    'saving_gap': 100000,

    'cuda_device_id': 1,
}

seeds = [11, 22]
seed_returns = []
path = os.path.dirname(os.path.realpath(__file__))
for seed in seeds:

    env = pybullet_envs.make("Walker2DBulletEnv-v0")
    # call render() before training to visualize (pybullet-gym-specific)
    # env.render()
    seed_path = path + '/seed'+str(seed)

    agent = SACDrQ(algo_params=drq_params, env=env, path=seed_path, seed=seed)
    agent.run(test=False)
    # the sleep argument pause the rendering for a while at every env step, useful for slowing down visualization
    # agent.run(test=True, load_network_ep=50, sleep=0.05)
    seed_returns.append(agent.statistic_dict['env_step_return'])
    del env, agent

return_statistic = plot.get_mean_and_deviation(seed_returns, save_data=True,
                                               file_name=os.path.join(path, 'return_statistic.json'))
plot.smoothed_plot_mean_deviation(path + '/returns.png', return_statistic, x_label='Episode', y_label='Average returns')
