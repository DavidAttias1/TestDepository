# Le plus grand defi que j'ai rencontré etait de faire en sorte que la saisie soit active quand les boutons ->
# s'activent. Avec beaucoup de difficulté, j'ai reussi a faire en sorte que les boutons fonctionnent aussi sur le num2.
# J'ai eu aussi un peu de probleme a faire les factorielles, mais j'ai reussi a la fin.

import tkinter as tk
import math

# Code de l'événement on click
def calculer():
    try:
        num1 = float(edit_num1.get())  # récupérer le premier nombre saisi dans le champ edit_num1
        op = operator_var.get()  # récupérer l'opération de calcul à effectuer à partir de la variable operator_var
        
        # Effectuer le calcul en fonction de l'opération sélectionnée
        if op == "+":
            num2 = float(edit_num2.get())
            res = num1 + num2
        elif op == "-":
            num2 = float(edit_num2.get())
            res = num1 - num2
        elif op == "*":
            num2 = float(edit_num2.get())
            res = num1 * num2
        elif op == "**":
            num2 = float(edit_num2.get())
            res = num1 ** num2
        elif op == "n!":
            res = math.factorial(int(num1))
        elif op == "sqrt":
            res = math.sqrt(num1)
        elif op == "carre":
            res = num1 ** 2
        elif op == "/":
            num2 = float(edit_num2.get())
            if num2 != 0:
                res = num1 / num2
            else:
                res = "Erreur: division par zéro"
        else:
            res = "Opérateur non valide"
    except ValueError:
        res = "Entrée non valide"
    
    # Effacer le résultat
    edit_resultat.delete(0, tk.END)
    # Afficher le résultat dans le champ de saisie du résultat
    edit_resultat.insert(0, res)  # 0 indique que la position 0

def effacer():
    edit_resultat.delete(0, tk.END)
    edit_num1.delete(0, tk.END)
    edit_num2.delete(0, tk.END)

# Fonction pour ajouter les chiffres dans le champ de saisie actif
def ajouter_chiffre(chiffre):
    if current_entry.get() == 'num1':
        edit_num1.insert(tk.END, chiffre)
    elif current_entry.get() == 'num2':
        edit_num2.insert(tk.END, chiffre)

# Fonction pour mettre à jour le champ de saisie actif
def set_active_entry(entry_name):
    current_entry.set(entry_name)

# Création de la fenêtre principale
window = tk.Tk()
window.title("Calculatrice")
window.geometry("600x300")  # dimension de la fenêtre

# Variable pour suivre le champ de saisie actif
current_entry = tk.StringVar(window, "num1")

# Création des champs de saisie pour les nombres: Text Edit
label_num1 = tk.Label(window, text="Nombre 1:")
label_num1.pack()
edit_num1 = tk.Entry(window)  # création du champ de saisie du premier nombre
edit_num1.pack()  # placer le champ de saisie sur la fenêtre
edit_num1.bind("<FocusIn>", lambda event: set_active_entry('num1'))

label_num2 = tk.Label(window, text="Nombre 2:")
label_num2.pack()
edit_num2 = tk.Entry(window)  # création du champ de saisie du second nombre
edit_num2.pack()  # placer le champ de saisie sur la fenêtre
edit_num2.bind("<FocusIn>", lambda event: set_active_entry('num2'))

# Création d'un champ de saisie pour le résultat
label_res = tk.Label(window, text="Résultat:")
label_res.pack()
edit_resultat = tk.Entry(window)
edit_resultat.pack()

# Création des boutons pour les chiffres 0-9
frame_chiffres = tk.Frame(window)
frame_chiffres.pack()

for i in range(10):
    button_chiffre = tk.Button(frame_chiffres, text=str(i), command=lambda i=i: ajouter_chiffre(i))
    button_chiffre.grid(row=i // 5, column=i % 5)

# Création d'un bouton pour effectuer le calcul
button_calculer = tk.Button(window, text="Calculer", command=calculer)
button_calculer.pack()  # placer le bouton sur la fenêtre

# Création d'un bouton pour effacer
button_rase = tk.Button(window, text="Remise à zéro", command=effacer)
button_rase.pack()  # placer le bouton sur la fenêtre

# Création de boutons pour les opérateurs
operator_var = tk.StringVar(window)  # créer une variable StringVar pour suivre l'opérateur sélectionné
operator_var.set("+")  # opérateur par défaut

# Création des boutons pour les opérateurs 
frame_operateurs = tk.Frame(window)
frame_operateurs.pack()

button_add = tk.Button(frame_operateurs, text="+", command=lambda: operator_var.set("+"))
button_add.pack(side=tk.LEFT)  # ajouter le bouton plus dans la fenêtre

button_sub = tk.Button(frame_operateurs, text="-", command=lambda: operator_var.set("-"))
button_sub.pack(side=tk.LEFT)  # ajouter le bouton moins dans la fenêtre

button_mul = tk.Button(frame_operateurs, text="*", command=lambda: operator_var.set("*"))
button_mul.pack(side=tk.LEFT)  # ajouter le bouton multiplication dans la fenêtre

button_puissance = tk.Button(frame_operateurs, text="**", command=lambda: operator_var.set("**"))
button_puissance.pack(side=tk.LEFT)  # ajouter le bouton puissance dans la fenêtre

button_div = tk.Button(frame_operateurs, text="/", command=lambda: operator_var.set("/"))
button_div.pack(side=tk.LEFT)  # ajouter le bouton division dans la fenêtre

button_sqrt = tk.Button(frame_operateurs, text="sqrt", command=lambda: operator_var.set("sqrt"))
button_sqrt.pack(side=tk.LEFT)  # ajouter le bouton racine carrée dans la fenêtre

button_carre = tk.Button(frame_operateurs, text="carre", command=lambda: operator_var.set("carre"))
button_carre.pack(side=tk.LEFT)  # ajouter le bouton carré dans la fenêtre

button_factorielle = tk.Button(frame_operateurs, text="n!", command=lambda: operator_var.set("n!"))
button_factorielle.pack(side=tk.LEFT)  # ajouter le bouton factorielle dans la fenêtre

# Lancement d'une boucle principale pour lancer la fenêtre
window.mainloop()

