from Race import Race

class Dwarf(Race):
    def __init__(self):
        ability_bonuses = {'constitution': 2, 'strength': 1}
        special_traits = ['Darkvision', 'Resilience: Advantage on saving throws against poison']
        super().__init__(name="Dwarf", ability_bonuses=ability_bonuses, special_traits=special_traits)