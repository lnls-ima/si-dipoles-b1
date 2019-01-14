#!/usr/bin/env python-sirius
"""Run analysis."""


import numpy as np
import matplotlib.pyplot as plt
from fieldmaptrack import hallprobe as hall
import mathphys as mp


_fmap_files = None

# --- original energies
c2e = {
    '381.7A': 2.852,
    '401.8A': 3.000,
    '421.9A': 3.148,
}

# --- media dos imas, apos procura do B2 com x0=8.165mm
c2e_B2 = {
    '381.7A': 2.8426315121951222,
    '401.8A': 2.990131219512195,
    # '403.6A': 3.0131593524884295,  # interpolated
    '403.6A': 3.0033241824405446, # poly fitted order=2
    '421.9A': 3.137303658536585,
}

# media dos imas, apos procura do B2 com x0=8.153mm
c2e_B2 = {
    '381.7A' : 2.84308943902439,
    '401.8A' : 2.990614,
    '403.6A' : 3.003809843074398, # poly fitted order=2
    '421.9A' : 3.137824707317073,
}

# --- media dos imas, apos procura do B1 com x0=8.285mm
c2e_B1 = {
    '381.7A': 2.8526211463414635,
    '401.8A': 3.0002371951219517,
    '403.6A': 3.0134503658536587,
    '421.9A': 3.1445346190476187,
}


# --- media dos imas, apos procura do B1 com x0=8.365 mm
c2e_B1 = {
    '381.7A' : 2.8495769268292683,
    '401.8A' : 2.9970287317073168,
    '403.6A' : 3.0102059268292685,
    '421.9A' : 3.144332682926829,
}

# -- media dos imas, apos procura do B1 com x0=8.598 mm
c2e_B1 = {
    '381.7A' : 2.840677756097561,
    '401.8A' : 2.987685682926829,
    '403.6A' : 3.0008746829268294,
    '421.9A' : 3.134536902439024,
}


# vB2 = np.array([
#     2.8426315121951222,
#     2.990131219512195,
#     3.0033241824405446,  # interpolated
#     3.137303658536585,
# ])
#
# vB1 = np.array([
#     2.840677756097561,
#     2.987685682926829,
#     3.0008746829268294,
#     3.134536902439024,
# ])
#
# diff = [-0.06873054 -0.08178693 -0.08155961 -0.08818898]
#
# print(100*(vB1 - vB2)/vB2)
#
# x = [381.7, 401.8, 421.9]
# y = vB2[[0,1,3]]
# z = np.polyfit(x, y, 2)
# p = np.poly1d(z)
# print(p(403.6))



def fit_energy(c2e):
    fmts = "'{}' : {}"
    ic, c, e = [], [], []
    for curr in c2e:
        if c2e[curr]:
            v = c2e[curr]
            c.append(float(curr.replace('A', '')))
            e.append(v)
            print(fmts.format(str(curr), v))
        else:
            ic.append(curr)
    z = np.polyfit(c, e, len(c)-1)
    p = np.poly1d(z)
    for curr in ic:
        c = float(curr.replace('A', ''))
        v = p(c)
        print(fmts.format(str(curr), v))


def load_search_reference_points_file():
    """."""
    with open('search-refpoint.txt') as fp:
        text = fp.readlines()
    data = dict()
    for line in text:
        words = line.split(':')
        magnet = words[1].split(',')[0]
        current = words[2].split(' =>')[0]
        energy = float(words[3].split(' GeV')[0])
        rx = float(words[4].split(' mm')[0])
        px = float(words[5].split(' deg')[0])
        if current not in data:
            data[current] = {magnet: (energy, rx, px)}
        elif magnet not in data[current]:
            data[current][magnet] = (energy, rx, px)
        else:
            raise ValueError()
    currs = tuple(data.keys())
    mags = tuple(data[currs[0]].keys())

    currents = tuple(c for m in mags for c in currs)
    energies = tuple(data[c][m][0] for m in mags for c in currs)
    rx = tuple(data[c][m][1] for m in mags for c in currs)
    px = tuple(data[c][m][2] for m in mags for c in currs)
    magnets = tuple(m for m in mags for c in currs)
    return currents, magnets, energies, rx, px

    # print(energies)
    # energies = tuple(tuple(data[c][m][0] for m in magnets) for c in currs)
    # rx = tuple(tuple(data[c][m][1] for m in magnets) for c in currs)
    # px = tuple(tuple(data[c][m][2] for m in magnets) for c in currs)
    # return currents, magnets, energies, rx, px


