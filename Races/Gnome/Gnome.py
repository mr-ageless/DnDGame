from Race import Race

class Gnome(Race):
    def __init__(self):
        ability_bonuses = {'intelligence': 2, 'dexterity': 1}
        special_traits = ['Gnome Cunning: Advantage on magic saves', 'Small: Extra stealth']
        super().__init__(name="Gnome", ability_bonuses=ability_bonuses, special_traits=special_traits)