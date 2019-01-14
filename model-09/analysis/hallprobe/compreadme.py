#!/usr/bin/env python-sirius
"""Run analysis."""

#
import numpy as np
import matplotlib.pyplot as plt
# from fieldmaptrack import hallprobe as hall
# import mathphys as mp


def load_readme(fname):
    """."""
    with open(fname, 'r') as f:
        lines = f.readlines()

    magnets, angles, dints, qints, sints = [], [], [], [], []
    for line in lines:
        if 'B1-' in line or 'B2-' in line:
            line = line.replace('|','')
            magnet, *words = line.split()
            angle, dint, qint, sint = [float(v) for v in words]
            magnets.append(magnet)
            angles.append(angle)
            dints.append(dint)
            qints.append(qint)
            sints.append(sint)
    return np.array(magnets), np.array(angles), \
           np.array(dints), np.array(qints), np.array(sints)


def plot_diff(curr):
    """."""

    x1 = 'x0-8p598mm'
    x2 = 'x0-8p539mm'

    f = './production/'+x1+'/README-'+curr+'-Zpositive.md'
    magnets1p, angles1p, dints1p, qints1p, sints1p = load_readme(f)
    f = './production/'+x1+'/README-'+curr+'-Znegative.md'
    magnets1n, angles1n, dints1n, qints1n, sints1n = load_readme(f)

    f = './production/'+x2+'/README-'+curr+'-Zpositive.md'
    magnets2p, angles2p, dints2p, qints2p, sints2p = load_readme(f)
    f = './production/'+x2+'/README-'+curr+'-Znegative.md'
    magnets2n, angles2n, dints2n, qints2n, sints2n = load_readme(f)

    qints1 = qints1p+qints1n
    qints2 = qints2p+qints2n
    dqints1 = 100*(qints1 - np.mean(qints1))/np.mean(qints1)
    dqints2 = 100*(qints2 - np.mean(qints2))/np.mean(qints2)
    plt.plot(dqints1, label=x1)
    plt.plot(dqints2, label=x2)
    plt.xlabel('Magnet Index')
    plt.ylabel('Diff Integrated Quadrupole from Avg [%]')
    plt.title('{}'.format(curr))
    plt.legend()
    plt.show()

plot_diff('381.7A')
plot_diff('401.8A')
plot_diff('403.6A')
plot_diff('421.9A')
