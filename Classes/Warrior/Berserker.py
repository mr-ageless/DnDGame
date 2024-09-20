class Berserker(Fighter):
    def __init__(self, hit_die, proficiencies, thac0, attack_chart, save_throw_chart, berserk_rage_abilities):
        super().__init__(hit_die, proficiencies, thac0, attack_chart, save_throw_chart)
        self.berserk_rage_abilities = berserk_rage_abilities
    
    def get_berserk_rage_abilities(self):
        return self.berserk_rage_abilities
    
    # Add any specific methods or overrides for Berserker here