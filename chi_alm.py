# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 03:22:55 2015

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

badvals = X == -1.6375e+30

Xc = hp.ma(X)

Xc.mask = badvals

Yc = hp.ma(Y)

Yc.mask = badvals

Zc = hp.ma(Z)

Zc.mask = badvals

Xd = Xc - np.mean(Xc)
 
Yd = Yc - np.mean(Yc)

Zd = Zc - np.mean(Zc) 

almX = hp.map2alm(Xd)

almY = hp.map2alm(Yd)

almZ = hp.map2alm(Zd)

almXc = np.array(almX)

almXc[0:20301] = 0 

almYc = np.array(almY)

almYc[0:20301] = 0 

almZc = np.array(almZ)

almZc[0:20301] = 0 

A = np.array([almYc, almZc]).transpose()
a, b = np.linalg.lstsq(A, almXc)[0]

print(a,b)