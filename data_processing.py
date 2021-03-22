import os
import plot
import json
import pylab

path = os.getcwd()

env = 'Reach'
data = 'success_rate'

mujoco_ddpg = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_mujoco_gym', env, data+'_statistic.json')))
mujoco_ddpg_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_mujoco_gym', env+'_HER', data+'_statistic.json')))
bullet_ddpg = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', env, data+'_statistic.json')))
bullet_ddpg_her = json.load(open(os.path.join(path, 'exp_multi_goal', 'ddpg_pybullet_gym', env+'_HER', data+'_statistic.json')))

plot.smoothed_plot_mean_deviation(file=os.path.join(path, 'src', data+'_'+env),
                                  data_dict_list=[mujoco_ddpg, mujoco_ddpg_her, bullet_ddpg, bullet_ddpg_her],
                                  file_formats=['pdf'], font_size=22,
                                  ylim=(-0.05, 1.05),
                                  # legend=['Mujoco-DDPG',
                                  #         'Mujoco-DDPG-HER',
                                  #         'Bullet-DDPG',
                                  #         'Bullet-DDPG-HER'],
                                  # legend_title=env+' (4 seeds)',
                                  # legend_loc='lower left', legend_bbox_to_anchor=(0.1, 0.98), legend_ncol=2, legend_frame=False,
                                  window=5,
                                  x_label='Epoch', y_label='Average test success rates')

# fig = pylab.figure()
# figlegend = pylab.figure(figsize=(7, 0.15))
# ax = fig.add_subplot(111)
# lines = ax.plot(range(10), pylab.randn(10),
#                 range(10), pylab.randn(10),
#                 range(10), pylab.randn(10),
#                 range(10), pylab.randn(10))
# figlegend.legend(lines,
#                  ('Mujoco-DDPG',
#                   'Mujoco-DDPG-HER',
#                   'Bullet-DDPG',
#                   'Bullet-DDPG-HER'),
#                  'center', ncol=4, frameon=False)
# figlegend.savefig(path+'/src/single_step_task_legend.pdf', dpi=500)
