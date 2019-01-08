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
    '403.6A': 3.0131593524884295,  # interpolated
    '421.9A': 3.137303658536585,
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

# v1 = np.array([
# 2.8426315121951222,
# 2.990131219512195,
# 3.0131593524884295,  # interpolated
# 3.137303658536585,])
#
# v2 = np.array([
#     2.8495769268292683,
#     2.9970287317073168,
#     3.0102059268292685,
#     3.144332682926829,])
#
# print(100*(v2 - v1)/v1)
# [ 0.24433046  0.2306759  -0.09801757  0.22404667


def get_fmap_files_B1(magnet=None, current=None):
    """."""
    global _fmap_files

    if _fmap_files is None:
        _s = '_Hall_X=-32_32mm_Z=-800_800mm_Imc='
        _fmap_files = (
            '2018-12-07_B1-002' + _s + '381.7A_ID=799.dat',
            '2018-12-07_B1-002' + _s + '401.8A_ID=800.dat',
            '2018-12-07_B1-002' + _s + '403.6A_ID=801.dat',
            '2018-12-07_B1-002' + _s + '421.9A_ID=802.dat',
            '2018-12-15_B1-003' + _s + '381.7A_ID=981.dat',
            '2018-12-15_B1-003' + _s + '401.8A_ID=982.dat',
            '2018-12-15_B1-003' + _s + '403.6A_ID=983.dat',
            '2018-12-15_B1-003' + _s + '421.9A_ID=984.dat',
            '2018-12-17_B1-004' + _s + '381.7A_ID=1021.dat',
            '2018-12-17_B1-004' + _s + '401.8A_ID=1022.dat',
            '2018-12-17_B1-004' + _s + '403.6A_ID=1023.dat',
            '2018-12-17_B1-004' + _s + '421.9A_ID=1024.dat',
            '2018-12-13_B1-005' + _s + '381.7A_ID=912.dat',
            '2018-12-13_B1-005' + _s + '401.8A_ID=913.dat',
            '2018-12-13_B1-005' + _s + '403.6A_ID=914.dat',
            '2018-12-13_B1-005' + _s + '421.9A_ID=915.dat',
            '2018-12-15_B1-006' + _s + '381.7A_ID=970.dat',
            '2018-12-15_B1-006' + _s + '401.8A_ID=971.dat',
            '2018-12-15_B1-006' + _s + '403.6A_ID=972.dat',
            '2018-12-15_B1-006' + _s + '421.9A_ID=973.dat',
            '2018-12-10_B1-009' + _s + '381.7A_ID=827.dat',
            '2018-12-10_B1-009' + _s + '401.8A_ID=828.dat',
            '2018-12-10_B1-009' + _s + '403.6A_ID=829.dat',
            '2018-12-10_B1-009' + _s + '421.9A_ID=830.dat',
            '2018-12-07_B1-010' + _s + '381.7A_ID=794.dat',
            '2018-12-07_B1-010' + _s + '401.8A_ID=795.dat',
            '2018-12-07_B1-010' + _s + '403.6A_ID=796.dat',
            '2018-12-07_B1-010' + _s + '421.9A_ID=797.dat',
            '2018-12-05_B1-011' + _s + '381.7A_ID=756.dat',
            '2018-12-05_B1-011' + _s + '401.8A_ID=757.dat',
            '2018-12-05_B1-011' + _s + '403.6A_ID=758.dat',
            '2018-12-05_B1-011' + _s + '421.9A_ID=759.dat',
            '2018-12-17_B1-012' + _s + '381.7A_ID=1007.dat',
            '2018-12-17_B1-012' + _s + '401.8A_ID=1008.dat',
            '2018-12-17_B1-012' + _s + '403.6A_ID=1009.dat',
            '2018-12-17_B1-012' + _s + '421.9A_ID=1010.dat',
            '2018-12-10_B1-013' + _s + '381.7A_ID=840.dat',
            '2018-12-10_B1-013' + _s + '401.8A_ID=841.dat',
            '2018-12-10_B1-013' + _s + '403.6A_ID=842.dat',
            '2018-12-10_B1-013' + _s + '421.9A_ID=843.dat',
            '2018-12-08_B1-014' + _s + '381.7A_ID=815.dat',
            '2018-12-08_B1-014' + _s + '401.8A_ID=816.dat',
            '2018-12-08_B1-014' + _s + '403.6A_ID=817.dat',
            '2018-12-08_B1-014' + _s + '421.9A_ID=818.dat',
            '2018-12-16_B1-015' + _s + '381.7A_ID=1001.dat',
            '2018-12-16_B1-015' + _s + '401.8A_ID=1002.dat',
            '2018-12-16_B1-015' + _s + '403.6A_ID=1003.dat',
            '2018-12-16_B1-015' + _s + '421.9A_ID=1004.dat',
            '2018-12-11_B1-016' + _s + '381.7A_ID=856.dat',
            '2018-12-11_B1-016' + _s + '401.8A_ID=857.dat',
            '2018-12-11_B1-016' + _s + '403.6A_ID=858.dat',
            '2018-12-11_B1-016' + _s + '421.9A_ID=859.dat',
            '2018-12-03_B1-017' + _s + '381.7A_ID=712.dat',
            '2018-12-03_B1-017' + _s + '401.8A_ID=713.dat',
            '2018-12-03_B1-017' + _s + '403.6A_ID=714.dat',
            '2018-12-03_B1-017' + _s + '421.9A_ID=715.dat',
            '2018-12-15_B1-018' + _s + '381.7A_ID=963.dat',
            '2018-12-15_B1-018' + _s + '401.8A_ID=964.dat',
            '2018-12-15_B1-018' + _s + '403.6A_ID=965.dat',
            '2018-12-15_B1-018' + _s + '421.9A_ID=966.dat',
            '2018-12-10_B1-019' + _s + '381.7A_ID=822.dat',
            '2018-12-10_B1-019' + _s + '401.8A_ID=823.dat',
            '2018-12-10_B1-019' + _s + '403.6A_ID=824.dat',
            '2018-12-10_B1-019' + _s + '421.9A_ID=825.dat',
            '2018-12-14_B1-020' + _s + '381.7A_ID=947.dat',
            '2018-12-14_B1-020' + _s + '401.8A_ID=948.dat',
            '2018-12-14_B1-020' + _s + '403.6A_ID=949.dat',
            '2018-12-14_B1-020' + _s + '421.9A_ID=950.dat',
            '2018-12-12_B1-021' + _s + '381.7A_ID=899.dat',
            '2018-12-12_B1-021' + _s + '401.8A_ID=900.dat',
            '2018-12-12_B1-021' + _s + '403.6A_ID=901.dat',
            '2018-12-12_B1-021' + _s + '421.9A_ID=902.dat',
            '2018-12-04_B1-022' + _s + '381.7A_ID=720.dat',
            '2018-12-04_B1-022' + _s + '401.8A_ID=721.dat',
            '2018-12-04_B1-022' + _s + '403.6A_ID=722.dat',
            '2018-12-04_B1-022' + _s + '421.9A_ID=723.dat',
            '2018-12-12_B1-023' + _s + '381.7A_ID=890.dat',
            '2018-12-12_B1-023' + _s + '401.8A_ID=891.dat',
            '2018-12-12_B1-023' + _s + '403.6A_ID=892.dat',
            '2018-12-12_B1-023' + _s + '421.9A_ID=893.dat',
            '2018-12-16_B1-024' + _s + '381.7A_ID=988.dat',
            '2018-12-16_B1-024' + _s + '401.8A_ID=989.dat',
            '2018-12-16_B1-024' + _s + '403.6A_ID=990.dat',
            '2018-12-16_B1-024' + _s + '421.9A_ID=991.dat',
            '2018-12-15_B1-025' + _s + '381.7A_ID=958.dat',
            '2018-12-15_B1-025' + _s + '401.8A_ID=959.dat',
            '2018-12-15_B1-025' + _s + '403.6A_ID=960.dat',
            '2018-12-15_B1-025' + _s + '421.9A_ID=961.dat',
            '2018-12-05_B1-026' + _s + '381.7A_ID=747.dat',
            '2018-12-05_B1-026' + _s + '401.8A_ID=748.dat',
            '2018-12-05_B1-026' + _s + '403.6A_ID=749.dat',
            '2018-12-05_B1-026' + _s + '421.9A_ID=750.dat',
            '2018-12-15_B1-027' + _s + '381.7A_ID=976.dat',
            '2018-12-15_B1-027' + _s + '401.8A_ID=977.dat',
            '2018-12-15_B1-027' + _s + '403.6A_ID=978.dat',
            '2018-12-15_B1-027' + _s + '421.9A_ID=979.dat',
            '2018-12-13_B1-028' + _s + '381.7A_ID=922.dat',
            '2018-12-13_B1-028' + _s + '401.8A_ID=923.dat',
            '2018-12-13_B1-028' + _s + '403.6A_ID=924.dat',
            '2018-12-13_B1-028' + _s + '421.9A_ID=925.dat',
            '2018-12-16_B1-029' + _s + '381.7A_ID=996.dat',
            '2018-12-16_B1-029' + _s + '401.8A_ID=997.dat',
            '2018-12-16_B1-029' + _s + '403.6A_ID=998.dat',
            '2018-12-16_B1-029' + _s + '421.9A_ID=999.dat',
            '2018-12-10_B1-030' + _s + '381.7A_ID=833.dat',
            '2018-12-10_B1-030' + _s + '401.8A_ID=834.dat',
            '2018-12-10_B1-030' + _s + '403.6A_ID=835.dat',
            '2018-12-10_B1-030' + _s + '421.9A_ID=836.dat',
            '2018-12-11_B1-031' + _s + '381.7A_ID=848.dat',
            '2018-12-11_B1-031' + _s + '401.8A_ID=849.dat',
            '2018-12-11_B1-031' + _s + '403.6A_ID=850.dat',
            '2018-12-11_B1-031' + _s + '421.9A_ID=851.dat',
            '2018-12-06_B1-032' + _s + '381.7A_ID=783.dat',
            '2018-12-06_B1-032' + _s + '401.8A_ID=784.dat',
            '2018-12-06_B1-032' + _s + '403.6A_ID=785.dat',
            '2018-12-06_B1-032' + _s + '421.9A_ID=786.dat',
            '2018-12-17_B1-033' + _s + '381.7A_ID=1016.dat',
            '2018-12-17_B1-033' + _s + '401.8A_ID=1017.dat',
            '2018-12-17_B1-033' + _s + '403.6A_ID=1018.dat',
            '2018-12-17_B1-033' + _s + '421.9A_ID=1019.dat',
            '2018-12-07_B1-034' + _s + '381.7A_ID=804.dat',
            '2018-12-07_B1-034' + _s + '401.8A_ID=805.dat',
            '2018-12-07_B1-034' + _s + '403.6A_ID=806.dat',
            '2018-12-07_B1-034' + _s + '421.9A_ID=807.dat',
            '2018-12-13_B1-035' + _s + '381.7A_ID=930.dat',
            '2018-12-13_B1-035' + _s + '401.8A_ID=931.dat',
            '2018-12-13_B1-035' + _s + '403.6A_ID=932.dat',
            '2018-12-13_B1-035' + _s + '421.9A_ID=933.dat',
            '2018-12-13_B1-036' + _s + '381.7A_ID=917.dat',
            '2018-12-13_B1-036' + _s + '401.8A_ID=918.dat',
            '2018-12-13_B1-036' + _s + '403.6A_ID=919.dat',
            '2018-12-13_B1-036' + _s + '421.9A_ID=920.dat',
            '2018-12-12_B1-037' + _s + '381.7A_ID=883.dat',
            '2018-12-12_B1-037' + _s + '401.8A_ID=884.dat',
            '2018-12-12_B1-037' + _s + '403.6A_ID=885.dat',
            '2018-12-12_B1-037' + _s + '421.9A_ID=886.dat',
            '2018-12-08_B1-038' + _s + '381.7A_ID=809.dat',
            '2018-12-08_B1-038' + _s + '401.8A_ID=810.dat',
            '2018-12-08_B1-038' + _s + '403.6A_ID=811.dat',
            '2018-12-08_B1-038' + _s + '421.9A_ID=812.dat',
            '2018-12-06_B1-039' + _s + '381.7A_ID=776.dat',
            '2018-12-06_B1-039' + _s + '401.8A_ID=777.dat',
            '2018-12-06_B1-039' + _s + '403.6A_ID=778.dat',
            '2018-12-06_B1-039' + _s + '421.9A_ID=779.dat',
            '2018-12-05_B1-040' + _s + '381.7A_ID=767.dat',
            '2018-12-05_B1-040' + _s + '401.8A_ID=768.dat',
            '2018-12-05_B1-040' + _s + '403.6A_ID=769.dat',
            '2018-12-05_B1-040' + _s + '421.9A_ID=770.dat',
            '2018-12-12_B1-041' + _s + '381.7A_ID=905.dat',
            '2018-12-12_B1-041' + _s + '401.8A_ID=906.dat',
            '2018-12-12_B1-041' + _s + '403.6A_ID=907.dat',
            '2018-12-12_B1-041' + _s + '421.9A_ID=908.dat',
            '2018-12-05_B1-042' + _s + '381.7A_ID=741.dat',
            '2018-12-05_B1-042' + _s + '401.8A_ID=742.dat',
            '2018-12-05_B1-042' + _s + '403.6A_ID=743.dat',
            '2018-12-05_B1-042' + _s + '421.9A_ID=744.dat',
            '2018-12-14_B1-043' + _s + '381.7A_ID=939.dat',
            '2018-12-14_B1-043' + _s + '401.8A_ID=940.dat',
            '2018-12-14_B1-043' + _s + '403.6A_ID=941.dat',
            '2018-12-14_B1-043' + _s + '421.9A_ID=942.dat',
            '2018-12-04_B1-046' + _s + '381.7A_ID=735.dat',
            '2018-12-04_B1-046' + _s + '401.8A_ID=736.dat',
            '2018-12-04_B1-046' + _s + '403.6A_ID=737.dat',
            '2018-12-04_B1-046' + _s + '421.9A_ID=738.dat'
            )


    if magnet is None and current is None:
        return _fmap_files

    files = []
    for f in _fmap_files:
        if magnet is None or magnet in f:
            if current is None or current in f:
                files.append(f)
    return tuple(files)


