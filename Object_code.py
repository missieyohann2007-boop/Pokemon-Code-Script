from Bonus_code import *

# ----------------------- SYSTEME -----------------------
class Object():
    def __init__(self,name:str,bonus:str,utilisation:int):
        self.Obj_Use = utilisation

        self.Bonus = bonus
        self.name = name

# ---------------------------------------------- OBJECT ---------------------------------------------- Object(name,bonus,utilisation,)
Potion = Object("Potion",heal_self_1,1)
Grosse_potion =  Object("Potion",heal_self_2,1)

Huile = Object("Huie",energy_up_self_1,1)
Elixir = Object("Elixir",energy_up_self_2,1)

Rappel = Object("Rappel",revive_1,1)
Rappel_max = Object("Rappel Max",revive_2,1)

Pokeball = Object("Pokeball",catching_1,1)
Superball = Object("Pokeball",catching_2,1)
Hyperball = Object("Pokeball",catching_3,1)
Masterball = Object("Pokeball",catching_4,1)