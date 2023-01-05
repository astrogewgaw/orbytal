"""
"""

import numpy as np


def fold(
    p: float,
    t: np.ndarray,
    x: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    return tuple(
        np.hsplit(
            np.asarray(
                [(ti, xi) for ti, xi in sorted(zip(((t - t.min()) % p) / p, x))]
            ),
            2,
        )
    )


def roughness():
    pass


def hodograph():
    pass


def refine():
    pass
