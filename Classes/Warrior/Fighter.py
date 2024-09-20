import random
from Proficiencies.ProficiencyManager import ProficiencyManager

class Fighter:
    def __init__(self, hit_die, proficiencies, thac0, attack_chart, save_throw_chart, proficiency_manager):
        self.hit_die = hit_die
        self.proficiencies = proficiencies
        self.thac0 = thac0
        self.attack_chart = attack_chart
        self.save_throw_chart = save_throw_chart
        self.proficiency_manager = proficiency_manager  # Store the instance of ProficiencyManager
    
    def get_hit_die(self):
        return self.hit_die
    
    def get_proficiencies(self):
        return self.proficiencies
    
    def get_thac0(self):
        return self.thac0
    
    def get_number_of_attacks(self, level):
        return self.attack_chart.get(level, "No data for this level")
    
    def get_save_throws(self, level):
        return self.save_throw_chart.get(level, "No data for this level")
    
    def roll_die(self, die_sides):
        return random.randint(1, die_sides)
    
    def calculate_hp(self, level):
        hp = 0
        for _ in range(level):
            hp += self.roll_die(self.hit_die)
        return hp
    
    def get_proficiency_slots(self, character_class, level):
        # Use the proficiency_manager instance to get proficiency slots
        return self.proficiency_manager.get_proficiency_slots(character_class, level)

    def update_proficiencies(self, character_class, level):
        proficiency_info = self.get_proficiency_slots(character_class, level)
        weapon_slots = proficiency_info['weapon']
        nonweapon_slots = proficiency_info['nonweapon']
        
        # Ensure that we have enough slots based on level
        while len(self.proficiencies['weapon']) < weapon_slots:
            self.proficiencies['weapon'].append(None)  # Add placeholder for new proficiency
        
        while len(self.proficiencies['nonweapon']) < nonweapon_slots:
            self.proficiencies['nonweapon'].append(None)  # Add placeholder for new proficiency

        # Handle removing or modifying proficiencies if needed

# Example usage:
proficiency_manager = ProficiencyManager()
fighter = Fighter(hit_die=10, proficiencies={'weapon': [], 'nonweapon': []}, thac0=20, 
                  attack_chart={1: 1, 2: 2}, save_throw_chart={1: [15, 14, 13], 2: [13, 12, 11]}, 
                  proficiency_manager=proficiency_manager)

# Now the Fighter can properly access proficiency data:
print(fighter.get_proficiency_slots('Warrior', 1))  # {'weapon': 4, 'nonweapon': 3}
