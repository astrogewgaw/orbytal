import unyt as u
import numpy as np
from typing import Tuple

Array = np.ndarray
Quantity = u.unyt_quantity


def roughness(
    P: Array,
    MJD: Array,
    nPB: int = 1000,
    PBi: Quantity = 0.5 * u.hr,
    PBf: Quantity = 300 * u.day,
) -> Tuple[Array, Array]:

    """
    Calculate the roughness parameter, R.
    """

    Rs = []
    t = (MJD - MJD.min()) * u.day
    PBs = np.linspace(PBi, PBf, nPB)
    for PB in PBs:
        phz = (2 * np.pi * t) / PB
        phz = np.mod(phz, 2 * np.pi)
        Pf = [x for _, x in sorted(zip(phz, P))]
        R = np.sum(np.diff(Pf) ** 2)
        Rs.append(R)
    Rs = np.asarray(Rs)
    return PBs, Rs