def get_magnets_B1():
    """."""
    fnames = get_fmap_files_B1()
    magnets = []
    for f in fnames:
        magnet = f[11:11+6]
        if magnet not in magnets:
            magnets.append(magnet)
    return sorted(magnets)


def get_currents_B1():
    """."""
    fnames = get_fmap_files_B1()
    currents = []
    for f in fnames:
        current = f[51:51+6]
        if current not in currents:
            currents.append(current)
    return sorted(currents)


def search_for_deflection_angle_B1():
    """."""
    init_energies = [2.8426315121951222 , 2.990131219512195, 3.0131593524884295, 3.137303658536585]
    magnets = get_magnets_B1()
    currents = get_currents_B1()

    fstr = 'magnet:{}, current:{} => nr_iter:{:02d}, energy:{:8.6f} GeV'
    for i in range(len(currents)):
        curr = currents[i]
        for magnet in magnets:
            files = get_fmap_files_B1(magnet, curr)
            fa = hall.DoubleFMapAnalysis(magnet=magnet, fmap_fname=files[0])
            fa.traj_init_rx = 8.285 + 0.080
            fa.energy = init_energies[i]
            n = fa.search_energy(False)
            print(fstr.format(magnet, curr, n, fa.energy))


def load_search_deflection_angle_file(fname=None):
    """."""
    if fname is None:
        fname = 'search-energies.txt'
    with open(fname) as fp:
        text = fp.readlines()
    data = dict()
    for line in text:
        words = line.split(' ')
        magnet = words[0].split(':')[1].replace(',','')
        current = words[1].split(':')[1]
        energy = float(words[4].split(':')[1].split(' ')[0])
        if current not in data:
            data[current] = {magnet: energy}
        elif magnet not in data[current]:
            data[current][magnet] = energy
        else:
            raise ValueError()

    # --- average energy ---
    for current in data:
        avg = np.mean(np.array([data[current][m] for m in data[current]]))
        print('{} : {}'.format(current, avg))

    currents = tuple(data.keys())
    magnets = tuple(data[currents[0]].keys())
    energies = tuple(tuple(data[c][m] for m in magnets) for c in currents)
    return currents, magnets, energies


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


