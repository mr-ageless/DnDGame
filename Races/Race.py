class Race:
    def __init__(self, name, ability_bonuses, special_traits):
        self.name = name
        self.ability_bonuses = ability_bonuses  # Dictionary with ability modifiers
        self.special_traits = special_traits  # List of unique traits

    def apply_ability_bonuses(self, abilities):
        for ability, bonus in self.ability_bonuses.items():
            abilities[ability] += bonus
        return abilities

    def describe(self):
        return f"Race: {self.name}, Traits: {', '.join(self.special_traits)}"

    def get_special_traits(self):
        return self.special_traits