import os
import plot
import json
import pybullet_multigoal_gym as pmg
from drl_implementation import GoalConditionedDDPG
algo_params = {
    'hindsight': True,
    'her_sampling_strategy': 'future',
    'prioritised': False,
    'memory_capacity': int(1e6),
    'actor_learning_rate': 0.001,
    'critic_learning_rate': 0.001,
    'Q_weight_decay': 0.0,
    'update_interval': 1,
    'batch_size': 128,
    'optimization_steps': 40,
    'tau': 0.05,
    'discount_factor': 0.98,
    'clip_value': 50,
    'discard_time_limit': True,
    'terminate_on_achieve': False,
    'observation_normalization': True,

    'random_action_chance': 0.2,
    'noise_deviation': 0.05,

    'training_epochs': 101,
    'training_cycles': 50,
    'training_episodes': 16,
    'testing_gap': 1,
    'testing_episodes': 30,
    'saving_gap': 50,
}
seeds = [11, 22, 33, 44]
seed_returns = []
seed_success_rates = []
path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(path, 'Joint_Reach_HER')

for seed in seeds:

    env = pmg.make_env(task='reach',
                       gripper='parallel_jaw',
                       joint_control=True,
                       render=True,
                       binary_reward=True,
                       max_episode_steps=50,
                       image_observation=False,
                       depth_image=False,
                       goal_image=False)

    seed_path = path + '/seed'+str(seed)

    agent = GoalConditionedDDPG(algo_params=algo_params, env=env, path=seed_path, seed=seed)
    agent.run(test=False)
    # agent.run(test=True, load_network_ep=100, sleep=0.05)
    seed_returns.append(agent.statistic_dict['epoch_test_return'])
    seed_success_rates.append(agent.statistic_dict['epoch_test_success_rate'])
    del env, agent

return_statistic = plot.get_mean_and_deviation(seed_returns, save_data=True,
                                               file_name=os.path.join(path, 'return_statistic.json'))
plot.smoothed_plot_mean_deviation(path + '/returns', return_statistic, x_label='Epoch', y_label='Average returns')


success_rate_statistic = plot.get_mean_and_deviation(seed_success_rates, save_data=True,
                                                     file_name=os.path.join(path, 'success_rate_statistic.json'))
plot.smoothed_plot_mean_deviation(path + '/success_rates', success_rate_statistic,
                                  x_label='Epoch', y_label='Success rates')
