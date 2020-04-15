#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 08:09:14 2019

@author: dfr2867a
"""

from numpy import*
import matplotlib.pyplot as plt
from pickle import *
import numpy as np
from scipy import optimize




#Question 4
fichier= open("data5.txt", "r")
x=load(fichier)
fichier.close()


NbNez= x.shape[0]
   
print 'Il y a',NbNez, ''
nbTotal = np.sum(x)
 

tab=[]
for i in range(len(x)) :
    tab.append(x[i][0])
    
for j in range(len(x)) :
    tab.append(x[j][0])
    
   

sumNez = np.sum(x)
print'Il y a ',sumNez, 'de longueur de nez total' 
moyenneNez = sumNez / NbNez
print'Le nez moyen est de',moyenneNez



moyenneNezCarre= moyenneNez*moyenneNez
xcarre = x*x
#Variance
variance = sum(xcarre)/x.shape[0] - moyenneNbHabcarre
print 'La variance de x est',variance

# Ecart type 
ecarttype= sqrt(variance)
print 'L''ecart-type de x est de',ecarttype

covariance=(sum(x))

    
tab=array(tab)
print x 
#droite de regression linéaire
t=arange(min(i)-1, max(j)+1,0.1)
axes = plt.axes()
axes.grid()
plt.scatter(i, j)
plot(t,f(t),'r')
plt.savefig("plot_simple_histogramme_matplotlib_03.png")

plt.show()

#a=0.2876...
#b=46.45...

