# ----------------------- SYSTEME -----------------------
class Bonus():
        def __init__(self,name:str,target:str,strong:float):
            self.name = name
            self.target=target
            self.strong = strong

# ------------------------------ BONUS ------------------------------ Bonus(name,target,strong)
no_bonus = Bonus("...","self",1)

atk_phy_up_self = Bonus("sent une augmentaion de sont attaque physique","self",1.2)
atk_phy_up_other = Bonus("sent une augmentaion de sont attaque physique","other",1.2)

def_phy_up_self = Bonus("sent une augmentation de ça defense physique","self",1.2)
def_phy_up_other = Bonus("sent une augmentation de ça defense physique","other",1.2)

def_spe_up_self = Bonus("sent une augmentation de ça defense special","self",1.2)
def_spe_up_other = Bonus("sent une augmentation de ça defense special","other",1.2)

atk_spe_up_self = Bonus("sent une augmentation de sont attaque special","self",1.2)
atk_spe_up_other = Bonus("sent une augmentation de sont attaque special","other",1.2)

atk_phy_down_self = Bonus("sent une baisse de sont attaque physique","self",0.8)
atk_phy_down_other = Bonus("sent une baisse de sont attaque physique","other",0.8)

def_phy_down_self = Bonus("sent une baisse de ça defense physique","self",0.8)
def_phy_down_other = Bonus("sent une baisse de ça defense physique","other",0.8)

def_spe_down_self = Bonus("sent une baisse de ça defense special","self",0.8)
def_spe_down_other = Bonus("sent une baisse de ça defense special","other",0.8)

atk_spe_down_self = Bonus("sent une baisse de ça defense special","self",0.8)
atk_spe_down_other = Bonus("sent une baisse de ça defense special","other",0.8)

sped_down_self = Bonus("sent une baisse de ça vitesse","self",0.8)
sped_down_other = Bonus("sent une baisse de ça vitesse","other",0.8)

sped_up_self = Bonus("sent une augmentation de ça vitesse","self",1.2)
sped_up_other = Bonus("sent une augmentation de ça vitesse","other",1.2)

energy_up_self_1 = Bonus("a recuperer de l'energie","self",100)
energy_up_other_1 = Bonus("a recuperer de l'energie","other",100)

energy_down_self_1 = Bonus("a perdue de l'energie","self",100)
energy_down_other_1 = Bonus("a perdue de l'energie","other",100)

energy_up_self_2 = Bonus("a recuperer de l'energie","self",150)
energy_up_other_2 = Bonus("a recuperer de l'energie","other",150)

energy_down_self_2 = Bonus("a perdue de l'energie","self",150)
energy_down_other_2 = Bonus("a perdue de l'energie","other",150)

Precision_up_self = Bonus("sent une augmentation de ça precision","self",2)
Precision_up_other = Bonus("sent une augmentation de ça precision","other",2)

Precision_down_self = Bonus("sent une baisse de ça precision","self",0.5)
Precision_down_other = Bonus("sent une baisse de ça precision","other",0.5)

Priority_self = Bonus("attaque rapidement","self",1)
Priority_other = Bonus("charge son attaque","other",1)

heal_self_1 = Bonus("a recuperer 20 point de vie","self",20)
heal_other_1 = Bonus("a recuperer 20 point de vie","other",20)

heal_self_2 = Bonus("a recuperer de la vie","self",60)
heal_other_2 = Bonus("a recuperer de la vie","other",60)

dmg_self = Bonus("a recsue des degats","self",1.2)
dmg_other =  Bonus("a recsue des degats","other",1.2)

revive_1 = Bonus("est remis sur pied","self",0.5)
revive_2 = Bonus("est remis sur pied","self",1)

catching_1 = Bonus("est entrer dans la Pokeball","other",0.40)
catching_2 = Bonus("est entrer dans la Superball","other",0.60)
catching_3 = Bonus("est entrer dans l'Hyperball","other",0.80)
catching_4 = Bonus("est entrer dans la Megaball","other",1.6)