def load_search_reference_points_file_relaxed():
    """."""
    with open('search-refpoint-relaxed.txt') as fp:
        text = fp.readlines()
    # data = dict()
    for i in range(len(text)):
        if 'magnet' in text[i]:
            # text[i]
            line = text[i]
            words = line.split(' ')
            magnet = words[0].replace(',', '').split(':')[1]
            current = words[1].split(':')[1]
            energy = float(words[3].split(':')[1])
            x0 = float(words[6])
            px = float(words[8].split(':')[1])
            # text[i-1]
            line = text[i-1]
            # wordsdangp = line.split(' ')
            magnet = words[0].replace(',', '').split(':')[1]

            print(magnet, current, energy, x0, px)


def seach_for_reference_point_B1():
    """."""
    def calc_residue_new(f):
        a1, b1 = f.calc_asymptotic_line_coeffs(f.traj)
        a2, b2 = f.calc_asymptotic_line_coeffs(f.configN.traj)
        a1 = f.calc_deflection_angle(f.traj)
        a2 = f.calc_deflection_angle(f.configN.traj)
        da1 = abs(a1) - abs(f.model_nominal_angle/2)
        da2 = abs(a2) - abs(f.model_nominal_angle/2)
        return np.array([da1, da2,
                         b1 - f.model_nominal_refrx,
                         b2 - f.model_nominal_refrx])

    def calc_residue_old(f):
        rp = np.array(f.reference_point) - \
            np.array((f.model_nominal_refrx, 0))
        da = abs(f.deflection_angle) - abs(f.model_nominal_angle)
        return np.array([da, rp[0], rp[1]])

    def search(f, p0, dp):
        """."""
        calc_residue = calc_residue_new
        sfmt = ('residue - dangP:{:+6.3f} %, dangN:{:+6.3f} %, '
                'drefrxP:{:+7.2f} um, drefrxN:{:+7.2f} um')
        p = np.array(p0)
        dp = np.array(dp)
        # res0
        f.traj_init_rx = p[0]
        f.traj_init_px = p[1]
        f.energy = p[2]
        f.analysis_trajectory()
        res0 = calc_residue(f)
        resn = res0 / np.array(
            [0.01*abs(f.model_nominal_angle/2),
             0.01*abs(f.model_nominal_angle/2),
             0.001, 0.001])
        print(sfmt.format(*resn))
        m = np.zeros((len(res0), 3))

        for i in range(4):

            # --- m[:,0]
            f.traj_init_rx = p[0] + dp[0]
            f.traj_init_px = p[1]
            f.energy = p[2]
            f.analysis_trajectory()
            r = calc_residue(f)
            m[:, 0] = (r - res0)/dp[0]

            # --- m[:,1]
            f.traj_init_rx = p[0]
            f.traj_init_px = p[1] + dp[1]
            f.energy = p[2]
            f.analysis_trajectory()
            r = calc_residue(f)
            m[:, 1] = (r - res0)/dp[1]

            # --- m[:,2]
            f.traj_init_rx = p[0]
            f.traj_init_px = p[1]
            f.energy = p[2] + dp[2]
            f.analysis_trajectory()
            r = calc_residue(f)
            m[:, 2] = (r - res0)/dp[2]

            # --- solve
            dr, *_ = np.linalg.lstsq(m, -res0, None)
            # dr = np.linalg.solve(m, -res0)
            p = p + dr
            dp *= 0.8

            # res0
            f.traj_init_rx = p[0]
            f.traj_init_px = p[1]
            f.energy = p[2]
            f.analysis_trajectory()
            res0 = calc_residue(f)
            resn = res0 / np.array(
                [0.01*abs(f.model_nominal_angle/2),
                 0.01*abs(f.model_nominal_angle/2),
                 0.001, 0.001])
            print(sfmt.format(*resn))

        return p, res0

    c2e_B1 = {
        '381.7A': 2.852039,
        '401.8A': 3.000021,
        '421.9A': 3.147681,
    }

    fstr = ('magnet:{}, current:{} => energy:{:8.6f} '
            'GeV, x0:{:6.3f} mm, px:{:+7.4f} deg')

    magnets = get_magnets_B1()
    currents = get_currents_B1()
    for magnet in magnets:
        for curr in currents:
            fname = get_fmap_files_B1(magnet, curr)[0]
            # print(fname)
            f = hall.DoubleFMapAnalysis(
                magnet=magnet, fmap_fname=fname)
            f.analysis_rawfield()
            p0 = [7.92, 0.0, c2e_B1[curr]]
            dp = [0.5, 0.3, 0.05]
            p, res0 = search(f, p0, dp)
            print(fstr.format(magnet, curr, p[2], p[0], p[1]))


