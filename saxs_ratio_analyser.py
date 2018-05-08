import numpy as np
import matplotlib.pyplot as plt

def saxs_plot_log(files, begin, end, struc,first_peak):
    crystals = {
        'Im3m': [np.sqrt(2 / 2), np.sqrt(4 / 2), np.sqrt(6 / 2), np.sqrt(8 / 2), np.sqrt(10 / 2), np.sqrt(12 / 2),
                 np.sqrt(14 / 2)],
        'Pn3m': [np.sqrt(2 / 2), np.sqrt(3 / 2), np.sqrt(4 / 2), np.sqrt(6 / 2), np.sqrt(8 / 2), np.sqrt(9 / 2),
                 np.sqrt(10 / 2)]}
    for i in range(len(files)):
        data = np.genfromtxt(files[i], skip_header=begin, skip_footer=end, usecols=(0,1), names=['q','I'])
        plt.plot(data['q'], np.log10(data['I'])-i, "-", lw=1)
    if struc in crystals:
        for index in crystals[struc]:
            plt.axvline(x=first_peak * index, ls='-.', color='red', lw=0.5)
    plt.xlabel('q [nm^(-1)]')
    plt.ylabel('log(I) [a.u.]')
    plt.yticks([])
    plt.show()

saxs_plot_log(['ra_10LA_1_norm_minus_agua_7_norm.dat','ra_10LH_1_norm_minus_agua_7_norm.dat'],20,100,'Pn3m',1.3)