def plot_results_search_deflection_angle_B1():
    """."""
    currents, magnets, energies = load_search_deflection_angle_file()
    fst = 'current:{}  energy_avg:{:8.6f} Gev  energy_std:{:5.3f} %'
    for i in range(len(energies)):
        em = np.mean(energies[i])
        es = np.std(energies[i])
        ev = 100*(energies[i] - em)/em
        plt.plot(ev, 'o', label=currents[i])
        print(fst.format(currents[i], em, 100*es/em))
    plt.plot([0, len(ev)-1], [+0.05, ]*2, '--k', label='spec')
    plt.plot([0, len(ev)-1], [-0.05, ]*2, '--k',)
    plt.xlabel('Magnet Index')
    plt.ylabel('Nominal deflection energy spread [%]')
    plt.grid()
    plt.legend()
    plt.show()


def generate_inputs_B1():
    """."""
    # c2e_B1 = {  # media dos imas, apos procura...
    #     '381.7A': 2.852039,
    #     '401.8A': 3.000021,
    #     '421.9A': 3.147681,
    # }

    # c2e2_B1 = {  # media dos imas, apos procura com x0=8.165mm
    #     '381.7A': 2.8526211463414635,
    #     '401.8A': 3.0002371951219517,
    #     '403.6A': 3.0134503658536587,
    #     '421.9A': 3.1477130975609757,
    # }
    c2e2_B1 = c2e_B1

    path_base = (
        '/home/fac_files/lnls-ima/si-dipoles-b1/model-09/analysis/'
        'hallprobe/production/x0-8p365mm/')
    magnets = get_magnets_B1()
    currents = get_currents_B1()
    for magnet in magnets:
        print('creating input files for magnet {}'.format(magnet))
        for curr in currents:
            path = path_base + magnet + '/' + curr.replace('.', 'p') + '/'
            fname = get_fmap_files_B1(magnet, curr)[0]
            f = hall.DoubleFMapAnalysis(magnet=magnet, fmap_fname=fname)
            default_s_step = f.get_defaults()['traj_rk_s_step']
            f.energy = c2e2_B1[curr]
            f.traj_init_rx = 8.365
            # positive
            f.traj_rk_s_step = +abs(default_s_step)
            f.create_input(
                path=path, force=True, path_subdir='z-positive/')
            # negative
            f.traj_rk_s_step = -abs(default_s_step)
            f.create_input(
                path=path, force=True, path_subdir='z-negative/')


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


