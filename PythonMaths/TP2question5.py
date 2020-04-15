#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:53:58 2019

@author: dfr2867a
"""

from numpy import*
import matplotlib.pyplot as plt
from pickle import *
import numpy as np
from scipy import optimize





#Question 5
fichier= open("data4.txt", "r")
x=load(fichier)
fichier.close()

nbAnnee = x.shape[0]

print 'Il y a',nbAnnee, ' enfants dans les quartiers de la ville de Denver dans le Colorado'
nbEnfant = np.sum(x)
print'Il y a ',nbEnfant, 'Enfants dans les quartier de Denver' 
minPop= np.min(x)
print 'La commune la moins peuplée a', minPop, 'habitant'
maxPop= np.max(x)
print 'Le quartier le plus peuplés d enfants a', maxPop, ''
moyenneNbHab = sum(x) / nbAnnee
print'La moyenne habitants par quartier à Denver est',moyenneNbHab


#médiane
t=sort(x, axis=0)
print t
mediane=(t[nbAnnee/2]+t[(nbAnnee/2)+1])/2
print "La médiane de la population des quartier de Denver est ",mediane



moyenneNbHabcarre= moyenneNbHab*moyenneNbHab
xcarre = x*x
#Variance
variance = sum(xcarre)/x.shape[0] - moyenneNbHabcarre
print 'La variance de x est',variance

# Ecart type 
ecarttype= sqrt(variance)
print 'L''ecart-type de x est de',ecarttype


#Histogramme 

hist(x) 
xlabel('effectif')
ylabel('nombres')
title('Question 5')
show()