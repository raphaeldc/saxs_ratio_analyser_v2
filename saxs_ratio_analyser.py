import matplotlib.pyplot as plt
from crystal_lattice import *

def saxs_plot_log(files, struc, first_peak, trace_color, begin=0, end=0, graph=True):
    files = np.array(files)
    if graph==True:
        for i in range(len(files)):
            data = np.genfromtxt(files[i], skip_header=begin, skip_footer=end, usecols=(0,1), names=['q','I'])
            plt.plot(data['q'], np.log10(data['I'])-i, "-", lw=1)
        if struc in ratios:
            for index in ratios[struc]:
                plt.axvline(x=first_peak * index, ls='-.', color=trace_color, lw=0.5)
        plt.xlabel('q [nm^(-1)]')
        plt.ylabel('log(I) [a.u.]')
        plt.yticks([])
        plt.show()
        print(2*np.pi*crystals[struc][0]/first_peak)
    else:
        return

saxs_plot_log(['ra_10LA_1_norm_minus_agua_7_norm.dat'], 'Pn3m', 1.3, 'k', begin=20, end=100, graph=True)
saxs_plot_log(['ra_10LH_1_norm_minus_agua_7_norm.dat'], 'Fd3m', 0.91, 'r', begin=20, end=100, graph=True)