def load_analysis_result(folder, plots=None):
    """."""
    path_base = (
        '/home/fac_files/lnls-ima/si-dipoles-b1/model-09/analysis/'
        'hallprobe/production/' + folder)
    magnets = get_magnets_B1()
    currents = get_currents_B1()
    data = {
        'angle': dict(),
        'angleP': dict(),
        'angleN': dict(),
        'dangle': dict(),
        'energy': dict(),
        'rx0': dict(),
        'refrxP': dict(),
        'refrxN': dict(),
        'dip_normal': dict(),
        'dip_skew': dict(),
        'quad_normal': dict(),
        'quad_skew': dict(),
        'sext_normal': dict(),
        'sext_skew': dict(),
        'dip_normalP': dict(),
        'dip_skewP': dict(),
        'quad_normalP': dict(),
        'quad_skewP': dict(),
        'sext_normalP': dict(),
        'sext_skewP': dict(),
        'dip_normalN': dict(),
        'dip_skewN': dict(),
        'quad_normalN': dict(),
        'quad_skewN': dict(),
        'sext_normalN': dict(),
        'sext_skewN': dict(),
        }
    convd = {
        'initial rx position of trajectory': 'rx0',
        'beam_energy': 'energy'}
    for current in currents:
        for p in data:
            data[p][current] = []
        for magnet in magnets:
            path = path_base + magnet + '/' + current.replace('.', 'p') + '/'
            fname = get_fmap_files_B1(magnet, current)[0]
            f = hall.DoubleFMapAnalysis(magnet=magnet, fmap_fname=fname)
            dataP = f.load_output_trajectory(path, 'z-positive/')
            dataN = f.load_output_trajectory(path, 'z-negative/')

            angle = \
                dataP['horizontal_deflection_angle'] - \
                dataN['horizontal_deflection_angle']
            data['angle'][current].append(angle)
            data['angleP'][current].append(
                dataP['horizontal_deflection_angle'])
            data['angleN'][current].append(
                dataN['horizontal_deflection_angle'])
            v = dataP['rx position of reference'] - f.model_nominal_refrx
            data['refrxP'][current].append(v)
            v = dataN['rx position of reference'] - f.model_nominal_refrx
            data['refrxN'][current].append(v)

            for k in convd:
                dP = dataP[k]
                dN = dataN[k]
            if dP == dN:
                data[convd[k]][current].append(dP)
            else:
                raise ValueError('{} != {}'.format(dP, dN))

            mpoles_normalP, mpoles_skewP, harms = \
                f.load_output_multipoles(path, 'z-positive/')
            mpoles_normalN, mpoles_skewN, harms = \
                f.load_output_multipoles(path, 'z-negative/')
            mpoles_normal = np.array(mpoles_normalP) + np.array(mpoles_normalN)
            mpoles_skew = np.array(mpoles_skewP) + np.array(mpoles_skewN)
            data['dip_normal'][current].append(mpoles_normal[0])
            data['dip_skew'][current].append(mpoles_skew[0])
            data['quad_normal'][current].append(mpoles_normal[1])
            data['quad_skew'][current].append(mpoles_skew[1])
            data['sext_normal'][current].append(mpoles_normal[2])
            data['sext_skew'][current].append(mpoles_skew[2])

            data['dip_normalP'][current].append(mpoles_normalP[0])
            data['dip_skewP'][current].append(mpoles_skewP[0])
            data['quad_normalP'][current].append(mpoles_normalP[1])
            data['quad_skewP'][current].append(mpoles_skewP[1])
            data['sext_normalP'][current].append(mpoles_normalP[2])
            data['sext_skewP'][current].append(mpoles_skewP[2])

            data['dip_normalN'][current].append(mpoles_normalN[0])
            data['dip_skewN'][current].append(mpoles_skewN[0])
            data['quad_normalN'][current].append(mpoles_normalN[1])
            data['quad_skewN'][current].append(mpoles_skewN[1])
            data['sext_normalN'][current].append(mpoles_normalN[2])
            data['sext_skewN'][current].append(mpoles_skewN[2])

    for current in currents:
        a = np.array(data['angle'][current])
        am = np.mean(a)
        # dm = 100*(a - am)/am
        dm = 100*(a - (-f.model_nominal_angle))/((-f.model_nominal_angle))
        data['dangle'][current] = dm

    if not plots:
        return magnets, currents, data

    # --- energy ---
    if not plots or 'energy' in plots:
        for current in currents:
            print(current, np.mean(data['energy'][current]))
            plt.plot(data['energy'][current], 'o', label=current)
        plt.legend()
        plt.xlabel('Magnet index')
        plt.ylabel('Energy [GeV]')
        plt.show()

    # --- angle ---
    if not plots or 'angle' in plots:
        for current in currents:
            plt.plot(data['angle'][current], 'o', label=current)
            n = len(data['angle'][current])
        plt.plot([0, n-1], [-f.model_nominal_angle, ]*2, '--k', label='spec')
        plt.legend()
        plt.xlabel('Magnet index')
        plt.ylabel('Angle [deg]')
        plt.show()

    # --- angle error ---
    if not plots or 'dangle' in plots:
        for current in currents:
            plt.plot(data['dangle'][current], 'o', label=current)
            n = len(data['dangle'][current])
        plt.plot([0, n-1], [-0.05, -0.05], '--k', label='spec')
        plt.plot([0, n-1], [+0.05, +0.05], '--k')
        plt.legend()
        plt.xlabel('Magnet index')
        plt.ylabel('Angle Deviation from Average for each Current[%]')
        plt.show()

    # --- quadrupolar error ---
    if not plots or 'quad' in plots:
        nominal_KL = hall.defaults['si-dipoles-b1']['model_nominal_KL']
        nominal_GL = dict()
        for current in currents:
            energy = np.mean(data['energy'][current])
            brho, *_ = mp.beam_optics.beam_rigidity(energy=energy)
            nominal_GL = -nominal_KL * brho
            GL = data['quad_normal'][current]
            # print(energy, brho, nominal_KL, nominal_GL, GL)
            v = 100*(GL - nominal_GL)/nominal_GL
            print('current:{}, avg_quad_error:{:f}'.format(current,
                                                           np.mean(v)))
            plt.plot(v, label=current)
            n = len(data['quad_normal'][current])
        plt.plot([0, n-1], [-0.1, -0.1], '--k', label='spec')
        plt.plot([0, n-1], [+0.1, +0.1], '--k')
        plt.xlabel('Magnet index')
        plt.ylabel('Quadrupolar Error [%]')
        plt.grid()
        plt.legend()
        plt.show()

    # --- reference point rx variation ---
    if not plots or 'refrx' in plots:
        s1 = ['ob', 'or', 'og', 'oy']
        s2 = ['sb', 'sr', 'sg', 'sy']
        for i in range(len(currents)):
            v = 1e3*np.array(data['refrxP'][currents[i]])
            plt.plot(v, s1[i], label=currents[i] + ' P')
            v = 1e3*np.array(data['refrxN'][currents[i]])
            plt.plot(v, s2[i], label=currents[i] + ' N')
        plt.legend(fontsize=20)
        plt.grid()
        plt.xlabel('Magnet Index', fontsize=20)
        plt.ylabel('Diff. between refpoint rx to nominal [um]', fontsize=20)
        plt.show()

