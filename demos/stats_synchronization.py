#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""This demo shows show to calculate synchronization of an auditory
model at different characteristic frequencies.

"""

from __future__ import division, absolute_import, print_function

__author__ = "Marek Rudnicki"

import numpy as np
import matplotlib.pyplot as plt

import cochlea
from cochlea.stats import calc_synchronization


def main():

    # sis = calc_synchronization(
    #     model=cochlea.run_holmberg2007,
    #     cfs=cochlea.holmberg2007.real_freq_map[10::5],
    #     model_pars={'fs': 48e3}
    # )

    sis = calc_synchronization(
        model=cochlea.run_zilany2013,
        model_pars={'species': 'human'}
    )

    print(sis)

    hsr_sis = sis.pivot(index='dbspl', columns='cf', values='hsr')

    fig,ax = plt.subplots(2,1)

    ax[0].imshow(hsr_sis, aspect='auto', interpolation='nearest')
    hsr_sis.max().plot(ax=ax[1], logx=True)

    plt.show()

if __name__ == "__main__":
    main()
