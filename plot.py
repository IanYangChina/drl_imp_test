import json
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from copy import deepcopy as dcp
mpl.use('Agg')


def smoothed_plot(file, data, x_label="Timesteps", y_label="Success rate", window=5):
    N = len(data)
    running_avg = np.empty(N)
    for t in range(N):
        running_avg[t] = np.mean(data[max(0, t - window):(t + 1)])
    x = [i for i in range(N)]
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    if x_label == "Epoch":
        x_tick_interval = len(data) // 10
        plt.xticks([n * x_tick_interval for n in range(11)])
    plt.plot(x, running_avg)
    plt.savefig(file, bbox_inches='tight', dpi=500)
    plt.close()


def smoothed_plot_multi_line(file, data,
                             legend=None, legend_loc="upper right",
                             x_label='Timesteps', y_label="Success rate", window=5):
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    if x_label == "Epoch":
        x_tick_interval = len(data[0]) // 10
        plt.xticks([n * x_tick_interval for n in range(11)])

    for t in range(len(data)):
        N = len(data[t])
        x = [i for i in range(N)]
        if window != 0:
            running_avg = np.empty(N)
            for n in range(N):
                running_avg[n] = np.mean(data[t][max(0, n - window):(n + 1)])
        else:
            running_avg = data[t]

        plt.plot(x, running_avg)

    if legend is None:
        legend = [str(n) for n in range(len(data))]
    plt.legend(legend, loc=legend_loc)
    plt.savefig(file, bbox_inches='tight', dpi=500)
    plt.close()


def smoothed_plot_mean_deviation(file, data_dict_list, legend=None, title=None, file_formats='png', font_size=12,
                                 x_label='Timesteps', y_axis_off=False, y_label="Success rate", ylim=(None, None), window=5,
                                 legend_title=None, legend_loc='lower left', dot_marker_legend=False,
                                 legend_bbox_to_anchor=None, legend_ncol=4, legend_frame=False):
    plt.rcParams.update({'font.size': font_size})
    colors = ['tab:gray', 'tab:gray', 'tab:gray', 'tab:gray', 'tab:gray', 'tab:gray']
    linestyles = ['-', '--', '-.', ':']
    if y_axis_off:
        plt.ylabel(None)
        plt.yticks([])
    else:
        plt.ylabel(y_label)
    if ylim[0] is not None:
        plt.ylim(ylim)
    plt.xlabel(x_label)
    plt.title(title)
    if not isinstance(data_dict_list, list):
        data_dict_list = [data_dict_list]
    if x_label == "Epoch":
        x_tick_interval = len(data_dict_list[-1]["mean"]) // 5
        x_ticks = [n * x_tick_interval for n in range(11)]
        plt.xticks(x_ticks)

    for i in range(len(data_dict_list)):
        N = len(data_dict_list[i]["mean"])
        x = [i for i in range(N)]
        case_data = data_dict_list[i]
        for key in case_data:
            running_avg = np.empty(N)
            for n in range(N):
                running_avg[n] = np.mean(case_data[key][max(0, n - window):(n + 1)])

            case_data[key] = dcp(running_avg)

        plt.fill_between(x, case_data["upper"], case_data["lower"], alpha=0.3, color=colors[i], label='_nolegend_')
        plt.plot(x, case_data["mean"], color=colors[i], linestyle=linestyles[i])

    if dot_marker_legend:
        handles = [Line2D([0], [0], marker='o', markersize=10, color=colors[i], linestyle=linestyles[i]) for i in range(len(data_dict_list))]
        handlelength = 0.1
    else:
        handles = [Line2D([0], [0], color=colors[i], linestyle=linestyles[i]) for i in range(len(data_dict_list))]
        handlelength = 1

    if legend is not None:
        plt.legend(handles, legend, handlelength=handlelength,
                   title=legend_title, loc=legend_loc, labelspacing=0.15,
                   bbox_to_anchor=legend_bbox_to_anchor, ncol=legend_ncol, frameon=legend_frame)
    if type(file_formats) == list:
        for file_format in file_formats:
            plt.savefig(file+'.'+file_format, bbox_inches='tight', dpi=500, format=file_format)
    else:
        plt.savefig(file+'.'+file_formats, bbox_inches='tight', dpi=500, format=file_formats)
    plt.close()


def get_mean_and_deviation(data, save_data=False, file_name=None):
    upper = np.max(data, axis=0)
    lower = np.min(data, axis=0)
    mean = np.mean(data, axis=0)
    statistics = {"mean": mean.tolist(),
                  "upper": upper.tolist(),
                  "lower": lower.tolist()}
    if save_data:
        assert file_name is not None
        json.dump(statistics, open(file_name, 'w'))
    return statistics
