import os
import plot
import json

path = os.getcwd()

return_ddpg = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', 'Reach', 'success_rate_statistic.json')))
return_ddpg_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', 'Reach_PHER', 'success_rate_statistic.json')))
return_sac = json.load(open(os.path.join(path, 'exp_multi_goal', 'sac_pybullet_gym', 'Reach', 'success_rate_statistic.json')))
return_sac_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'sac_pybullet_gym', 'Reach_PHER', 'success_rate_statistic.json')))

plot.smoothed_plot_mean_deviation(file=os.path.join(path, 'src', 'returns_pybullet_kuka_reach'),
                                  data_dict_list=[return_ddpg, return_ddpg_her, return_sac, return_sac_her],
                                  file_formats=['pdf', 'png'],
                                  legend=['DDPG', 'DDPG-HER', 'SAC', 'SAC-HER'],
                                  legend_title='Pybullet Kuka Reach (4 seeds)',
                                  legend_loc='lower left', legend_bbox_to_anchor=(0, 0.98), legend_ncol=4, legend_frame=False,
                                  window=0,
                                  x_label='Epoch', y_label='Average test returns')
