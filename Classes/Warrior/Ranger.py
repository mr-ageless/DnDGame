class Ranger(Fighter):
    def __init__(self, hit_die, proficiencies, thac0, attack_chart, save_throw_chart, tracking_abilities):
        super().__init__(hit_die, proficiencies, thac0, attack_chart, save_throw_chart)
        self.tracking_abilities = tracking_abilities
    
    def get_tracking_abilities(self):
        return self.tracking_abilities
    
    # Add any specific methods or overrides for Ranger here