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

badvals = X == -1.6375e+30

Xc = hp.ma(X)

Xc.mask = badvals

Yc = hp.ma(Y)

Yc.mask = badvals

Zc = hp.ma(Z)

Zc.mask = badvals

#Xc = X.clip(0)

#Yc = Y.clip(0)

#Zc = Z.clip(0)

#a_array = np.linspace(0,.1,100)

#rms_array = []

Xd = Xc - np.mean(Xc)
 
Yd = Yc - np.mean(Yc)

Zd = Zc - np.mean(Zc) 

r = Xd - .04367*Yd - .0006496*Zd 
 
rms= np.sqrt(np.mean(r**2))

print(rms)
#for rms in rms_array:
   #r = Xc - a*Yc - .0065*Zc   
 #  rms= np.sqrt(np.mean(Xc**2)) 
  # rms_array.append(rms)
   
   