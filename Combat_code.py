from random import *
from time import *
from Bonus_code import *
from Element_code import *
from Statu_code import *
from Attack_code import *
from Pokemon_code import *
from Meteo_code import *
from Object_code import *

# ----------------------- SYSTEME -----------------------
class Combat_sauvage():
    def __init__(self, Equipe_player:list, Poke_sauvage:list,Inventaire:list,Evenement:Meteo,Time:str,Nom:str):
        # Repertoir des variables
        self.Poke = 0
        self.Escape = False
        self.Catch = False
        self.Total_hp_player = 0
        self.Total_hp_auto = 0
        self.Equipe_auto = []

        self.Poke_combat = no_pokemon
        self.Poke_cible = no_pokemon

        self.Poke_1 = no_pokemon
        self.Reponse_1 = "Attaque"
        self.Action_1 = no_attack
        self.Cible_1 = no_pokemon
        self.Poke_2 = no_pokemon
        self.Reponse_2 = "Attaque"
        self.Action_2 = no_attack
        self.Cible_2 = no_pokemon
        self.Poke_3 = no_pokemon
        self.Reponse_3 = "Attaque"
        self.Action_3 = no_attack
        self.Cible_3 = no_pokemon
        self.Poke_4 = no_pokemon
        self.Reponse_4 = "Attaque"
        self.Action_4 = no_attack
        self.Cible_4 = no_pokemon

        self.Poke_attaquant = no_pokemon
        self.Poke_defenseur = no_pokemon
        self.Reponse = "Repos"
        self.Action = no_attack
        self.round = 0

        self.List_Poke = []
        self.List_Reponse = []
        self.List_Action = []
        self.List_Cible = []

        self.Equipe_auto = self.RNG(Poke_sauvage,Equipe_player)
        if self.Equipe_auto[0] != no_pokemon :
            self.Poke_combat = Equipe_player[0]
            self.Poke_combat.ia = "Player"
            print(f"{Nom} : Va si {self.Poke_combat.name} !")
            self.wait()
            for i in Equipe_player:
                self.Refresh(i)
            for i in self.Equipe_auto:
                self.Refresh(i)
            self.Total_hp_player = self.Calcul_Total_hp(Equipe_player)
            self.Total_hp_auto = self.Calcul_Total_hp(self.Equipe_auto)
            if Evenement != no_meteo:
                print(Evenement.name)
                self.wait()

            # Boucle de combat
            while self.Total_hp_player > 0 and self.Total_hp_auto > 0 and self.Escape == False and self.Catch == False : 

                while self.round == 0:

                    # ------------------------------------------------------------------------
                    #print("Equipe player [", end = " " )
                    #for i in Equipe_player :
                    #    print(i.name, end = " ")
                    #print("]")
                    #self.wait()
                    #print("Equipe enemy [", end = " " )
                    #for i in self.Equipe_auto :
                    #    print(i.name, end = " ")
                    #print("]")
                    #self.wait()
                    #-------------------------------------------------------------------------

                    self.Poke = self.Turn(self.Poke_combat,self.Equipe_auto)
                    self.Poke_1 = self.Poke[0]
                    self.Poke_2 = self.Poke[1]
                    self.Poke_3 = self.Poke[2]
                    self.Poke_4 = self.Poke[3]
                    self.List_Poke = [self.Poke_1,self.Poke_2,self.Poke_3,self.Poke_4]

                    # ------------------------------------------------------------------------
                    #print("Turn order [", end = " " )
                    #for i in self.List_Poke :
                    #    print(i.name,f"({i.ia})", end = " ")
                    #print("]")
                    #self.wait()
                    #-------------------------------------------------------------------------

                    self.Reponse_1 = self.Decision(self.Poke_1,self.Equipe_auto)
                    self.Reponse_2 = self.Decision(self.Poke_2,self.Equipe_auto)
                    self.Reponse_3 = self.Decision(self.Poke_3,self.Equipe_auto)
                    self.Reponse_4 = self.Decision(self.Poke_4,self.Equipe_auto)
                    self.List_Reponse = [self.Reponse_1,self.Reponse_2,self.Reponse_3,self.Reponse_4]

                    for i_1 in self.List_Reponse :
                        if i_1 == "Changement" or i_1 == "Info" or i_1 == "Objet":
                            self.Poke = self.List_Poke.pop(self.List_Reponse.index(i_1))
                            self.List_Poke.insert(0,self.Poke)
                            self.Poke = self.List_Reponse.pop(self.List_Reponse.index(i_1))
                            self.List_Reponse.insert(0,self.Poke)

                    # ------------------------------------------------------------------------
                    #print("Reponse [", end = " " )
                    #for i in self.List_Reponse :
                    #    print(i, end = " ")
                    #print("]")
                    #self.wait()
                    #-------------------------------------------------------------------------

                    self.Action_1 = no_attack
                    self.Action_2 = no_attack
                    self.Action_3 = no_attack
                    self.Action_4 = no_attack
                    self.List_Action = [self.Action_1,self.Action_2,self.Action_3,self.Action_4]
                    self.Cible_1 = no_pokemon
                    self.Cible_2 = no_pokemon
                    self.Cible_3 = no_pokemon
                    self.Cible_4 = no_pokemon
                    self.List_Cible = [self.Cible_1,self.Cible_2,self.Cible_3,self.Cible_4]

                    I = 0
                    while I < 4:
                        if self.List_Reponse[I] == "Attaque":
                            if I == 0:
                                self.Poke = self.Attack(self.List_Poke[I],self.Equipe_auto,self.Poke_combat)
                                self.Action_1 = self.Poke[0]
                                self.Cible_1 = self.Poke[1]
                            elif I == 1:
                                self.Poke = self.Attack(self.List_Poke[I],self.Equipe_auto,self.Poke_combat)
                                self.Action_2 = self.Poke[0]
                                self.Cible_2 = self.Poke[1]
                            elif I == 2:
                                self.Poke = self.Attack(self.List_Poke[I],self.Equipe_auto,self.Poke_combat)
                                self.Action_3 = self.Poke[0]
                                self.Cible_3 = self.Poke[1]
                            elif I == 3:
                                self.Poke = self.Attack(self.List_Poke[I],self.Equipe_auto,self.Poke_combat)
                                self.Action_4 = self.Poke[0]
                                self.Cible_4 = self.Poke[1]
                        elif self.List_Reponse[I] == "Objet":
                            if I == 0:
                                self.Action_1 = self.Objet(self.List_Poke[I],Inventaire)
                            elif I == 1:
                                self.Action_2 = self.Objet(self.List_Poke[I],Inventaire)
                            elif I == 2:
                                self.Action_3 = self.Objet(self.List_Poke[I],Inventaire)
                            elif I == 3:
                                self.Action_4 = self.Objet(self.List_Poke[I],Inventaire)
                        elif self.List_Reponse[I] == "Info":
                            if I == 0:
                                self.Action_1 = self.Info(self.List_Poke[I],self.Equipe_auto)
                            elif I == 1:
                                self.Action_2 = self.Info(self.List_Poke[I],self.Equipe_auto)
                            elif I == 2:
                                self.Action_3 = self.Info(self.List_Poke[I],self.Equipe_auto)
                            elif I == 3:
                                self.Action_4 = self.Info(self.List_Poke[I],self.Equipe_auto)
                        I += 1
                    self.List_Action = [self.Action_1,self.Action_2,self.Action_3,self.Action_4]
                    self.List_Cible = [self.Cible_1,self.Cible_2,self.Cible_3,self.Cible_4]

                    # ------------------------------------------------------------------------
                    #print("Action [", end = " " )
                    #for i in self.List_Action :
                    #    if i != "Retour":
                    #        print(i.name, end = " ")
                    #    else :
                    #        print("Retour", end = " ")
                    #print("]")
                    #self.wait()
                    #-------------------------------------------------------------------------
                    
                    self.Poke_attaquant = self.List_Poke[0]
                    self.Reponse = self.List_Reponse[0]
                    self.Action = self.List_Action[0]
                    self.Poke_defenseur = self.List_Cible[0]

                    # ------------------------------------------------------------------------
                    #print("Poke attaquant [", self.Poke_attaquant.name,f"({self.Poke_attaquant.ia})","]")
                    #self.wait()
                    #print("Poke defenceur [", self.Poke_defenseur.name,f"({self.Poke_defenseur.ia})","]")
                    #self.wait()
                    #-------------------------------------------------------------------------
       
                    self.round = 1
                    for i_2 in self.Equipe_auto:
                        if i_2.hp > 0:
                            self.round += 1
                    for i_3 in self.List_Action :
                        if i_3 == "Retour":
                            self.round = 0
                    if self.round != 0:
                        input("...")

                while self.round > 0 and self.Escape == False and self.Catch == False :

                    if self.Reponse == "Attaque" :
                        if self.Poke_attaquant != no_pokemon and self.Poke_attaquant.hp > 0:
                            self.CM_total = self.CM(self.Poke_attaquant,self.Poke_defenseur,self.Action,Evenement,Nom)
                            input("...")
                            self.wait()
                            if self.CM_total != 0:
                                self.CM_total = self.Efficacité(self.Poke_defenseur,self.Action,self.CM_total)
                                self.Calcul_degat(self.Poke_attaquant,self.Poke_defenseur,self.Action,self.CM_total)
                                input("...")
                                self.wait()
                
                    elif self.Reponse == "Objet":
                        if self.Poke_attaquant != no_pokemon and self.Poke_attaquant.hp > 0:
                            self.Action = no_attack
                            input("...")
                            self.wait()
            
                    elif self.Reponse == "Fuite":  
                        if self.Poke_attaquant != no_pokemon and self.Poke_attaquant.hp > 0:
                            self.Escape = self.Fuite(self.Poke_attaquant, self.Poke_defenseur,self.Equipe_auto)
                            input("...")
                            self.wait()

                    elif self.Reponse == "Changement":
                        if self.Poke_attaquant != no_pokemon :
                            self.Poke = self.Poke_attaquant
                            self.Poke_attaquant = self.Changement(self.Poke_attaquant,Equipe_player,self.List_Poke,Nom)
                            self.Poke_combat = self.Poke_attaquant
                            for i in self.List_Cible:
                                if i == self.Poke:
                                    i = self.Poke_attaquant
                            input("...")
                            self.wait()

                    elif self.Reponse == "Repos":
                        if self.Poke_attaquant != no_pokemon and self.Poke_attaquant.hp > 0:
                            self.Repos(self.Poke_attaquant)
                            input("...")
                            self.wait()

                    elif self.Reponse == "Info":
                        if self.Poke_attaquant != no_pokemon and self.Poke_attaquant.hp > 0:
                            self.Description(self.Action)
                            input("...")
                            self.wait()

                    self.statu_effect(self.Poke_attaquant,self.Poke_defenseur)
                    self.Poke = self.Boucle_de_combat(self.Poke_attaquant,self.List_Poke,self.List_Reponse,self.List_Action,self.List_Cible)
                    self.Poke_attaquant = self.Poke[0]
                    self.Reponse = self.Poke[1]
                    self.Action = self.Poke[2]
                    self.Poke_defenseur = self.Poke[3]
                    self.round -= 1

                    # ------------------------------------------------------------------------
                    #print("Poke attaquant [", self.Poke_attaquant.name,f"({self.Poke_attaquant.ia})","]")
                    #self.wait()
                    #print("Poke defenceur [", self.Poke_defenseur.name,f"({self.Poke_defenseur.ia})","]")
                    #self.wait()
                    #-------------------------------------------------------------------------

                self.Mort(Equipe_player,self.Equipe_auto,self.List_Poke)
                self.Arena_effect(Evenement,self.Poke_1,self.Poke_2,self.Poke_3,self.Poke_4)
                self.statu_effect(self.Poke_attaquant,self.Poke_defenseur)
                self.Mort(Equipe_player,self.Equipe_auto,self.List_Poke)
                self.Total_hp_player = self.Calcul_Total_hp(Equipe_player)
                self.Total_hp_auto = self.Calcul_Total_hp(self.Equipe_auto)
                if self.Total_hp_player > 0 :
                    self.Poke = True
                    for i_1 in self.List_Poke:
                        if i_1.hp > 0 and i_1.ia == "PLayer":
                            self.Poke = True
                    if self.Poke == False :
                        self.Poke_attaquant = self.Changement(self.Poke_attaquant,Equipe_player,self.List_Poke,Nom)
                        self.Poke_combat = self.Poke_attaquant
                        
            self.Fin(self.Poke_1,self.Poke_2,self.Total_hp_player,Equipe_player)

    # ----------------------------------------------------------------FONCTION----------------------------------------------------------------
    def wait (self):
        T = time() + 1
        T2 = time()
        while T2 < T :
            T2 = time()
        print( )

    def mini_wait (self):
        T = time() + 0.5
        T2 = time()
        while T2 < T :
            T2 = time()

    def Refresh (self,Poke:Pokemon): 
        if Poke.ia != "Player" :
            Poke.hp = Poke.max_hp
            Poke.energy = Poke.max_energy

        Poke.atk_phy = Poke.max_atk_phy
        Poke.def_phy = Poke.max_def_phy
        Poke.atk_spe = Poke.max_atk_spe
        Poke.def_spe = Poke.max_def_spe
        Poke.sped = Poke.max_sped
        Poke.precision = 1
        Poke.statu = []

    def Decision (self,Poke:Pokemon,Equipe_2:list):
        valid = False
        if Poke.ia == "Player" :
            while valid == False :
                print("[    MENU    ]")
                self.wait()
                print(f"[{Poke.name}]({Poke.hp}/{Poke.max_hp})   VS   ", end = " ")
                for i in Equipe_2:
                    if i != no_pokemon:
                        print(f"[{i.name}]({i.hp}/{i.max_hp})", end = " ")
                print(" ")
                print( )
                print("[Attaque] [Objet] [Fuite] [Changement] [Info] [Repos]")
                self.mini_wait()
                reponse = input("ACTION : ")
                self.wait()
                if reponse == "Attaque" or reponse == "Objet" or reponse == "Fuite" or reponse == "Changement" or reponse == "Info" or reponse == "Repos":
                    valid = True
        elif Poke.ia == "auto_1" and Poke != no_pokemon:
            if Poke.energy > 0:
                a = random()
                if Poke.max_hp*0.66 < Poke.hp > Poke.max_hp*0.33:
                    if 0 < a < 0.8 :
                        reponse = "Attaque"
                    elif 0.8 < a < 0.90 :
                        reponse = "Fuite"
                    elif 0.90 < a < 1 :
                        reponse = "Repos"
                elif Poke.max_hp*0.66 > Poke.hp > Poke.max_hp*0.33 :
                    if 0 < a < 0.6 :
                        reponse = "Attaque"
                    elif 0.6 < a < 0.8 :
                        reponse = "Fuite"
                    elif 0.8 < a < 1 :
                        reponse = "Repos"
                else :
                    if 0 < a < 0.4 :
                        reponse = "Attaque"
                    elif 0.4 < a < 0.9 :
                        reponse = "Fuite"
                    elif 0.9 < a < 1 :
                        reponse = "Repos"
            else :
                reponse = "Repos"
        else :
            reponse = "Repos"

        return reponse

    def Attack (self,Poke:Pokemon,List_Equipe_auto:list,Poke_combat:Pokemon):
        action = False
        cible = False
        if Poke.ia == "Player":
            print(f"Qu'es ce que {Poke.name} va faire ?")
            self.wait()
            while action == False or cible == False:
                while action == False:
                    print("[    CAPACITE   ]")
                    self.wait()
                    print(f"    [{Poke.energy}/{Poke.max_energy}]")
                    print()
                    print(f"[{Poke.Capacity_1.name}]({Poke.Capacity_1.Energy_cost}) [{Poke.Capacity_2.name}]({Poke.Capacity_2.Energy_cost}) [{Poke.Capacity_3.name}]({Poke.Capacity_3.Energy_cost}) [{Poke.Capacity_4.name}]({Poke.Capacity_4.Energy_cost}) [Retour]")    
                    self.mini_wait()
                    I = input("ATTAQUE : ")
                    self.wait()
                    if I == Poke.Capacity_1.name :
                        action = Poke.Capacity_1
                    elif I == Poke.Capacity_2.name:
                        action = Poke.Capacity_2
                    elif I == Poke.Capacity_3.name:
                        action = Poke.Capacity_3
                    elif I == Poke.Capacity_4.name:
                        action = Poke.Capacity_4
                    elif I == "Retour" :
                        action = I
                        cible = no_pokemon
                    else:
                        action = False
                        print(f"{Poke.name} ne connait pas cette competence")
                        self.wait()
                    if action == Poke.Capacity_1 or action == Poke.Capacity_2 or action == Poke.Capacity_3 or action == Poke.Capacity_4 :
                        if Poke.energy < action.Energy_cost:
                            action = False
                            print(f"{Poke.name} ne peut pas utiliser cette attaque")
                            self.wait()
                        else :
                            Poke.energy -= action.Energy_cost
                while cible == False and action != False and action != "Retour":
                    print("[    POKEMON   ]")
                    self.wait()
                    for i_1 in List_Equipe_auto:
                        if i_1 != no_pokemon:
                            print(f"[{i_1.name}]({i_1.hp}/{i_1.max_hp})", end=" ")   
                    print(f"[Retour]")
                    self.mini_wait()
                    I = input("CIBLE : ")
                    self.wait()
                    for i_2 in List_Equipe_auto :
                        if i_2.hp > 0 and i_2.name == I and i_2.name != no_pokemon.name :
                            cible = i_2
                        elif I == "Retour" :
                            cible = I
                    if cible == "Retour":
                        action = False
                        cible = False
            
        elif Poke.ia == "auto_1":
            while action == False :
                R = random()
                if R <= 0.25 :
                    action = Poke.Capacity_1
                elif R <= 0.50 and R> 0.25:
                    action = Poke.Capacity_2
                elif R <= 0.75 and R> 0.50:
                    action = Poke.Capacity_3
                else:
                    action = Poke.Capacity_4
            cible = Poke_combat

        return [action,cible]

    def Objet (self,Poke:Pokemon,Inventaire:list):
        action = False
        print(f"Que veut tu utiliser ?")
        self.wait()
        while action == False:
            print("[    SAC    ]")
            self.wait()
            for i in Inventaire:
                 if i.Obj_Use > 0:
                    print(f"[{i.name}]({i.Obj_Use})", end=" ") 
            print("[Retour]")
            self.mini_wait()
            I = input("Objet : ")
            print( )
            for i in Inventaire:
                if I == i.name and i.Obj_Use > 0 :
                    action = i
                    print(f"Tu utilise une {action.name} sur {Poke.name} .")
                    self.wait()
                elif I == "Retour" :
                    action = I
            if action == False and action != "Retour":
                print(f"Tu ne peut pas uttiliser cette objet.")
                self.wait()
            elif action != False and action != "Retour":
                action.Obj_Use -= 1
            
        return action

    def Fuite (self,Poke_atk:Pokemon,Poke_def:Pokemon,Equipe_auto:list):
        escape = False
        R = random()
        if Poke_atk.ia == "Player":
            if Poke_def.lv < Poke_atk.lv :
                if R < 0.66 :
                    escape = True
                    print(f"{Poke_atk.name} fuit le combat !")
                    self.wait()
                else :
                    escape = False
                    print(f"{Poke_atk.name} n'a pas reussi à fuir.")
                    self.wait()
            elif Poke_def.lv == Poke_atk.lv:
                if R < 0.50 :
                    escape = True
                    print(f"{Poke_atk.name} fuit le combat !")
                    self.wait()
                else :
                    escape = False
                    print(f"{Poke_atk.name} n'a pas reussi à fuir.")
                    self.wait()
            elif Poke_def.lv > Poke_atk.lv:
                if R < 0.33 :
                    escape = True
                    print(f"{Poke_atk.name} fuit le combat !")
                    self.wait()
                else :
                    escape = False
                    print(f"{Poke_atk.name} n'a pas reussi à fuir.")
                    self.wait()

        elif Poke_atk.ia != "Player":
            if Poke_atk.Rarity == "Commun":
                if R < 0.50 :
                    Equipe_auto.remove(Poke_atk)
                    Equipe_auto.append(no_pokemon)
                    escape = False
                    print(f"{Poke_atk.name} fuit le combat !")
                    self.wait()
                else :
                    escape = False
                    print(f"{Poke_atk.name} n'a pas reussi à fuir.")
                    self.wait()
            elif Poke_atk.Rarity == "Peu commun":
                if R < 0.66 :
                    Equipe_auto.remove(Poke_atk)
                    Equipe_auto.append(no_pokemon)
                    escape = False
                    print(f"{Poke_atk.name} fuit le combat !")
                    self.wait()
                else :
                    escape = False
                    print(f"{Poke_atk.name} n'a pas reussi à fuir.")
                    self.wait()
            elif Poke_atk.Rarity == "Rare":
                if R < 0.75 :
                    Equipe_auto.remove(Poke_atk)
                    Equipe_auto.append(no_pokemon)
                    escape = False
                    print(f"{Poke_atk.name} fuit le combat !")
                    self.wait()
                else :
                    escape = False
                    print(f"{Poke_atk.name} n'a pas reussi à fuir.")
                    self.wait()
            elif Poke_atk.Rarity == "legendaire":
                if R < 0.80 :
                    Equipe_auto.remove(Poke_atk)
                    Equipe_auto.append(no_pokemon)
                    escape = False
                    print(f"{Poke_atk.name} fuit le combat !")
                    self.wait()
                else :
                    escape = False
                    print(f"{Poke_atk.name} n'a pas reussi à fuir.")
                    self.wait()
            else :
                if R < 0.50 :
                    Equipe_auto.remove(Poke_atk)
                    Equipe_auto.append(no_pokemon)
                    escape = False
                    print(f"{Poke_atk.name} fuit le combat !")
                    self.wait()
                else :
                    escape = False
                    print(f"{Poke_atk.name} n'a pas reussi à fuir.")
                    self.wait()
            
        return escape

    def Repos (self,Poke_atk:Pokemon):
        R = random()
        Poke_atk.energy += round(Poke_atk.max_energy*0.5)
        if Poke_atk.energy > Poke_atk.max_energy:
            Poke_atk.energy = Poke_atk.max_energy
        print(f"{Poke_atk.name} a recuperer de  l'energie")
        self.wait()
        if R < 0.5:
            if len(Poke_atk.statu) > 0:
                I = randint(0,len(Poke_atk.statu)-1)
                self.wait()
                print(f"{Poke_atk.name} n'est plus {Poke_atk.statu[I]}")
                Poke_atk.statu.remove(Poke_atk.statu[I]) 

        for i in Poke_atk.statu :
            if i == "Fatigue" :
                self.wait()
                print(f"{Poke_atk.name} tombe de sommeil.")
                self.wait()
                Poke_atk.statu.remove("Fatigue")
                Poke_atk.statu.append("Endormie")

    def Info (self,Poke_2:Pokemon,list_Poke:list):
        valid = False
        while valid == False:
            print("[ POKEMON ]")
            self.wait()
            for i in list_Poke:
                if i != no_pokemon:
                    print(f"[{i.name}]", end=" ")   
            print(f"[{Poke_2.name}] [Retour]")
            self.mini_wait()
            I = input("identification : ")
            self.wait()
            if I == Poke_2.name :
                valid = True
                action = Poke_2
                return action
            elif I == "Retour":
                valid == True
                action = I
                return action
            else:
                for i in list_Poke:
                    if i.name == I and i != no_pokemon:
                        valid = True
                        action = i
                        return action
            if valid == False:
                print(f"[    Pokedex   ]")
                self.mini_wait()
                print("identification : [ERREUR]")
                self.wait()

    def RNG (self,Poke_sauvage,Equipe):
        Equipe_2 = [no_pokemon,no_pokemon,no_pokemon]
        Poke = 3
        Try = 5
        R1 = random()
        while Try > 0:
            R2 = randint(0,len(Poke_sauvage)-1)
            valid = True
            for i in Equipe:
                if i.specie == Poke_sauvage[R2].specie:
                    valid = False
            for i_2 in Equipe_2:
                if i_2.specie == Poke_sauvage[R2].specie:
                    valid = False
            if valid == True:
                Equipe_2.remove(no_pokemon)
                Equipe_2.insert(0,Poke_sauvage[R2])
                Poke -= 1
            Try -= 1
        if Poke == 3:
            print("il n'y a pas de pokemon ici.")
            self.wait()
            return Equipe_2
        else :
            for i_3 in Equipe_2:
                i_3.ia = "auto_1"

            if Poke == 2:
                Equipe_2.pop(1)
                Equipe_2.pop(1)
                Equipe_2.append(no_pokemon)
                Equipe_2.append(no_pokemon)
                print(f"Un {Equipe_2[0].name} sauvage appare !")
                self.wait()
            elif Poke == 1:
                if 0 < R1 <= 0.5:
                    Equipe_2.pop(1)
                    Equipe_2.pop(1)
                    Equipe_2.append(no_pokemon)
                    Equipe_2.append(no_pokemon)
                    print(f"Un {Equipe_2[0].name} sauvage appare !")
                    self.wait()
                elif  0.5 < R1 <= 1:
                    Equipe_2.pop(2)
                    Equipe_2.append(no_pokemon)
                    print(f"Un {Equipe_2[0].name} et un {Equipe_2[1].name} sauvages apparessent !")
                    self.wait()
            elif Poke == 0:
                if 0 < R1 <= 0.33:
                    Equipe_2.pop(1)
                    Equipe_2.pop(1)
                    Equipe_2.append(no_pokemon)
                    Equipe_2.append(no_pokemon)
                    print(f"Un {Equipe_2[0].name} sauvage appare !")
                    self.wait()
                elif  0.33 < R1 <= 0.66:
                    Equipe_2.pop(2)
                    Equipe_2.append(no_pokemon)
                    print(f"Un {Equipe_2[0].name} et un {Equipe_2[1].name} sauvages apparessent !")
                    self.wait()
                elif  0.66 < R1 <= 1:
                    print(f"Un {Equipe_2[0].name}, un {Equipe_2[1].name} et un {Equipe_2[2].name} sauvages apparessent !")
                    self.wait()

        return Equipe_2

    def Changement (self,Poke_atk:Pokemon,List_Poke_Good,List_Poke:list,Nom:str):
        valid = False
        R = random()
        print(f"{Nom} : Reviens {Poke_atk.name}")
        self.wait()
        for i in Poke_atk.statu:
            if i == "Piege":
                print(f"{Poke_atk.name} est coincer a cause du piege !")
                self.wait()
                valid = True
            if i == "Enerve":
                print(f"{Poke_atk.name} refuse le changement !")
                self.wait()
                valid = True
        if Poke_atk.love - 1 > R:
            print(f"{Poke_atk.name} veut combatre a vos cote.")
            self.wait()
            print(f"{Poke_atk.name} veut rester sur le terrain !")
            self.wait()
            valid_2 = False
            while valid_2 == False:
                print("[Oui] [Non]")
                reponse = input("Reponse : ")
                self.wait()
                if reponse == "Oui":
                    print(f"{Poke_atk.name} est content !")
                    valid_2 = True
                    valid = True
                    Poke_1.love += 0.2
                elif reponse == "Non":
                    valid_2 = True
                    print(f"{Poke_atk.name} est triste !")
                    self.wait()
                    Poke_1.love -= 0.1
                else :
                    valid_2 = False

        while valid == False :                
            print("[    EQUIPE    ]")
            self.wait()
            for i in List_Poke_Good:
                print(f"[{i.name}]({i.hp}/{i.max_hp})", end=" ")
            print("[Retour]")
            Poke_1 = input("POKEMON : ")
            self.wait()
            for i in List_Poke_Good :
                if i.hp > 0 and i.name == Poke_1 and i.name != no_pokemon.name :
                    valid = True
                    Poke_1 = i
                    Poke_1.ia = "Player"
                    List_Poke.insert(List_Poke.index(Poke_atk),Poke_1)
                    List_Poke.remove(Poke_atk)
            if valid == False:
                print("Tu ne peut pas envoyer ce Pokemon.")
                self.wait()
            elif valid == True :
                print(f"{Nom} : Je te choisi {Poke_1.name} !")
                self.wait()
        return Poke_1

    def Turn(self,Poke_combat:Pokemon,Equipe_auto:list):
        Poke = [Poke_combat,Equipe_auto[0],Equipe_auto[1],Equipe_auto[2]]
        for i_1 in Poke:
            A = len(Poke) - 1
            while A > -1:
                if i_1.sped == Poke[A].sped and Poke.index(i_1) != A:
                    Poke[A].sped += random()
                    i_1.sped += random()
                A -= 1

        for i_2 in Poke:
            while i_2.sped > Poke[Poke.index(i_2)- 1].sped and Poke.index(i_2) > 0:
                a = Poke.index(i_2)- 1
                Poke.remove(i_2)
                Poke.insert(a,i_2)

        A = len(Poke) - 1
        while A > -1:
            Poke[A].sped = int(Poke[A].sped)
            A -= 1
        
        return Poke
    
    def Boucle_de_combat (self,Poke:Pokemon,List_Poke:list,List_Reponse:list,List_Action:list,List_Cible:list):

        if List_Poke.index(Poke) == 3 :
            return [List_Poke[0],List_Reponse[0],List_Action[0],List_Cible[0]]
        else :
            return [List_Poke[List_Poke.index(Poke) + 1],List_Reponse[List_Poke.index(Poke) + 1],List_Action[List_Poke.index(Poke) + 1],List_Cible[List_Poke.index(Poke) + 1]]
    
    def CM (self,Poke_atk:Pokemon,Poke_def:Pokemon,Action:Attack,Terrain:Meteo,Nom:str):
        R = random()*255
        R2 = random()
        message = True
        CM = round(1 - random()*0.15)

        if Poke_atk.Poke_Ele_1.name == Action.Atk_Ele.name and message == True or Poke_atk.Poke_Ele_2.name == Action.Atk_Ele.name and message == True:
            CM = CM*1.5

        if Action.Atk_Ele.name == Terrain.Ele.name and message == True:
            CM = CM*1.5

        if Action.target != "all" and Poke_def.position != "ground" and Action.target != Poke_def.position and message == True:
            CM = 0
            print(f"{Poke_atk.name} ne peut pas atteindre {Poke_def.name} !")
            self.wait()
            message = False

        for i in Poke_atk.statu:

            if i == "Bruler" and Action.Type == "phy" and message == True:
                CM = CM*0.5
            if i == "Trempe" and Action.Type == "spe" and Action.Atk_Ele == Electrique and message == True:
                CM = CM*0.5
                if Action.Atk_Ele == Feu or Action.Atk_Ele == Electrique :
                    CM = 0
                    print("L'humidite l'empeche d'attaquer !")
                    message = False
                    self.wait()

            if i == "Gele" and Action.Atk_Ele != Feu and message == True:
                CM = 0
                print("Le gele l'empeche d'attaquer !")
                message = False
                self.wait()
            elif i == "Gele" and Action.Atk_Ele == Feu and message == True:
                Poke_atk.statu.remove("Gele")
                print(f"{Poke_atk.name} est degele !")
                self.wait()

            if i == "Endormie" and message == True :
                R = random()
                if R < 0.33:
                    Poke_atk.statu.remove("Endormie")
                    print(f"{Poke_atk.name} ce réveil !")
                    self.wait()
                else:
                    print(f"{Poke_atk.name} dort profondement !")
                    self.wait()

            if i == "Seduie" and message == True :
                R = random()
                if Poke_atk == "Male" and Poke_atk == "Female" or Poke_atk == "Female" and Poke_def == "Male" :
                    if R < 0.5 :
                        CM = 0
                        print(f"{Poke_atk.name} ne veut pas attacker !")
                        self.wait()
                else :
                    Poke_atk.statu.remove("Seduie")
                    print(f"{Poke_atk.name} ce resésie !")
                    self.wait()

            if i == "Paralyse" and message == True :
                R = random()
                if R < 0.25 :
                    CM = 0
                    print(f"{Poke_atk.name} est paralyse !")
                    self.wait()

            if i == "Apeure" and message == True :
                R = random()
                if R < 0.50 :
                    Poke_atk.statu.remove("Apeure")
                    print(f"{Poke_atk.name} n'a plus peur !")
                    self.wait()
                else :
                    CM = 0
                    print(f"{Poke_atk.name} tremble de peur !")
                    self.wait()

            if i == "Confu" and message == True:
                R = random()
                if R < 0.5 :
                    CM = 0
                    print(f"{Poke_atk.name} ce blaisse dans sa confusion !")
                    self.wait()
                    print(f"{Poke_atk.name} a pris {round((((Poke_atk.lv*0.4+2)*Poke_atk.atk_phy*40)/Poke_def.def_phy)/50+2)} de degat !")
                    self.wait()
                    Poke_atk.hp -= round((((Poke_atk.lv*0.4+2)*Poke_atk.atk_phy*40)/Poke_def.def_phy)/50+2)

            # a continuer

        if CM > 0 :
            print(f"{Poke_atk.name} utilise {Action.name} !")
            self.wait()
            if  Action.Precision*Poke_atk.precision < R2: 
                CM = 0
                print(f"{Poke_atk.name} rate.")
                self.wait()
            else:
                if round(Poke_atk.sped/2) > R:
                    CM = round(CM*((2*Poke_atk.lv + 5)/(Poke_atk.lv + 5)))
                    print("Coup critique !")
                    self.wait()
        return CM
    
    def Efficacité (self,Poke_def:Pokemon,Action:Attack,CM):
        efficacité = 1
        Atk_unvulnerability = Action.Atk_Ele.unvulnerability
        Atk_resistence = Action.Atk_Ele.resistence
        Atk_weakness = Action.Atk_Ele.weakness

        for i in Atk_unvulnerability:
            if Poke_def.Poke_Ele_1.name == i:
                efficacité = efficacité*0
            elif Poke_def.Poke_Ele_2.name == i:
                efficacité = efficacité*0
        for i in Atk_resistence:
            if Poke_def.Poke_Ele_1.name == i:
                efficacité = efficacité*2
            elif Poke_def.Poke_Ele_2.name == i:
                efficacité = efficacité*2
        for i in Atk_weakness:
            if Poke_def.Poke_Ele_1.name == i:
                efficacité = efficacité*0.5
            elif Poke_def.Poke_Ele_2.name == i:
                efficacité = efficacité*0.5

        if efficacité == 0.25:
            print("C'est n'est pas efficace.")
            self.wait()
        elif efficacité == 0.5:
            print("Ce n'est pas trés efficace.")
            self.wait()
        elif efficacité == 0:
            print("L'attaque n'a aucun effet.")
        elif efficacité == 2:
            print("C'est efficace.")
            self.wait()
        elif efficacité == 4:
            print("C'est trés efficace.")
            self.wait()

        return efficacité*CM

    def Calcul_degat(self,Poke_atk:Pokemon,Poke_def:Pokemon,Action:Attack,CM:bool):
        R = random()
        if Action.Type == "spe" :
            C = (((Poke_atk.lv*0.4+2)*Poke_atk.atk_spe*Action.Dmg)/Poke_def.def_spe)/50+2
        elif Action.Type == "phy" :
            C = (((Poke_atk.lv*0.4+2)*Poke_atk.atk_phy*Action.Dmg)/Poke_def.def_phy)/50+2
        Attack = round(C*CM)
        Poke_def.hp = round(Poke_def.hp - Attack)
        print(f"{Poke_def.name} a pris {Attack} point de dégat. Il lui reste {Poke_def.hp} point de vie !")
        self.wait()
        if Poke_def.hp < 0:
            Poke_def.hp = 0

        Poke_Ele = [Poke_atk.Poke_Ele_1,Poke_atk.Poke_Ele_2]
        for i_1 in Action.Effect:
            for i_2 in Poke_Ele :
                Resistence = False
                if i_1.Ele == i_2 :
                    Resistence = True
            if i_1 != no_statu_change and R < i_1.Probability :
                if i_1.Ele != no_type and Resistence == True :
                    print(f"{Poke_def.name} ne peut pas etre {i_1.name} .")
                    self.wait()
                elif i_1.Ele != no_type and Resistence == False :
                    if i_1.target == "other" :
                        Poke_def.statu.append(i_1.name)
                        print(f"{Poke_def.name} est {i_1.name} !")
                        self.wait()
                    elif i_1.target == "self" :
                        Poke_atk.statu.append(i_1.name)
                        print(f"{Poke_atk.name} est {i_1.name} !")
                        self.wait()
                    elif i_1.target == "all" :
                        Poke_atk.statu.append(i_1.name)
                        Poke_def.statu.append(i_1.name)
                        print(f"{Poke_atk.name} et {Poke_def.name} sont {i_1.name}s !")
                        self.wait()
                
    def Description(self,Poke:Pokemon):
        print(f"[    POKEDEX    ]")
        self.wait()
        print(f"Nom : {Poke.name}")
        self.mini_wait()
        if Poke.Poke_Ele_2 == no_type:
            print(f"Type : {Poke.Poke_Ele_1.name}")
        else :
            print(f"Type : {Poke.Poke_Ele_1.name} et {Poke.Poke_Ele_2.name}")
        self.mini_wait()
        print(f"Niveau : {Poke.lv}")
        self.mini_wait()
        print(f"Vie : {Poke.hp}/{Poke.max_hp}")
        self.mini_wait()
        print(f"Energie : {Poke.energy}/{Poke.max_energy}")
        self.mini_wait()
        print(f"Competence 1: {Poke.Capacity_1.name}({Poke.Capacity_1.Energy_cost})")
        self.mini_wait()
        print(f"Competence 2: {Poke.Capacity_2.name}({Poke.Capacity_2.Energy_cost})")
        self.mini_wait()
        print(f"Competence 3: {Poke.Capacity_3.name}({Poke.Capacity_3.Energy_cost})")
        self.mini_wait()
        print(f"Competence 4: {Poke.Capacity_4.name}({Poke.Capacity_4.Energy_cost})")
        self.mini_wait()
        print(f"Statue : ",end = " ")
        for i in Poke.statu:
            print(f"{i}", end =" ")
        print(" ")
        self.wait()

    def statu_effect (self,Poke_atk:Pokemon,Poke_def:Pokemon):
        if Poke_atk.hp > 1:
            for i in Poke_atk.statu:
                if i == "Regenere":
                    if Poke_atk.hp < Poke_atk.max_hp:
                        print(f"{Poke_atk.name} a recuperer {round(Poke_atk.max_hp/8)} de vie !")
                        self.wait()
                        Poke_atk.hp += round(Poke_atk.max_hp/8)
                        if Poke_atk.hp > Poke_atk.max_hp:
                            Poke_atk.hp = Poke_atk.max_hp
                if i == "Brule":
                    print(f"{Poke_atk.name} pert {round(Poke_atk.max_hp/16)} point de vie a cause des brulure !")
                    self.wait()
                    Poke_atk.hp -= round(Poke_atk.max_hp/16)
                    if Poke_atk.hp < 0:
                        Poke_atk.hp = 0
                if i == "Empoisonne":
                    print(f"{Poke_atk.name} pert {round(Poke_atk.max_hp/8)} point de vie a cause du  poison !")
                    self.wait()
                    Poke_atk.hp -= round(Poke_atk.max_hp/8)
                    if Poke_atk.hp < 0:
                        Poke_atk.hp = 0 
                if i == "Endormie":
                    R = random()
                    if R < 0.33:
                        Poke_atk.statu.remove("Endormie")
                        print(f"{Poke_atk.name} ce réveil !")
                        self.wait()

    def Arena_effect (self,Arena:Meteo,Poke_1:Pokemon,Poke_2:Pokemon,Poke_3:Pokemon,Poke_4:Pokemon):
        # introduire le effets d'arene
        a = 1

    def Calcul_Total_hp (self,List_Poke:list):
        Total_hp = 0
        for i in List_Poke:
            Total_hp += i.hp
        return Total_hp
    
    def Mort (self,Equipe_1:list,Equipe_2:list,List_Poke:list):
        for i in List_Poke:
            if 1 > i.hp and i.ia == "Player" and i != no_pokemon:
                R = random()
                if R > i.love :
                    print(f"{i.name} meurt !")
                    Equipe_1.remove(i)
                    self.wait()
                elif R <= i.love :
                    if i.love >= 1 and  0.5 > R:
                        valid = False
                        print("...")
                        self.wait()
                        print(f"{i.name} ne veut pas vous abondoner.")
                        self.wait()
                        print(f"{i.name} veut continuer le combat !")
                        self.wait()
                        while valid == False:
                            print("[Oui] [Non]")
                            reponse = input("Reponse : ")
                            self.wait()
                            if reponse == "Oui":
                                print(f"{i.name} se releve !")
                                valid = True
                                i.hp = 1
                                i.love -= 0.2
                                i.statu = []
                            elif reponse == "Non":
                                valid = True
                                print(f"{i.name} s'evanouit !")
                                self.wait()
                                i.love -= 0.1
                                i.statu = []
                            else :
                                valid = False
                    else :
                        print(f"{i.name} s'evanouit !")
                        self.wait()
                        i.love -= 0.1
                        i.statu = []
            elif 1 > i.hp and i.ia != "Player" and i != no_pokemon:
                if i.Rarity != "Legendaire":
                    print(f"{i.name} meurt !")
                    Equipe_2.remove(i)
                    List_Poke.remove(i)
                    List_Poke.append(no_pokemon)
                    Equipe_2.append(no_pokemon)
                    self.wait()
                else:
                    print(f"{i.name} s'échappe !")
                    Equipe_2.remove(i)
                    List_Poke.remove(i)
                    List_Poke.append(no_pokemon)
                    Equipe_2.append(no_pokemon)
                    self.wait()

    def Fin (self,Poke_1:Pokemon,Poke_2:Pokemon,Total_hp:int,List_Poke:list):
        if 1 > Total_hp:
            print("Vous avez perdue le combat !")
            for i in List_Poke:
                if i != no_pokemon:
                    i.love -= 0.1
            self.wait()
        elif 1 > Poke_2.hp and 0 < Total_hp:
            print("Vous avez gagner le combat !")
            self.wait()
            xp = round((Poke_2.max_hp*Poke_2.lv*1)/7)
            print(f"{Poke_1.name} gagne {xp} points d'exp.")
            Poke_1.xp += xp
            self.wait()
            for i in List_Poke:
                if i != no_pokemon and 0 < i.hp:
                    i.xp += round(xp/4)
                    i.love += 0.1
            print(f"Tout le monde gagne {round(xp/4)} points d'exp.")
            self.wait()
            for i in List_Poke:
                while i != no_pokemon and i.next_level_xp <= i.xp:
                    print(f"{i.name} mmonte au niveau {i.lv+1} .")
                    self.wait()
                    i.xp -= i.next_level_xp
                    i.lv += 1


