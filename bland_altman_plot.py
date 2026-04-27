"""
This code generates a Bland-Altman plot which is a method of data plotting used in analyzing the 
agreement between two different measurements. The plot uses systolic blood pressure measurements 
from the arm and finger for demonstration. The appearance of the plot is customized and the final 
figure is saved.
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# suppress pandas warning
pd.options.mode.chained_assignment = None


def generate_bland_altman(data1, data2, ax_var, color_input):
    """   
    Generates a Bland-Altman plot for two sets of data.
    """
    mean = np.mean([data1, data2], axis=0)
    diff = data1 - data2  # difference between data1 and data2
    md = np.mean(diff)  # mean of the difference
    sd = np.std(diff, axis=0)  # standard deviation of the difference
    ci_low = md - 1.96 * sd
    ci_high = md + 1.96 * sd
    ax_var.scatter(mean, diff, color=color_input, s=50)
    ax_var.axhline(md, color='black', linestyle='-', linewidth=2)
    ax_var.axhline(md + 1.96 * sd, color='black', linestyle='--', linewidth=2)
    ax_var.axhline(md - 1.96 * sd, color='black', linestyle='--', linewidth=2)
    return diff, md, sd, ci_low, ci_high


def generate_plot(measure1,
                  measure2,
                  x_range_array,
                  independent_variable_label=None,
                  dependent_variable_label=None,
                  specified_colors='mediumblue',
                  super_title=None):
    """
    Calls function to generate a Bland-Altman plot for two sets of measurements and provides 
    customized aesthetics.
    """

    sns.set(style="whitegrid", font_scale=1.6)

    with plt.rc_context({'axes.edgecolor': 'black'}):

        fig, ax = plt.subplots(figsize=(8, 6))

        # bland altman plot
        diff, md, sd, ci_low, ci_high = generate_bland_altman(measure1,
                                                              measure2,
                                                              ax,
                                                              specified_colors)

        ax.axhline(y=0, color='black', linestyle=':', linewidth=2)

        ax.set(ylim=(md - 3.5 * sd, md + 3.5 * sd))
        x_out_plot = x_range_array[0] + (x_range_array[1] - x_range_array[0]) * 1.2
        ax.text(x_out_plot, md - 1.96 * sd,
                f"-1.96 SD\n{ci_low:.0f}",
                ha="center", va="center", color='black')
        ax.text(x_out_plot, md + 1.96 * sd,
                f"+1.96 SD\n{ci_high:.0f}",
                ha="center", va="center", color='black')
        ax.text(x_out_plot, md,
                f"mean\n{md:.0f}",
                ha="center", va="center", color='black')

        # set x range
        ax.set(xlim=(x_range_array[0], x_range_array[1]))

        # set y range
        ax.set(ylim=(diff.min() - 0.5 * sd, diff.max() + 0.5 * sd))

        # set x and y labels
        if independent_variable_label is not None:
            ax.set_xlabel(independent_variable_label)
        if dependent_variable_label is not None:
            ax.set_ylabel(dependent_variable_label)

        # alter axis line size
        # change all spines
        for axis in ['top', 'bottom', 'right', 'left']:
            ax.spines[axis].set_linewidth(2)

        # specify ticks
        ax.set_xticks(np.linspace(x_range_array[0], x_range_array[1], num=5).tolist())
        ax.tick_params(axis='both', colors='black')

        # set the color of the axis labels
        ax.xaxis.label.set_color('black')
        ax.yaxis.label.set_color('black')

        # remove grid lines
        ax.grid(False)

        # adjust subplots spacing
        # if subplots are added, can include, for e.g., 'wspace=0.4, hspace=0.4'
        # to control padding between subplots
        plt.subplots_adjust(bottom=0.3, top=0.8, left=0.25, right=0.7)

        # add global title
        if super_title is not None:
            fig.suptitle(super_title, fontsize="large", color="k")


if __name__ == '__main__':

    # --- read data ---
    EXAMPLE_DATA_PATH = r'.\systolic blood pressure.csv'
    example_data_df = pd.read_csv(EXAMPLE_DATA_PATH)

    # --- variables setup ---
    m1_array = example_data_df.iloc[:, 0].to_numpy()
    m2_array = example_data_df.iloc[:, 1].to_numpy()

    # --- plot data ---
    generate_plot(m1_array,
                  m2_array,
                  [50, 250],
                  independent_variable_label=r'Arm systolic pressure $\mathregular{[mmHg]}$',
                  dependent_variable_label=r'Finger systolic pressure $\mathregular{[mmHg]}$',
                  specified_colors='cornflowerblue')

    # save figure
    FILE_DESTINATION = r'.\figure'
    plt.savefig(os.path.join(FILE_DESTINATION + '.pdf').replace("\\", "/"), format="pdf")
    plt.savefig(os.path.join(FILE_DESTINATION + '.png').replace("\\", "/"), dpi=300)
    plt.close()
