import os
import plot
import json

path = os.getcwd()

mujoco_ddpg = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_mujoco_gym', 'Reach', 'success_rate_statistic.json')))
mujoco_ddpg_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_mujoco_gym', 'Reach_HER', 'success_rate_statistic.json')))
# bullet_ddpg = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', 'Reach', 'success_rate_statistic.json')))
bullet_ddpg_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', 'Reach_HER', 'success_rate_statistic.json')))

plot.smoothed_plot_mean_deviation(file=os.path.join(path, 'src', 'success_rate_reach'),
                                  data_dict_list=[mujoco_ddpg, mujoco_ddpg_her, bullet_ddpg_her],
                                  file_formats=['pdf', 'png'],
                                  legend=['Mujoco-DDPG',
                                          'Mujoco-DDPG-HER',
                                          # 'Bullet-DDPG',
                                          'Bullet-DDPG-HER'],
                                  legend_title='Reach (4 seeds)',
                                  legend_loc='lower left', legend_bbox_to_anchor=(0, 0.98), legend_ncol=4, legend_frame=False,
                                  window=0,
                                  x_label='Epoch', y_label='Average test returns')