def save_readme_files():
    """."""
    header = (
        'Sirius B1 Dipoles Integrated Principal Multipoles',
        '=================================================',
        '',
        'As calculated in SIDE-half Runge-Kutta trajectory,',
        ('defined by measured fieldmap with magnet excitated with current '
         'of CURRENT,'),
        'corresponding to nominal particle energy of ENERGY GeV.',
        '',
        ('  Dipole   |  Angle [°]   |  Dint [T.m]  |   Gint [T]   |  Sint '
         '[T/m]  |'),
        ('           |              |              |              '
         '|              |'))
    sfmt = ('|{0:^10s}| {1:^+12.5f} | {2:^+12.5f} | {3:^+12.5f} '
            '| {4:^+12.5f} |\n')

    magnets, currents, data = load_analysis_result_x0_8p285mm(False)

    for current in currents:
        for side in ('Zpositive', 'Znegative'):
            with open('README-' + current + '-' + side + '.md', 'w') as fp:
                # header
                for line in header:
                    line = line.replace('CURRENT', current)
                    line = line.replace('SIDE', side)
                    line = line.replace('ENERGY', str(c2e_B1[current]))
                    fp.write(line + '\n')
                # data
                for i in range(len(magnets)):
                    magnet = magnets[i]
                    angle = data['angleP'][current][i] if \
                        side == 'Zpositive' else data['angleN'][current][i]
                    dip = data['dip_normalP'][current][i] if \
                        side == 'Zpositive' else \
                        data['dip_normalN'][current][i]
                    quad = data['quad_normalP'][current][i] if \
                        side == 'Zpositive' else \
                        data['quad_normalN'][current][i]
                    sext = data['sext_normalP'][current][i] if \
                        side == 'Zpositive' else \
                        data['sext_normalN'][current][i]
                    fp.write(sfmt.format(magnet, angle, dip, quad, sext))


def run():
    """."""
    # search_for_deflection_angle_B1()
    # load_search_deflection_angle_file('search-energies-shifted-x0.txt')
    # plot_results_search_deflection_angle_B1()
    # generate_inputs_B1()
    # seach_for_reference_point_B1()
    # load_search_reference_points_file()
    # plot_results_search_reference_points_B1()
    # generate_inputs_reference_point_B1()
    load_analysis_result('x0-8p365mm/', ('dangle', 'refrx', 'quad'))
    # load_search_reference_points_file_relaxed()
    # plot_results_search_reference_points_relaxed_B1()
    # save_readme_files()

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