def plot_results_search_reference_points_B1():
    """."""
    currents, magnets, energies, rx, px = load_search_reference_points_file()

    # energies x current

    # 381.7A: 2.850293 GeV  std: 0.026 %  minmax: [-0.050,+0.069] %
    # 401.8A: 2.998122 GeV  std: 0.023 %  minmax: [-0.036,+0.043] %
    # 421.9A: 3.145611 GeV  std: 0.028 %  minmax: [-0.044,+0.057] %

    data = dict()
    for i in range(len(currents)):
        if currents[i] in data:
            data[currents[i]].append(energies[i])
        else:
            data[currents[i]] = [energies[i], ]

    # print
    fstr = '{}: {:.6f} GeV  std: {:0.3f} %  minmax: [{:+0.3f},{:+0.3f}] %'
    print('Averages:')
    for cur in data:
        d = data[cur]
        avg = np.mean(d)
        std = np.std(d)
        de = 100*(d - avg)/avg
        print(fstr.format(cur, avg, 100*std/avg, min(de), max(de)))

    # plot
    for cur in data:
        d = data[cur]
        de = 100*(d - np.mean(d))/np.mean(d)
        plt.plot(de, 'o', label=cur)
    plt.legend()
    plt.grid()
    plt.xlabel('Magnet index')
    plt.ylabel('Energy deviation [%]')
    plt.show()

    # rx and px x magnet


