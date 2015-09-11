# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 12:09:05 2015

@author: david
"""

import numpy as np

import healpy as hp

from astropy.io import fits

import matplotlib.pyplot as plt

from IPython.utils.data import flatten

has=fits.open('/home/dweisberger/haslam_masked.fits')

ham=has[1].data.field(0)

flh=flatten(ham)

fha=np.array(flh)

Y = fha

free=fits.open('/home/dweisberger/freefree_mask.fits')

fre=free[1].data.field(0)

fra=flatten(fre)

ffa=np.array(fra)

Z = ffa

chip=fits.open('/home/dweisberger/chipass_masked.fits')

chi=chip[1].data.field(0)

chf=flatten(chi)

cfa=np.array(chf)

X = cfa

Xc = X.clip(0)

Yc = Y.clip(0)

Zc = Z.clip(0)

A = np.array([Yc, Zc, [1]*len(Xc)]).transpose()
a, b, mean = np.linalg.lstsq(A, Xc)[0]

b_array = np.linspace(0,.003,100)

rms_array = []

for d in b_array:
   r = Xc - 0.039857512377487227*Yc - d*Zc   
   rms= np.sqrt(np.mean(r**2)) 
   rms_array.append(rms)
   
   