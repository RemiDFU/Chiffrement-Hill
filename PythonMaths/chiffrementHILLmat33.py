from numpy import*
from matplotlib.pyplot import*
import string


#Créer une liste contenant l'alphabet
string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

a= list(string.ascii_uppercase[0:26])
print(a)

message=raw_input("Entrez le message a coder en MAJUSCULES :")
#Saisir une lettre de l'alphabet
i=0
tab=zeros((len(message)))
while i != len(message):
    i2=0
#Renvoie le positionnement (numéro) de la lettre de l'alphabet
    while (a[i2] != message[i] and i2<26 ):
        i2=i2+1
    b=i2
    tab[i]=b
    i=i+1
    
print tab

    
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
num1=(mat[0][0])*((mat[1][1])*(mat[2][2])-(mat[1][2])*(mat[2][1]))
print num1
num2=(mat[0][1])*((mat[1][0])*(mat[2][2])-(mat[1][2])*(mat[2][0]))
print num2
num3=(mat[0][2])*((mat[1][0])*(mat[2][1])-(mat[1][1])*(mat[2][0]))
print num3
det=num1-num2+num3
#Calcul le determinant de la matrice clé
#def det(matrice[2][2])
#    det=(mat[0][0])*(mat[1][1])-(mat[0][1])*(mat[1][0])
#def det2(matrice[3][3])
#    det=((mat[0],[0])*((mat[1][1])*(mat[2][2])-(mat[1][2])*(mat[2][1])))-((mat[0],[1])*((mat[1][0])*(mat[2][2])-(mat[1][2])*(mat[2][0])))+((mat[0],[2])*((mat[1][0])*(mat[2][1])-(mat[1][1])*(mat[2][0])))
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
tabdecode=[' ']*len(message)
i=0
while i<=len(message)/2:
    X=matrix([[tab[i]],[tab[i+1]]]) 
    Y=mat*X 
    U=int(Y[0][0])%26
    V=int(Y[1][0])%26
    Z=([[U],[V]])    
    g=int(Z[0][0])
    h=int(Z[1][0])
    tabdecode[i]=a[g]
    tabdecode[i+1]=a[h]
    i=i+2
print ("Voici le message " + message + " chiffre")
print tabdecode