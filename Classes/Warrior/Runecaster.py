class Runecaster(Fighter):
    def __init__(self, hit_die, proficiencies, thac0, attack_chart, save_throw_chart, rune_crafting_abilities):
        super().__init__(hit_die, proficiencies, thac0, attack_chart, save_throw_chart)
        self.rune_crafting_abilities = rune_crafting_abilities
    
    def get_rune_crafting_abilities(self):
        return self.rune_crafting_abilities
    
    # Add any specific methods or overrides for Runecaster here