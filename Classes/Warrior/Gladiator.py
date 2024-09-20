class Gladiator(Fighter):
    def __init__(self, hit_die, proficiencies, thac0, attack_chart, save_throw_chart, arena_fighting_abilities):
        super().__init__(hit_die, proficiencies, thac0, attack_chart, save_throw_chart)
        self.arena_fighting_abilities = arena_fighting_abilities
    
    def get_arena_fighting_abilities(self):
        return self.arena_fighting_abilities
    
    # Add any specific methods or overrides for Gladiator here