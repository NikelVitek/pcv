'''
Konstanty v Pythonu

Konstanta je vlastně speciální typ proměnné, jejíž hodnota nemůže být změněna.
V Pythonu jsou konstanty obvykle deklarovány a přiřazovány v modulu, který bývá importován do souboru aplikace.
Konstanty jsou pojmenovány velkými písmeny a jednotlivá slova jsou oddělována podtržítky.
'''

EARTH_GRAVITY = 9.81 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.625 #? měsíční gravitace
SPEED_OF_LIGHT = 299792458 #? rychlost světla ve vakuu
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu

''' 
Úkol:
1. Doplňte správně hodnoty uvedených konstant.
2. Doplňte physics.py o několik výpočtových funkcí (opatřené docstrings), v nichž využijete minimálně všechny výše uvedené konstanty.
Samozřejmě můžete své řešení rozšířit i o jiné fyzikální konstanty.
3. Vytvořte z tohoto souboru samostatný modul v Pythonu podle návodu, který si sami najdete na internetu.      
4. Vytvořte vlastní aplikaci myapp.py, do níž tento modul importujte. Demonstrujte v ní na jednoduchých příkladech využití vámi
připravených funkcí.  
'''


def weight_on_surface(mass, planet="Earth"):
    if planet == "Earth":
        gravity = EARTH_GRAVITY
    elif planet == "Moon":
        gravity = MOON_GRAVITY
    else:
        raise ValueError("Unsupported planet")
    weight = mass * gravity
    return weight


def time_to_travel_distance(distance, velocity=SPEED_OF_LIGHT):
    time = distance / velocity
    return time


def speed_of_sound_in_air(temperature=20):
    speed = SPEED_OF_SOUND * (temperature / 20) ** 0.5
    return speed

