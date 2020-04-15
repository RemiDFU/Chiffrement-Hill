# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:09:50 2019

@author: dfure
"""

from tkinter import*


#Créer une fenetre

window1 = Tk()

#personnaliser cette fentre
window1.title("Hill")
window1.geometry("1080x720")
window1.minsize(480, 360 )
#window.iconbitmap("")
window1.config(background='#544B49')
              
              
#Créer la frame   
frame =Frame(window1, bg='#544B49')           
#Ajouter le titre

label_title = Label(frame, text="Bienvenue sur l'application de chiffrement de Hill", font=("Arial", 30), bg='#544B49', fg='white')
label_title.pack(expand=YES)

#Ajouter un second texte              

label_subtitle = Label(frame, text="Que voulez-vous faire ?", font=("Arial", 15), bg='#544B49', fg='white')
label_subtitle.pack(expand=YES)

#Ajouter un premier bouton
menu_button1 = Button(frame, text="Chiffrer un texte", font=("Arial", 15), bg='white', fg='#544B49')
menu_button1.pack()
#Ajouter 
frame.pack(expand=YES)
              
#Afficher

window1.mainloop()