def plot_results_search_reference_points_relaxed_B1():
    """."""
    d381p7A = np.array([
        [2.848880, 7.970, +0.0262],
        [2.849926, 7.964, -0.0063],
        [2.850784, 7.962, +0.0072],
        [2.849825, 7.963, -0.0155],
        [2.849165, 7.964, +0.0173],
        [2.849716, 7.967, +0.0053],
        [2.849981, 7.966, -0.0146],
        [2.852262, 7.960, -0.0265],
        [2.850515, 7.957, +0.0159],
        [2.851081, 7.955, -0.0107],
        [2.851349, 7.957, +0.0143],
        [2.849121, 7.964, -0.0032],
        [2.849671, 7.962, +0.0086],
        [2.850017, 7.961, +0.0324],
        [2.851427, 7.957, +0.0199],
        [2.850374, 7.961, -0.0207],
        [2.850050, 7.960, +0.0094],
        [2.849103, 7.966, -0.0305],
        [2.850035, 7.965, -0.0356],
        [2.849523, 7.966, -0.0071],
        [2.849699, 7.965, +0.0020],
        [2.850636, 7.964, +0.0051],
        [2.849966, 7.967, -0.0195],
        [2.850496, 7.965, +0.0035],
        [2.850935, 7.963, -0.0108],
        [2.851207, 7.963, -0.0068],
        [2.850787, 7.964, -0.0338],
        [2.849765, 7.967, +0.0317],
        [2.850790, 7.968, +0.0047],
        [2.850709, 7.967, -0.0079],
        [2.850909, 7.965, -0.0061],
        [2.849964, 7.968, +0.0083],
        [2.850044, 7.962, -0.0062],
        [2.849876, 7.966, +0.0019],
        [2.850034, 7.967, +0.0117],
        [2.849969, 7.963, -0.0229],
        [2.850028, 7.962, +0.0067],
        [2.849664, 7.963, -0.0019],
        [2.850995, 7.962, +0.0094],
        [2.851099, 7.963, +0.0194],
        [2.851654, 7.959, -0.0002]])

    avg = np.mean(d381p7A[:, 0])

    currents, magnets, energies, rx, px = load_search_reference_points_file()

    # energies x current

    # 381.7A: 2.850293 GeV  std: 0.026 %  minmax: [-0.050,+0.069] %
    # 401.8A: 2.998122 GeV  std: 0.023 %  minmax: [-0.036,+0.043] %
    # 421.9A: 3.145611 GeV  std: 0.028 %  minmax: [-0.044,+0.057] %

    data = dict()
    for i in range(len(currents)):
        if currents[i] in data:
            data[currents[i]].append(energies[i])
        else:
            data[currents[i]] = [energies[i], ]

    # print
    fstr = '{}: {:.6f} GeV  std: {:0.3f} %  minmax: [{:+0.3f},{:+0.3f}] %'
    print('Averages:')
    for cur in data:
        d = data[cur]
        avg = np.mean(d)
        std = np.std(d)
        de = 100*(d - avg)/avg
        print(fstr.format(cur, avg, 100*std/avg, min(de), max(de)))

    # plot
    for cur in data:
        d = data[cur]
        de = 100*(d - np.mean(d))/np.mean(d)
        plt.plot(de, 'o', label=cur)
    plt.legend()
    plt.grid()
    plt.xlabel('Magnet index')
    plt.ylabel('Energy deviation [%]')
    plt.show()

    # rx and px x magnet


def generate_inputs_reference_point_B1():
    """."""
    print('incomplete...')
    currents, magnets, energies, rx, px = load_search_reference_points_file()

    # c2e_B1 = {
    #     '381.7A': 2.852039,
    #     '401.8A': 3.000021,
    #     '421.9A': 3.147681,
    # }
    path_base = (
        '/home/fac_files/lnls-ima/si-dipoles-b1/model-09/analysis/'
        'hallprobe/production/refpoint/')

    for i in range(len(currents)):
        magnet = magnets[i]
        current = currents[i]
        path = path_base + magnet + '/' + current.replace('.', 'p') + '/'
        fname = get_fmap_files_B1(magnet, current)[0]
        f = hall.DoubleFMapAnalysis(magnet=magnet, fmap_fname=fname)
        # default_s_step = f.get_defaults()['traj_rk_s_step']
        print(path, f)

