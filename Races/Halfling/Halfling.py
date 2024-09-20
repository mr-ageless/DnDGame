from Race import Race

class Halfling(Race):
    def __init__(self):
        ability_bonuses = {'dexterity': 2, 'charisma': 1}
        special_traits = ['Lucky: Reroll on critical fails', 'Brave: Advantage on fear saves']
        super().__init__(name="Hobbit", ability_bonuses=ability_bonuses, special_traits=special_traits)