from Race import Race

class HalfElf(Race):
    def __init__(self):
        ability_bonuses = {'charisma': 2, 'dexterity': 1, 'intelligence': 1}
        special_traits = ['Darkvision', 'Fey Ancestry', 'Versatile: Bonus to two other stats']
        super().__init__(name="Half-Elf", ability_bonuses=ability_bonuses, special_traits=special_traits)