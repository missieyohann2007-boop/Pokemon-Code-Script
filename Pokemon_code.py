from random import *
from Attack_code import *
from Element_code import *

# ----------------------- SYSTEME -----------------------
class Pokemon():
    def __init__(self,name_1:str,specie:str,evolution:Pokemon,evolution_stage:int,element_1:str,element_2:str,level:int,life:int,energy:int,speed:int,Comp1:Attack,Comp2:Attack,Comp3:Attack,Comp4:Attack,def_phy:int,atk_phy:int,def_spe:int,atk_spe:int,rarity:str,sexe:str,all_Comp:list):
        self.lv = level
        self.max_hp = life
        self.hp = life
        self.max_energy = energy
        self.energy = energy
        self.name = name_1
        self.evo_1 = evolution
        self.evo_stage = evolution_stage
        self.specie = specie
        self.sexe = sexe

        self.xp = 0
        self.next_level_xp = 10*self.lv
        self.next_evolution_xp = 15*self.evo_stage + randint(1,10)
        self.next_capacity_xp = 0
        self.precision = 1
        self.love = 0.5

        self.max_def_phy = round(def_phy+self.love*2+self.lv*0.8+self.evo_stage*5)
        self.max_atk_phy = round(atk_phy+self.love*2+self.lv*0.8+self.evo_stage*5)
        self.max_def_spe = round(def_spe+self.love*2+self.lv*0.8+self.evo_stage*5)
        self.max_atk_spe = round(atk_spe+self.love*2+self.lv*0.8+self.evo_stage*5)
        self.max_sped = round(speed+self.lv*0.5)

        self.def_phy = round(def_phy+self.love*2+self.lv*0.8+self.evo_stage*5)
        self.atk_phy = round(atk_phy+self.love*2+self.lv*0.8+self.evo_stage*5)
        self.def_spe = round(def_spe+self.love*2+self.lv*0.8+self.evo_stage*5)
        self.atk_spe = round(atk_spe+self.love*2+self.lv*0.8+self.evo_stage*5)
        self.sped = round(speed+self.lv*0.5)

        self.Poke_Ele_1 = element_1
        self.Poke_Ele_2 = element_2
        self.Rarity = rarity

        self.Capacity_1 = Comp1
        self.Capacity_2 = Comp2
        self.Capacity_3 = Comp3
        self.Capacity_4 = Comp4

        self.All_capacity = all_Comp
        self.statu = []
        self.position = "ground"
        self.ia = "auto_1"

# ------------ POKEMON ------------ Pokemeon(name_1,specie,evolution,evolution_stage,element_1,element_2,level,life,speed,Comp1,Comp2,Comp3,Comp4,def_phy,atk_phy,def_spe,atk_spe,rarity,all_Comp)
no_pokemon = Pokemon("...","...","...",1,no_type,no_type,0,0,0,0,no_attack,no_attack,no_attack,no_attack,0,0,0,0,"Inconnue",["Asexue"],[])

#Inconnue
Missingno = Pokemon("Missingno","Missingno",no_pokemon,1,Inconnue,Inconnue,randint(1,100),randint(1,200),randint(1,200),randint(1,200),Censored,Redacted,Censored,Redacted,randint(1,200),randint(1,200),randint(1,200),randint(1,200),"Asexue","Inconnue",[])

# Legendaire
Rayquaza = Pokemon("Rayquaza","Rayquaza",no_pokemon,1,Dragon,Vol,100,120,100,1,Ultre_lazer,Charge_draconique,Tackle,Machouille,100,50,150,200,"legendaire","Inconnue",[])

# Peu commun
Florizarre = Pokemon("Florizarre","Bulbizarre",no_pokemon,3,Plante,Poison,5,80,100,120,no_attack,no_attack,no_attack,no_attack,110,70,200,180,"Peu commun",["Male","Female"],[])
Herbizarre = Pokemon("Herbizarre","Bulbizarre",Florizarre,2,Plante,Poison,5,80,100,120,no_attack,no_attack,no_attack,no_attack,110,70,200,180,"Peu commun",["Male","Female"],[])
Bulbizarre = Pokemon("Bulbizarre","Bulbizarre",Herbizarre,1,Plante,Poison,5,80,100,120,Fouet_liagne,Balle_graine,Tackle,Vive_attack,110,70,200,180,"Peu commun",["Male","Female"],[])

Dracaufeu = Pokemon("Dracaufeu","Salameche",no_pokemon,3,Feu,Vol,5,60,100,130,no_attack,no_attack,no_attack,no_attack,110,70,200,180,"Peu commun",["Male","Female"],[])
Reptincel = Pokemon("Reptincel","Salameche",Dracaufeu,2,Feu,no_type,5,60,100,130,no_attack,no_attack,no_attack,no_attack,110,70,200,180,"Peu commun",["Male","Female"],[])
Salameche = Pokemon("Salameche","Salameche",Reptincel,1,Feu,no_type,5,60,100,130,Machouille,Deflagration,Vive_attack,Tackle,110,70,200,180,"Peu commun",["Male","Female"],[])

Tortank = Pokemon("Tortank","Carapuce",no_pokemon,3,Eau,no_type,5,90,100,110,no_attack,no_attack,no_attack,no_attack,175,100,150,125,"Peu commun",["Male","Female"],[])
Carabaffe = Pokemon("Carabaffe","Carapuce",Tortank,2,Eau,no_type,5,90,100,110,no_attack,no_attack,no_attack,no_attack,175,100,150,125,"Peu commun",["Male","Female"],[])
Carapuce = Pokemon("Carapuce","Carapuce",Carabaffe,1,Eau,no_type,5,90,100,110,Bulle_eau,Tackle,Machouille,Vive_attack,175,100,150,125,"Peu commun",["Male","Female"],[])

Raichu = Pokemon("Raichu","Pikachu",no_pokemon,2,Electrique,no_type,5,70,100,160,no_attack,no_attack,no_attack,no_attack,25,10,100,200,"Peu commun",["Male","Female"],[])
Pikachu = Pokemon("Pikachu","Pikachu",Raichu,1,Electrique,no_type,5,70,100,160,Boule_elect,Vive_attack,Queue_de_fer,Tonnerre,25,10,100,200,"Peu commun",["Male","Female"],[])