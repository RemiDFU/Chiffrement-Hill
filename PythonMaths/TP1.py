# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

from numpy import*
from matplotlib.pyplot import *



#Script

a=array([1,2,3])
type(a)
print(a)
a.shape
print(a.shape)
b= array([[1,2],[8,13]])
print(b)
b.shape
print(b.shape)

c=array([[1],[2],[3]])
print(c)
print(c.shape)

a=zeros((5,4))
print(a)

b=ones((2,3))
print(b)
(n,m)= b.shape
print(b.shape)