import os
import plot
import json

path = os.getcwd()

env = 'PickAndPlace'

mujoco_ddpg = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_mujoco_gym', env, 'success_rate_statistic.json')))
mujoco_ddpg_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_mujoco_gym', env+'_HER', 'success_rate_statistic.json')))
bullet_ddpg = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', env, 'success_rate_statistic.json')))
bullet_ddpg_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', env+'_HER', 'success_rate_statistic.json')))

plot.smoothed_plot_mean_deviation(file=os.path.join(path, 'src', 'success_rate_'+env),
                                  data_dict_list=[mujoco_ddpg, mujoco_ddpg_her, bullet_ddpg, bullet_ddpg_her],
                                  file_formats=[
                                      'pdf',
                                      'png'
                                  ],
                                  ylim=(-0.05, 1.05),
                                  legend=['Mujoco-DDPG',
                                          'Mujoco-DDPG-HER',
                                          'Bullet-DDPG',
                                          'Bullet-DDPG-HER'],
                                  legend_title=env+' (4 seeds)',
                                  legend_loc='lower left', legend_bbox_to_anchor=(0.1, 0.98), legend_ncol=2, legend_frame=False,
                                  window=5,
                                  x_label='Epoch', y_label='Average test returns')
