import numpy as np

class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note

    def __str__(self):
        return f"Nom: {self.nom}, Âge: {self.age}, Note: {self.note}"

class Classe:
    def __init__(self):
        self.liste_etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.liste_etudiants.append(etudiant)

    def afficher_tous_les_etudiants(self):
        for etudiant in self.liste_etudiants:
            print(etudiant)

    def calculer_moyenne(self):
        if not self.liste_etudiants:
            raise ValueError("Aucun étudiant dans la classe")
        notes = [etudiant.note for etudiant in self.liste_etudiants]
        return np.mean(notes)

    def filtrer_par_age(self, age):
        return [etudiant for etudiant in self.liste_etudiants if etudiant.age == age]

    def trier_par_note(self):
        self.liste_etudiants.sort(key=lambda etudiant: etudiant.note)

    def rechercher_etudiant(self, nom):
        for etudiant in self.liste_etudiants:
            if etudiant.nom == nom:
                return etudiant
        raise ValueError(f"Étudiant {nom} non trouvé")

    def __str__(self):
        return f"Classe avec {len(self.liste_etudiants)} étudiants"

#test de mon code:
    
classe = Classe()

# Ajout d'étudiants
classe.ajouter_etudiant(Etudiant("Tarek", 20, 85))
classe.ajouter_etudiant(Etudiant("Mohammed", 22, 78))
classe.ajouter_etudiant(Etudiant("Diego", 30, 92))
classe.ajouter_etudiant(Etudiant("David", 25, 68))

# Affichage de tous les étudiants
print("Affichage de tous les étudiants:")
classe.afficher_tous_les_etudiants()
print()

# Calcul de la moyenne de classe
try:
    moyenne = classe.calculer_moyenne()
    print(f"La moyenne de la classe est: {moyenne}")
except ValueError as e:
    print(e)
print()

# Filtrage des étudiants par âge (20 ans)
print("Filtrage des étudiants de 20 ans:")
etudiants_20_ans = classe.filtrer_par_age(20)
for etudiant in etudiants_20_ans:
    print(etudiant)
print()

# Tri des étudiants par note
classe.trier_par_note()
print("Étudiants triés par note:")
classe.afficher_tous_les_etudiants()
print()


# Recherche d'un étudiant par nom
try:
    etudiant_recherche = classe.rechercher_etudiant("Diego")
    print(f"Étudiant trouvé: {etudiant_recherche}")
except ValueError as e:
    print(e)
print()

