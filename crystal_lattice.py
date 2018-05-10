# Cubic structures
import numpy as np

lines = np.array(['c','m','y','k','r','g','b'])

ratios = {
            'Im3m': np.array([np.sqrt(2 / 2), np.sqrt(4 / 2), np.sqrt(6 / 2), np.sqrt(8 / 2), np.sqrt(10 / 2), np.sqrt(12 / 2),
                     np.sqrt(14 / 2)]),
            'Pn3m': np.array([np.sqrt(2 / 2), np.sqrt(3 / 2), np.sqrt(4 / 2), np.sqrt(6 / 2), np.sqrt(8 / 2), np.sqrt(9 / 2),
                     np.sqrt(10 / 2)]),
            'Ia3d': np.array([np.sqrt(6 / 6), np.sqrt(8 / 6), np.sqrt(14 / 6), np.sqrt(16 / 6), np.sqrt(20 / 6), np.sqrt(22 / 6),
                     np.sqrt(24 / 6)]),
            'Fd3m': np.array([np.sqrt(3 / 3), np.sqrt(8 / 3), np.sqrt(11 / 3), np.sqrt(12 / 3), np.sqrt(16 / 3), np.sqrt(19 / 3),
                     np.sqrt(24 / 3)])
}

crystals = {
            'Im3m': np.array([np.sqrt(2), np.sqrt(4), np.sqrt(6), np.sqrt(8), np.sqrt(10), np.sqrt(12),
                     np.sqrt(14)]),
            'Pn3m': np.array([np.sqrt(2), np.sqrt(3), np.sqrt(4), np.sqrt(6), np.sqrt(8), np.sqrt(9),
                     np.sqrt(10)]),
            'Ia3d': np.array([np.sqrt(6), np.sqrt(8), np.sqrt(14), np.sqrt(16), np.sqrt(20), np.sqrt(22),
                     np.sqrt(24)]),
            'Fd3m': np.array([np.sqrt(3), np.sqrt(8), np.sqrt(11), np.sqrt(12), np.sqrt(16), np.sqrt(19),
                     np.sqrt(24)])
}