#!/usr/bin/env python-sirius

"""Generate SI dipole excitation file."""

import math
import numpy as np
import mathphys as mp


# --- measured currents and fitted energies for nominal deflections.
currents = np.array([381.7, 401.8, 403.6, 421.9, ])
energies = np.array([2.84308943902439, 2.990614,
                     3.003809843074398, 3.137824707317073, ])


def get_poly_function():
    """."""
    z = np.polyfit(currents, energies, 2)
    p = np.poly1d(z)
    return p


def conv_curr2energy(current):
    """."""
    pfit = get_poly_function()
    return pfit(current)


I_3GeV = 403.08027705705274
E_3GeV = conv_curr2energy(I_3GeV)
print(I_3GeV)
print(E_3GeV)
