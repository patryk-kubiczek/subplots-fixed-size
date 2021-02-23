import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import Divider, Size
from mpl_toolkits.axes_grid1.mpl_axes import Axes

import numpy as np

def subplots(nrows=1, ncols=1,
             wsize=3.2, hsize=2.3,
             leftspace=0.6, wspace=0.6, rightspace=0.2,
             bottomspace=0.5, hspace=0.5, topspace=0.2):

    figsize = (leftspace + ncols * wsize + (ncols - 1) * wspace + rightspace,
               bottomspace + nrows * hsize + (nrows - 1) * hspace + topspace)

    dpi = mpl.rcParams['savefig.dpi']
    figsize_px = tuple(int(inch * dpi) for inch in figsize)
    print(f"{ncols} x {nrows} axes array, figsize = ({figsize[0]:.2f}, {figsize[1]:.2f}) in = {figsize_px} px, dpi = {dpi}")

    fig = plt.figure(figsize=figsize)

    h = [Size.Fixed(leftspace)] + [Size.Fixed(wsize), Size.Fixed(wspace)] * ncols
    h[-1] = Size.Fixed(rightspace)
    v = [Size.Fixed(bottomspace)] + [Size.Fixed(hsize), Size.Fixed(hspace)] * nrows
    v[-1] = Size.Fixed(topspace)

    divider = Divider(fig, (0, 0, 1, 1), h, v, aspect=False)
    axarr = np.empty((nrows, ncols), dtype=object)
    for nrow in range(nrows):
        for ncol in range(ncols):
            ax = Axes(fig, divider.get_position())
            ax.set_axes_locator(divider.new_locator(nx=2*ncol+1, ny=2*nrow+1))
            axarr[nrow, ncol] = fig.add_axes(ax)
    return fig, axarr
