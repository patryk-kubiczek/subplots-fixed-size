from matplotlib import pyplot as plt
from subplots_fixed_size import subplots

import yaml

conf = yaml.safe_load(open("conf.yaml"))

plt.style.use(conf['plot_style'])

# Example 1: default settings
fig, axes = subplots()
ax = axes.flat[0]

ax.plot([1, 2, 3])
ax.set_xlabel("X label")
ax.set_ylabel("Y label")

fig.savefig("plot.png")

# Example 2: 3 plots in a row
fig, axes = subplots(ncols=3, wsize=2.3, hsize=2.3, wspace=0.6 + 0.2)
ax1, ax2, ax3 = axes.flat

ax1.plot([1, 2, 3])
ax2.plot([10, 50, 90])
ax3.plot([111, 112, 113])
for ax in axes.flat:
    ax.set_xlabel("X label")
    ax.set_ylabel("Y label")

fig.savefig("plot3.png")

# Example 3: plot with legend
fig, axes = subplots(rightspace = 0.2 + 1.2)
ax = axes.flat[0]

ax.plot([1, 2, 3], label="Variable A")
ax.plot([4, 5, 6], label="Variable B")
ax.set_xlabel("X label")
ax.set_ylabel("Y label")

ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)

fig.savefig("plot_with_legend.png")
