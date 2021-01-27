l = [0, 1, 2, 3]
del l[0]
l.append(4)
print(l)
exit()

import gym
import matplotlib.pyplot as plt
env = gym.make("BreakoutNoFrameskip-v4")
obs = env.reset()
for i in range(30):
    env.render()
    frame, _, _, _ = env.step(0)
for _ in range(30):
    env.render()
    a = env.action_space.sample()
    frame, _, _, _ = env.step(a)
    plt.imshow(frame)
    plt.pause(0.000001)
exit()
import numpy as np
import random
print(np.arange(46, 50))
print(random.sample(np.arange(46, 50).tolist(), 4))
exit()
import plot
from agent.utils.exploration_strategy import OUNoise, GaussianNoise

ex = GaussianNoise(action_dim=1, mu=0.0, sigma=0.05)
n = []
for i in range(10):
    noises = []
    for t in range(1000):
        noises.append(ex())
    n.append(noises)

data = plot.get_mean_and_deviation(n)
plot.smoothed_plot_mean_deviation('noises.png', data, y_label='noise')