def run():
    """."""
    # fit_energy(c2e_B2)
    # hall.search_for_deflection_angle_vary_x0(c2e_B2, 'B1')
    # hall.generate_inputs(c2e_B2, '8p527', dipole_type='B1')
    # hall.load_analysis_result('x0-8p527mm/', 'B1', ('dangle', 'refrx', 'quad'))
    hall.save_readme_files(c2e_B2, 'x0-8p527mm/', 'B1')
    # hall.generate_inputs(c2e_B2, '8p546', dipole_type='B1')
    # hall.load_analysis_result('x0-8p539mm/', 'B1', ('dangle', 'refrx', 'quad'))
    # hall.save_readme_files(c2e_B2, 'x0-8p539mm/', 'B1')

    # hall.search_for_deflection_angle('B1')
    # hall.plot_results_search_deflection_angle('search-energies-shifted-x0.txt')
    # hall.load_analysis_result('x0-8p598mm/', 'B1', ('dangle', 'refrx', 'quad'))
    # hall.save_readme_files(c2e_B1, 'x0-8p598mm/', 'B1')

    # seach_for_reference_point_B1()
    # load_search_reference_points_file()
    # plot_results_search_reference_points_B1()
    # generate_inputs_reference_point_B1()
    # load_search_reference_points_file_relaxed()
    # plot_results_search_reference_points_relaxed_B1()

    # currents, magnets, energies = \
    #     load_search_deflection_angle_file(fname='search-energies-shifted-x0.txt')
    # e = [[], [], []]
    # for i in range(len(currents)):
    #     if currents[i] == '381.7A':
    #         e[0].append(energies[i])
    #     elif currents[i] == '401.8A':
    #         e[1].append(energies[i])
    #     elif currents[i] == '421.9A':
    #         e[2].append(energies[i])
    #
    # print(e[0])
    # print(np.mean(np.array(e[0])))
    # print()
    #
    # print(e[1])
    # print(np.mean(np.array(e[1])))
    # print()
    #
    # print(e[2])
    # print(np.mean(np.array(e[2])))
    # print()

run()

# v1 = [
# 8.5571, 8.5590, 8.5351, 8.5330, 8.5590, 8.5458, 8.5351, 8.5345, 8.5645, 8.5522,
# 8.5358, 8.5579, 8.5267, 8.5750, 8.5608, 8.5236, 8.5638, 8.5422, 8.5494, 8.5610,
# 8.5452, 8.5337, 8.5272, 8.5571, 8.5663, 8.5525, 8.5594, 8.5374, 8.5310, 8.5562,
# 8.5582, 8.5314, 8.5420, 8.5496, 8.5292, 8.5637, 8.5372, 8.5429, 8.5563,
# ]
# v2 = [
# 8.5432, 8.5425, 8.5261, 8.5225, 8.5522, 8.5339, 8.5291, 8.5184, 8.5522, 8.5439,
# 8.5183, 8.5577, 8.5146, 8.5510, 8.5526, 8.5066, 8.5599, 8.5212, 8.5408, 8.5533,
# 8.5345, 8.5112, 8.5166, 8.5535, 8.5622, 8.5458, 8.5503, 8.5247, 8.5288, 8.5438,
# 8.5611, 8.5233, 8.5330, 8.5448, 8.5150, 8.5605, 8.5261, 8.5329, 8.5425,
# ]
# v3 = [
# 8.5414, 8.5455, 8.5277, 8.5234, 8.5496, 8.5309, 8.5312, 8.5128, 8.5538, 8.5491,
# 8.5266, 8.5550, 8.5136, 8.5574, 8.5587, 8.5044, 8.5561, 8.5257, 8.5484, 8.5482,
# 8.5356, 8.5087, 8.5121, 8.5467, 8.5576, 8.5453, 8.5520, 8.5257, 8.5281, 8.5375,
# 8.5542, 8.5238, 8.5315, 8.5441, 8.5196, 8.5584, 8.5277, 8.5310, 8.5396,
# ]
# v4 = [
# 8.5375, 8.5353, 8.5251, 8.5182, 8.5480, 8.5348, 8.5252, 8.5036, 8.5504, 8.5491,
# 8.5237, 8.5552, 8.5011, 8.5523, 8.5578, 8.5064, 8.5437, 8.5172, 8.5450, 8.5444,
# 8.5322, 8.5079, 8.5070, 8.5435, 8.5477, 8.5415, 8.5513, 8.5225, 8.5254, 8.5334,
# 8.5478, 8.5231, 8.5308, 8.5365, 8.5180, 8.5505, 8.5214, 8.5258, 8.5335,
# ]
#
# plt.plot(v1)
# plt.plot(v2)
# plt.plot(v3)
# plt.plot(v4)
# plt.show()
#
# v = v1+v2+v3+v4
# print(np.mean(v))
# <x0> = 8.538532692307692


