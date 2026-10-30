from random import *
from Element_code import *
from Bonus_code import *
from Statu_code import *

# ----------------------- SYSTEME -----------------------
class Attack():
    def __init__(self,name:str,element:str,effect:Statu_Change,bonus:Bonus,target:str,damage:int,energie:int,accuracy:bool,type:str):
        self.Dmg = damage
        self.Energy_cost = energie
        self.Precision = accuracy

        self.Atk_Ele = element
        self.Effect = effect
        self.Bonus = bonus

        self.target = target
        self.name = name
        self.Type = type

# ------------------------------ ATTACK ------------------------------ Attack(name,element,effect,bonus,target,damage,energie,accuracy,type)
no_attack = Attack("...",no_type,[no_statu_change],no_bonus,"all",0,0,0,"phy")

Censored = Attack("[CENSORED]",Inconnue,[no_statu_change],no_bonus,"all",randint(1,200),randint(1,50),1,"phy")
Redacted = Attack("[REDACTED]",Inconnue,[no_statu_change],no_bonus,"all",randint(1,200),randint(1,50),1,"spe")

# Dragon
Ultre_lazer = Attack("Ultra lazer",Dragon,[no_statu_change],no_bonus,"ground",50,60,0.66,"spe")
Charge_draconique = Attack("Charge draconique",Dragon,[Confuse_self],no_bonus,"ground",70,30,0.66,"phy")

# Electrique
Boule_elect = Attack("Boule elect",Electrique,[Paralyze_other],no_bonus,"ground",20,25,0.8,"spe")
Tonnerre = Attack("Tonnerre",Electrique,[Paralyze_other],no_bonus,"sky",40,50,0.7,"spe")

# Acier
Queue_de_fer = Attack("Queue de fer",Acier,[no_statu_change],no_bonus,"ground",25,25,0.8,"phy")

# Normal
Vive_attack = Attack("Vive attack",Normal,[no_statu_change],no_bonus,"ground",15,25,0.6,"phy")
Tackle = Attack("Tackle",Normal,[no_statu_change],no_bonus,"ground",10,20,0.9,"phy")
Machouille = Attack("Machouille",Normal,[no_statu_change],no_bonus,"ground",15,20,0.9,"phy")

# Eau 
Bulle_eau = Attack("Bulle d'eau",Eau,[no_statu_change],no_bonus,"ground",25,40,0.9,"spe")
Jet_eau = Attack("Jet d'eau",Eau,[no_statu_change],no_bonus,"ground",30,30,0.9,"spe")

# Feu
Deflagration = Attack("Deflagration",Feu,[Burned_other],no_bonus,"ground",100,40,0.9,"spe")

# Plante
Balle_graine = Attack("Balle graine",Plante,[no_statu_change],no_bonus,"ground",20,10,0.9,"spe")
Fouet_liagne = Attack("Fouet liagne",Plante,[no_statu_change],no_bonus,"ground",50,20,0.9,"phy")