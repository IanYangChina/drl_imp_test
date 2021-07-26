import os
import plot
import json
import pylab
from matplotlib.lines import Line2D

path = os.getcwd()

# env = 'Reach'
# data = 'success_rate'
#
# mujoco_ddpg = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_mujoco_gym', env, data+'_statistic.json')))
# mujoco_ddpg_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_mujoco_gym', env+'_HER', data+'_statistic.json')))
# bullet_ddpg = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', env, data+'_statistic.json')))
# bullet_ddpg_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', env+'_HER', data+'_statistic.json')))
#
# plot.smoothed_plot_mean_deviation(file=os.path.join(path, 'src', data+'_'+env),
#                                   data_dict_list=[mujoco_ddpg, mujoco_ddpg_her, bullet_ddpg, bullet_ddpg_her],
#                                   file_formats=['pdf'], font_size=22,
#                                   ylim=(-0.05, 1.05),
#                                   y_axis_off=False,
#                                   window=5,
#                                   x_label='Epoch', y_label='Average test success rates')

env = 'JointControl'
data = 'success_rate'

J_reach = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', 'Joint_Reach_HER', data+'_statistic.json')))
J_push = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', 'Joint_Push_HER', data+'_statistic.json')))
J_pick_and_place = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', 'Joint_PickAndPlace_HER', data+'_statistic.json')))
J_slide = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', 'Joint_Slide_HER', data+'_statistic.json')))

plot.smoothed_plot_mean_deviation(file=os.path.join(path, 'src', env),
                                  data_dict_list=[J_reach, J_push, J_pick_and_place, J_slide],
                                  file_formats=['pdf'], font_size=22,
                                  legend=['Reach', 'Push', 'PickAndPlace', 'Slide'],
                                  legend_ncol=2,
                                  legend_loc='upper left', legend_bbox_to_anchor=(-0.1, 1.3),
                                  ylim=(-0.05, 1.05),
                                  y_axis_off=False,
                                  window=5,
                                  x_label='Epoch', y_label='Average test success rates')

# fig = pylab.figure()
# figlegend = pylab.figure(figsize=(6.8, 0.2))
# ax = fig.add_subplot(111)
# lines = ax.plot(range(10), pylab.randn(10),
#                 range(10), pylab.randn(10),
#                 range(10), pylab.randn(10),
#                 range(10), pylab.randn(10))
# colors = ['tab:gray', 'tab:gray', 'tab:gray', 'tab:gray', 'tab:gray', 'tab:gray']
# linestyles = ['-', '--', '-.', ':']
# handles = [Line2D([0], [0], color=colors[i], linestyle=linestyles[i]) for i in range(4)]
# figlegend.legend(handles,
#                  ('Mujoco-DDPG',
#                   'Mujoco-DDPG-HER',
#                   'Bullet-DDPG',
#                   'Bullet-DDPG-HER'),
#                  'center', handlelength=2, ncol=4, frameon=False)
# figlegend.savefig(path+'/src/single_step_task_legend.pdf', dpi=500)

# env = 'BlockStack'
# data = 'success_rate'
#
# d1 = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_multi_step', env+'_2', data+'_statistic.json')))
# d2 = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_multi_step', env+'_2_crcl', data+'_statistic.json')))
# d3 = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_multi_step', env+'_3_crcl', data+'_statistic.json')))
# d4 = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_multi_step', env+'_4_crcl', data+'_statistic.json')))
#
# plot.smoothed_plot_mean_deviation(file=os.path.join(path, 'src', data+'_'+env),
#                                   data_dict_list=[d1, d2, d3, d4],
#                                   file_formats=['pdf'], font_size=20,
#                                   # title=env,
#                                   ylim=(-0.05, 1.05),
#                                   # y_axis_off=True,
#                                   legend=['2 block (50 epo)',
#                                           '2 block crcl (50 epo)',
#                                           '3 block crcl (100 epo)',
#                                           '4 block crcl (150 epo)'],
#                                   # legend_title=env+' (4 seeds)',
#                                   legend_loc='upper right',
#                                   dot_marker_legend=False,
#                                   # legend_bbox_to_anchor=(0.1, 0.98),
#                                   legend_ncol=1, legend_frame=False,
#                                   window=5,
#                                   x_label='Epoch', y_label='Average test success rates')
