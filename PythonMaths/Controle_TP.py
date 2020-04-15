# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 20:41:37 2019

@author: dfure
"""
from pickle import load
from matplotlib.pyplot import hist,xlabel,ylabel,title,show,plot
from math import sqrt,log,pi
from numpy import power,exp,arange,sort



fichier= open("data5.txt", "r")
x=load(fichier)
fichier.close()

#faire deux liste pour chaque dimension du tableau
tab=[]
for i in range(len(x)) :
    tab.append(x[i][0])
    
for j in range(len(x)) :
    tab.append(x[j][0])
    

#Question 2
print 'Il y a',nbElement, 'Elements'
# Calcul de la moyenne à partir d'une liste et de son nombre d'élément
def calcul_moyenne(liste,nbElement):
    return sum(liste)/nbElement

# Calcul de l'écarType à partir d'une liste et de son nombre d'élément
def calcul_ecartType(liste,nbElement):
    listeCarre=[]
    for i in range(nbElement):
        listeCarre.append(liste[i]*liste[i])

    moyenne=calcul_moyenne(liste,nbElement)
    moyenneCarre=moyenne*moyenne
    
    ecartType=sqrt((sum(listeCarre)/nbElement)-moyenneCarre)
    
    return ecartType

# Calcul de la mediane à partir d'une liste et de son nombre d'élément    
def calcul_mediane(liste,nbElement):
    listeTrie=sort(liste,axis=0)
    if(nbElement%2 == 0):
        mediane=(listeTrie[nbElement/2]+listeTrie[(nbElement/2)+1])/2
    else:
        mediane=(listeTrie[(nbElement/2)+0.5])
        
    return mediane
    
# Calcul de la covariance à partir de deux listes et de leurs nombres d'éléments 
def calcul_covariance(liste1,liste2,longeurDesListes):
    
    xy=[]
    for i in range(longeurDesListes):
        xy.append(liste1[i]*liste2[i])
    
    moyenneListe1=calcul_moyenne(liste1,longeurDesListes)
    moyenneListe2=calcul_moyenne(liste2,longeurDesListes)
    
    covariance=(sum(xy)/longeurDesListes)-(moyenneListe1*moyenneListe2)
    
    return covariance

# Calcul du coefficient de regression linéaire à partir de la covariance et des l'ecarType de chacune des listes
def calucl_coefficient_regression_lineaire(covariance,ecartTypeListe1,ecartTypeListe2):
    r=covariance/(ecartTypeL*ecartTypeW)
    return r

# Droite de régression ou d'ajustement linéaire ou encore droite des moindre carrés cf chap2 page 12
# y=ax+b
    #a=cov(XY)/ecarTypeDeX**2
    #b=moyenneY - a * moyenneX
# Pour une valeur unique !!!
def droite_de_regression(valeur,covariance,ecartTypeListe1,moyenneListe1,moyenneListe2):
    a=covariance/ecartTypeListe1**2
    b=moyenneListe1-a*moyenneListe2
    return a*valeur+b

# Pour une valeur unique !!!
def gaussienne(valeur,moyenne,ecart_type):
    terme1=1/(sqrt(2*pi)*ecart_type)
    terme2=exp(-1* (power(valeur-moyenne,2) / ( 2*power(ecart_type,2) ) ))
    return terme1*terme2

def afficher_histogramme(liste):
    hist(liste)
    xlabel('Nom des x ')
    ylabel('Nom des y')
    title('Nom de l histogramme')
    show()
    
def afficher_nuage_de_points(liste1,liste2):
    scatter(liste1,liste1)
    xlabel('Nom des x ')
    ylabel('Nom des y')
    title('Nom de l histogramme')
    show()
    
def afficher_nuage_de_points_et_droite(liste1,liste2):
    t=arange(min(liste1)-1,max(liste2)+1,0.1)
    scatter(liste1,liste2)
    plot(t,droite_de_regression(t),'r')
    xlabel('Nom des x ')
    ylabel('Nom des y')
    title('Nom de l histogramme')
    show()
    
def afficher_histogramme_et_gaussienne(liste,moyenne,ecarType):
    t=arange(min(liste),max(liste),0.1)
    hist(liste,bins=50,normed=1)
    plot(t,gaussienne(t,moyenne,ecartType))
    show()
    
    


print calcul_moyenne(x,nbElement)
print calcul_ecartType(x,nbElement)
print calcul_mediane(x,nbElement)
print calcul_covariance(liste1,liste2,longeurDesListes)



    
    