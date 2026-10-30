# ----------------------- SYSTEME -----------------------
class Element():
    def __init__(self,name:str,weak:list,strong:list,useless:list):
        self.name = name

        self.weakness = weak
        self.resistence = strong
        self.unvulnerability = useless

# ------------------------------ Element ------------------------------ Element(name,weak,strong,useless)
no_type = Element("...",[],[],[])

Normal = Element("Normal",["Terre","Acier"],["Inconnue"],["Phantom"])
Feu = Element("Feu",["Feu","Eau","Terre","Dragon"],["Plante","Glace","Insect","Acier"],["Inconnue"])
Eau = Element("Eau",["Eau","Plante","Dragon"],["Feu","Sol","Terre"],["Inconnue"])
Electrique = Element("Electrique",["Electrique","Plante","Dragon"],["Eau","Vol"],["Sol"])
Plante = Element("Plante",["Feu","Plante","Poison","Vol","Insect","Dragon"],["Eau","Sol","Terre"],["Inconnue"])
Glace = Element("Glace",["Feu","Eau","Glace","Acier"],["Plante","Sol","Vol"],["Inconnue"])
Combat = Element("Combat",["Poison","Vol","Psy","Insect"],["Normal","Glace","Terre","Tenebre","Acier"],["Phantom"])
Poison = Element("Poison",["Poison","Sol","Terre","Phantom"],["Plante"],["Acier"])
Sol = Element("Sol",["Plante","Insect"],["Feu","Electrique","Poison","Terre"],["Vol"])
Vol = Element("Vol",["Electrique","Terre","Acier"],["Plante","Combat","Insect"],["Inconnue"])
Psy = Element("Psy",["Psy","Acier"],["Combat","Poison"],["Inconnue"])
Insect = Element("Insect",["Feu","Combat","Poison","Vol","Phantom","Acier"],["Plante","Psy","Tenebre"],["Inconnue"])
Terre = Element("Terre",["Combat","Sol","Acier"],["Feu","Glace","Vol","Insect"],["Inconnue"])
Phantom = Element("Phantom",["Tenebre","Acier"],["Psy","Phantom"],["Normal"])
Dragon = Element("Dragon",["Acier"],["Dragon"],["Inconnue"])
Tenebre = Element("Tenebre",["Combat","Tenebre","Acier"],["Psy","Phantom"],["Inconnue"])
Acier = Element("Acier",["Feu","Eau","Electrique","Acier"],["Glace","Terre"],["Inconnue"])
Inconnue = Element("Inconnue",["Normal","Electrique","Combat","Poison","Sol","Psy","Phantom"],["Feu","Eau","Plante","Glace","Vol","Insect","Terre","Dragon","Tenebre","Acier"],["Inconnue"])
