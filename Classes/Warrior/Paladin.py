class Paladin(Fighter):
    def __init__(self, hit_die, proficiencies, thac0, attack_chart, save_throw_chart, divine_abilities):
        super().__init__(hit_die, proficiencies, thac0, attack_chart, save_throw_chart)
        self.divine_abilities = divine_abilities
    
    def get_divine_abilities(self):
        return self.divine_abilities
    
    # Add any specific methods or overrides for Paladin here