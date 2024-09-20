class Barbarian(Fighter):
    def __init__(self, hit_die, proficiencies, thac0, attack_chart, save_throw_chart, rage_abilities):
        super().__init__(hit_die, proficiencies, thac0, attack_chart, save_throw_chart)
        self.rage_abilities = rage_abilities
    
    def get_rage_abilities(self):
        return self.rage_abilities
    
    # Add any specific methods or overrides for Barbarian here