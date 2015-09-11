# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:19:28 2015

@author: david
"""

import numpy as np

import healpy as hp

import matplotlib.pyplot as plt

from astropy.io import fits

get_ipython().magic(u'pinfo bin_llcl.bin_llcl'

import bin_llcl

l = np.arange(3072)

ll=l*(l+1)/(2*np.pi)

cl=hp.anafast(array1, map2=array2)

plt.figure()

bin_cl=bin_llcl.bin_llcl(ll*cl,25)

plt.plot(bin_cl['l_out'],bin_cl['llcl'],'.b')

plt.errorbar(bin_cl['l_out'],bin_cl['llcl'],bin_cl['std_llcl'],fmt='.r')
