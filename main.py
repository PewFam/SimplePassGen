import os
from colors import *


try:
        import pyperclip
        import datetime
        import time
        import keyboard
        import webbrowser
        import random
   
        import string
        import secrets

except ImportError:
        print(f'{color.FAIL}{style.BOLD}Un ou plusieurs modules nécessaires au fonctionnement du programme ne sont pas installé sur votre ordinateur. Voulez vous les télécharger ?{style.END}')
        quest = input('-->  Y/N\n')
        if quest == 'Y' or quest == 'y':
            os.system('pip install python-time')
            os.system('pip install pyperclip')
            os.system('pip install keyboard')
            os.system('pip install datetime')
        else :
            print(f'{color.PURPLE}Vous avez choisi de ne pas installer les modules nécessaires. Bonne journée !{style.END}') 
            input("presse n'importe quelle touche pour quitter")
            exit()

        import pyperclip
        import datetime
        import time
        import keyboard
        import webbrowser
        import random
 
        import string
        import secrets





def clear():
    os.system('cls')


clear()
print(f'Bievenue')
print(f"{color.BLUE}pressez 'alt+h' pour plus d'informations")
print(f"{color.PURPLE}pressez 'ctrl+alt+g' pour générer un mot de passe")
while True:
    if keyboard.is_pressed('alt+h'):
        webbrowser.open('https://pastebin.com/raw/bV0F1gw2')
        print('help')
        time.sleep(0.5)
    if keyboard.is_pressed('ctrl+alt+g'):
        import tkinter as tk
        from tkinter import messagebox
        wind = tk.Tk()
        greeting = tk.Label(text="Combien de caractères souhaitez-vous ?")
        inu = tk.Entry(text="")
        wind.geometry("400x300")
        def helloCallBack():
            try:
                int(inu.get())
                letters = string.ascii_letters
                digits = string.digits
                special_chars = string.punctuation
                alpha = letters + digits + special_chars 
                while True:
                    pwd = ''
                    for i in range(int(inu.get())):
                        pwd += ''.join(secrets.choice(alpha))

                    if (any(char in special_chars for char in pwd) and 
                        sum(char in digits for char in pwd)>=2):
                            break
                
                if int(inu.get()) >= 1800:
                    messagebox.showinfo("Erreur de valeur", "Veuillez entrer un nombre moins grand que 1800")
                    greeting.configure(text="Combien de caractères souhaitez-vous ?")
                    
                greeting.configure(text="Ok, je copie le mot de passe sécurisé à  " + inu.get() + " caractères !")
                pyperclip.copy(pwd)
                with open('log.txt', 'a') as f:
                    f.write(str(datetime.datetime.now()) +"            ->            "+ pwd +'\n\n')
            except ValueError:
                messagebox.showinfo("Erreur de valeur", "Veuillez entrer un nombre")
            except inu.get() == None:
                messagebox.showinfo("Erreur de valeur", "Veuillez entrer un nombre")
                greeting.configure(text="Combien de caractères souhaitez-vous ?")

        click = tk.Button(wind, text ="Valider", command = helloCallBack)
        greeting.pack()
        inu.pack()
        tk.Label(text='').pack()
        click.pack()
        wind.mainloop()
        time.sleep(0.5)
        
        
        