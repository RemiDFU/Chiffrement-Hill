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

#Calcul le determinant de la matrice clé
det=(mat[0][0])*(mat[1][1])-(mat[0][1])*(mat[1][0])
print(det)
matinv=np.linalg.inv(mat)
print mat2
tabdecode=[' ']*len(message)
i=0
while i<=len(message)/2:
    X=matrix([[tab[i]],[tab[i+1]]]) 
    Y=matinv*X 
    print Y
    U=int(Y[0][0])%26
    V=int(Y[1][0])%26
    Z=([[U],[V]])    
    g=int(Z[0][0])
    h=int(Z[1][0])
    print a[g]
    print a[h]
    tabdecode[i]=a[g]
    tabdecode[i+1]=a[h]
    i=i+2
print ("Voici le message " + message + " chiffre")
print tabdecode
