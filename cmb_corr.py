# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:19:28 2015

@author: david
"""

import numpy as np

import healpy as hp

import matplotlib.pyplot as plt

from astropy.io import fits

#get_ipython().magic(u'pinfo bin_llcl.bin_llcl')

import bin_llcl

#cmb = hp.read_map('/data/Planck/COM_CompMap_CMB-smica_2048.fits')

cmb = hp.read_map('CMB_SMICA_mask.fits')

#cmbd = hp.ud_grade(cmb, nside_out=1024)

cmbd = cmb

hp.mollview(cmbd)

plt.show()

#chiminusfore = hp.read_map('total_masked_map.fits')

lemon = 1024

cl=hp.anafast(cmbd, lmax = lemon)

l = np.arange(len(cl))

ll=l*(l+1)/(2*np.pi)

plt.figure()

bin_cl=bin_llcl.bin_llcl(ll*cl,25)

plt.plot(bin_cl['l_out'],bin_cl['llcl'],'.b')

plt.errorbar(bin_cl['l_out'],bin_cl['llcl'],bin_cl['std_llcl']/5.,fmt='.r')

plt.show()