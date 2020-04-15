# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:34:03 2019

@author: dfure
"""

from matplotlib.pyplot import*
import string


#Créer une liste contenant l'alphabet
string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a= list(string.ascii_uppercase[0:26])
print(a)
print("Pour definir la matrice cle :")
nbc=int(input("Entrer le nombre de colonne(s) de la matrice cle : "))
nbl=int(input("Entrer le nombre de ligne(s) de la matrice cle : "))
 
mat = [ [0 for i in range(0,nbc)] for j in range(0,nbl)]
print mat
 
for i in range(nbl):
    for j in range(nbc):                
        mat[i][j]=int(input("Entrer le terme de la ligne "+str(i+1)+" et de la colonne "+str(j+1)+" : "))
        print(mat)
print("")
print(mat)

#Calcul le determinant de la matrice clé
det=(mat[0][0])*(mat[1][1])-(mat[0][1])*(mat[1][0])
print(det)

def pgcd(a,b):
   # """pgcd(a,b): calcul du 'Plus Grand Commun Diviseur' entre les 2 nombres entiers a et b"""
    if b==0:
        if a<0 :
            return -a
        else:
            return a
    else:
        r=a%b
        return pgcd(b,r)

c= pgcd(26,det)
print(c)
if pgcd(26,det) == 1:
    print("Le determinant est inversible dans Z/26 donc la matrice est inversible dans Z/26")
    print("La matrice peut donc etre utilisée comme cle")



print lettre1, lettre2

X=matrix([[b],[d]]) 
print(X)

Y=mat*X 
print(Y)
U=int(Y[0][0])%26
V=int(Y[1][0])%26
Z=([[U],[V]])   
print(Z) 
g=int(Z[0][0])
h=int(Z[1][0])
print a[g],a[h]

