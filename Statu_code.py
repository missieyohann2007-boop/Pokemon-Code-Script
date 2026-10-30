from Element_code import *

# ----------------------- SYSTEME -----------------------
class Statu_Change():
    def __init__(self,name:str,element:str,target:str,Proba:int):
        self.name=name
        self.target=target
        
        self.Ele = element
        self.Probability = Proba

# ------------------------------ STATU_CHANGE ------------------------------ STATU_CHANGE(name,element,target,Dmg,Heal,Proba)
no_statu_change = Statu_Change("",no_type,"self",1)

Paralyze_self = Statu_Change("Paralyse",Electrique,"self",0.6)
Paralyze_other = Statu_Change("Paralyse",Electrique,"other",0.6)
Paralyze_all = Statu_Change("Paralyse",Electrique,"every",1)

Attract_self = Statu_Change("Seduie",no_type,"self",0.6)
Attract_other = Statu_Change("Seduie",no_type,"other",0.6)
Attract_all = Statu_Change("Seduie",no_type,"every",1)

Fear_self = Statu_Change("Apeure",no_type,"self",0.6)
Fear_other = Statu_Change("Apeure",no_type,"other",0.6)
Fear_all = Statu_Change("Apeure",no_type,"every",1)

Poison_self = Statu_Change("Empoisonne",[Poison,Acier],"self",0.2)
Poison_other = Statu_Change("Empoisonne",[Poison,Acier],"other",0.2)
Poison_all = Statu_Change("Empoisonne",[Poison,Acier],"every",1.0)

Confuse_self = Statu_Change("Confu",no_type,"self",0.5)
Confuse_other = Statu_Change("Confu",no_type,"other",0.5)
Confuse_all = Statu_Change("Confu",no_type,"every",1)

Frozed_self = Statu_Change("Gele",Glace,"self",0.6)
Frozed_other = Statu_Change("Gele",Glace,"other",0.6)
Frozed_all = Statu_Change("Gele",Glace,"every",1)

Burned_self = Statu_Change("Brule",Feu,"self",0.6)
Burned_other = Statu_Change("Brule",Feu,"other",0.6)
Burned_all = Statu_Change("Brule",Feu,"every",1)

Wet_self = Statu_Change("Trempe",Eau,"self",0.6)
Wet_other = Statu_Change("Trempe",Eau,"other",0.6)
Wet_all = Statu_Change("Trempe",Eau,"every",1)

Sleepy_self = Statu_Change("Fatigue",Phantom,"self",0.8)
Sleepy_other = Statu_Change("Fatigue",Phantom,"other",0.8)
Sleepy_all = Statu_Change("Fatigue",Phantom,"every",1)

Sleep_self = Statu_Change("Endormie",Phantom,"self",0.2)
Sleep_other = Statu_Change("Endormie",Phantom,"other",0.2)
Sleep_all = Statu_Change("Endormie",Phantom,"every",1)

Healed_self = Statu_Change("Regenere",no_type,"slef",0.8)
Healed_other = Statu_Change("Regenere",no_type,"other",0.8)
Healed_all = Statu_Change("Regenere",no_type,"every",1)

Trap_other = Statu_Change("Piege",no_type,"other",1)
Aggro_other = Statu_Change("Enerve",no_type,"other",1)