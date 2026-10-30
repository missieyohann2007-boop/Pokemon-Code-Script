from random import *
from Element_code import *
from Bonus_code import *
from Statu_code import *

# ----------------------- SYSTEME -----------------------
class Meteo():
    def __init__(self,name:str,element:str,effect:Statu_Change,bonus:Bonus,target:str,damage:int):
        self.Dmg = damage
        self.Ele = element
        self.Bonus = bonus

        self.Effect = effect
        self.Effect_target = target

        self.name = name

# -------------------------------------------- Meteo -------------------------------------------- Arena(name,element,effect,bonus,target,damage)
no_meteo = Meteo("...",no_type,no_statu_change,no_bonus,"all",0)

Degager = Meteo("le temps est degager.",Normal,no_statu_change,no_bonus,"all",0)
Plui = Meteo("La pluie tombe.",Eau,no_statu_change,no_bonus,"all",0)
Orage = Meteo("Le tonnerre grande.",Electrique,no_statu_change,no_bonus,"sky",0)
Chaleur = Meteo("La temperature monte.",Feu,no_statu_change,no_bonus,"all",0)
Sable = Meteo("Un nuage de sable envelope le terrain.",Terre,no_statu_change,no_bonus,"ground",1)
Vent = Meteo("Le vent souffle.",Vol,no_statu_change,no_bonus,"sky",0)
Neige = Meteo("La neige recouvre le terrain.",Glace,no_statu_change,no_bonus,"ground",0)
Grele = Meteo("La grele tombe.",Glace,no_statu_change,no_bonus,"sky",1)
Brouillard = Meteo("Le brouillard se leve.",Tenebre,no_statu_change,no_bonus,"sky",0)
Aleatoir = [Degager,Plui,Orage,Chaleur,Sable,Vent,Neige,Grele,Brouillard,no_meteo]
Aleatoir = Aleatoir[randint(0,len(Aleatoir)-1)]