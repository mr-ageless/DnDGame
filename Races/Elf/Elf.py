from Race import Race

class Elf(Race):
    def __init__(self):
        ability_bonuses = {'dexterity': 2, 'intelligence': 1}
        special_traits = ['Keen Senses: Proficiency in Perception', 'Fey Ancestry: Advantage on charm saves']
        super().__init__(name="Elf", ability_bonuses=ability_bonuses, special_traits=special_traits)