# v = [
#  [0.0020 ,  +0.00644 ,  +0.0000e+00 ,  -7.5340e-01 ,  -2.9735e-01 ,  +7.7615e-01 ,  -3.7805e+01 ,  +7.7650e+03 ,  -5.4386e+04 , ],
#  [0.0030 ,  +0.00966 ,  +0.0000e+00 ,  -7.5575e-01 ,  -2.4508e-01 ,  +4.5129e-01 ,  -3.8924e+01 ,  +6.5029e+03 ,  -1.5664e+04 , ],
#  [0.0050 ,  +0.01614 ,  +0.0000e+00 ,  -7.6242e-01 ,  -1.1701e-01 ,  -2.3400e-01 ,  -4.5079e+01 ,  +5.9481e+03 ,  +7.0597e+04 , ],
#  [0.0050 ,  +0.01620 ,  +0.0000e+00 ,  -7.7003e-01 ,  -1.5001e-02 ,  +5.4571e-02 ,  -3.7010e+01 ,  +5.2731e+03 ,  +7.1373e+04 , ],
#  [0.0050 ,  +0.01623 ,  +0.0000e+00 ,  -7.7387e-01 ,  +3.8018e-03 ,  +7.4966e-01 ,  -2.3986e+01 ,  +4.2452e+03 ,  +1.1962e+05 , ],
#  [0.0100 ,  +0.03250 ,  +0.0000e+00 ,  -7.7496e-01 ,  -3.1229e-03 ,  +9.7935e-01 ,  +2.3856e+00 ,  +3.5272e+03 ,  +1.2499e+05 , ],
#  [0.0400 ,  +0.12976 ,  +0.0000e+00 ,  -7.7402e-01 ,  +1.9461e-02 ,  +1.1120e+00 ,  +2.3872e+01 ,  +3.1803e+03 ,  +1.2777e+05 , ],
#  [0.1500 ,  +0.48326 ,  +0.0000e+00 ,  -7.7343e-01 ,  +5.4918e-02 ,  +1.9857e+00 ,  +4.0989e+01 ,  +3.4137e+03 ,  +1.4539e+05 , ],
#  [0.1000 ,  +0.32210 ,  +0.0000e+00 ,  -7.7298e-01 ,  +7.5842e-02 ,  +2.6791e+00 ,  +5.4030e+01 ,  +3.4599e+03 ,  +1.3914e+05 , ],
#  [0.0500 ,  +0.16186 ,  +0.0000e+00 ,  -7.7450e-01 ,  +7.8398e-03 ,  +1.7151e+00 ,  +4.9396e+01 ,  +3.6838e+03 ,  +1.3839e+05 , ],
#  [0.0340 ,  +0.10511 ,  +0.0000e+00 ,  -7.7652e-01 ,  -1.5867e-01 ,  +5.6619e+00 ,  +3.2082e+01 ,  +7.9171e+03 ,  -1.3675e+04 , ],
#  [0.0160 ,  +0.03328 ,  +0.0000e+00 ,  -4.2796e-01 ,  -2.2317e+00 ,  +1.6032e+01 ,  -1.8676e+02 ,  +1.7391e+04 ,  -3.2940e+05 , ],
#  [0.0400 ,  +0.03267 ,  +0.0000e+00 ,  -8.4794e-02 ,  -1.9642e+00 ,  +7.5802e+00 ,  -5.1702e+01 ,  +5.4621e+03 ,  +5.5585e+03 , ],
#  [0.0400 ,  +0.00789 ,  +0.0000e+00 ,  -9.0989e-03 ,  -4.2785e-01 ,  +1.5586e+00 ,  +2.0396e+01 ,  +3.4934e+01 ,  +1.2201e+03 , ],
#  [0.0500 ,  +0.00455 ,  -3.8076e-06 ,  -9.9754e-04 ,  -1.0224e-01 ,  +2.0697e-01 ,  +4.4900e+00 ,  -1.5401e+01 ,  -6.3421e+02 ,],
# ]
#
# L = np.array([l[0] for l in v])
# K = np.array([l[3] for l in v])
# KL = K*L
# print(sum(KL))
