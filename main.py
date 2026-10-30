from Bonus_code import *
from Element_code import *
from Statu_code import *
from Attack_code import *
from Pokemon_code import *
from Meteo_code import *
from Object_code import *
from Combat_code import *
from Groupe_code import *

# --- TEST ---
Combat_sauvage(Equipe,Zone_1,Sac,Aleatoir,"Midi","Hexdaria")

# ---- Dictionair ----

# Type of element : Normal ; Feu ; Eau ; Dragon ; Electrique ; Plante ; Glace ; Combat ; Poison ; Sol ; Vol ; Psy ; Insect ; Terre ; Phantom ; Dragon ;  Tenebre ; Acier ; ; Inconnue

# Type of attaque : phy ; spe

# Type of target : ground ; underground ; sky ; all

# Type of effect : Paralyze ; Stun ; Confuse ; Frozed ; Burned ; Blinded ; Sleepy ; Sleep ; Healed

# Type of bonus : atk_phy_up ; def_phy_up ; def_spe_up ; atk_spe_up ; atk_phy_down ; def_phy_down ; def_spe_down ; atk_spe_down ; sped_down ; sped_up ; heal ; dmg ;  use_up

# Type of rarity : Commun ; Peu commun ; Rare ; Legendaire

# ---- Note ----

# < >
# Problem : seul le premier pokemon peut attaquer, un pokemon mort ou partie est toujours contabiliser pendant le tour en cour
# Mise a jour actife : Créer des combat avec plusieur pokemon sauvage
# Prochaine mise a jour : Systéme d'évolution, Systéme d'apprentissage de capacité, Systéme de bonus, Systéme d'objet & capture, fonctionnement de la meteo, Systéme de temps (Jour -> Soir -> Nuit -> Matin ->)
# Mise a jour future : création du menu, créaton de la boucle de gameplay, ajout de pokemon (gen 1), ajout d'une histoire et ajout de capacités