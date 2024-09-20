class SavingThrowManager:
    def __init__(self):
        # Define saving throw charts for various character classes (AD&D 2e)
        self.saving_throw_data = {
            'Fighter': {
		    0:  {'death_paral_poison': 16, 'rod_staff_wand': 18, 'petrification_polymorph': 17, 'breath_weapon': 20, 'spell': 19},
        	1:  {'death_paral_poison': 14, 'rod_staff_wand': 16, 'petrification_polymorph': 15, 'breath_weapon': 17, 'spell': 17},
        	2:  {'death_paral_poison': 14, 'rod_staff_wand': 16, 'petrification_polymorph': 15, 'breath_weapon': 17, 'spell': 17},
        	3:  {'death_paral_poison': 13, 'rod_staff_wand': 15, 'petrification_polymorph': 14, 'breath_weapon': 16, 'spell': 16},
        	4:  {'death_paral_poison': 13, 'rod_staff_wand': 15, 'petrification_polymorph': 14, 'breath_weapon': 16, 'spell': 16},
        	5:  {'death_paral_poison': 11, 'rod_staff_wand': 13, 'petrification_polymorph': 12, 'breath_weapon': 13, 'spell': 14},
        	6:  {'death_paral_poison': 11, 'rod_staff_wand': 13, 'petrification_polymorph': 12, 'breath_weapon': 13, 'spell': 14},
        	7:  {'death_paral_poison': 10, 'rod_staff_wand': 12, 'petrification_polymorph': 11, 'breath_weapon': 12, 'spell': 13},
        	8:  {'death_paral_poison': 10, 'rod_staff_wand': 12, 'petrification_polymorph': 11, 'breath_weapon': 12, 'spell': 13},
        	9:  {'death_paral_poison': 8, 'rod_staff_wand': 10, 'petrification_polymorph': 9, 'breath_weapon': 9, 'spell': 11},
        	10: {'death_paral_poison': 8, 'rod_staff_wand': 10, 'petrification_polymorph': 9, 'breath_weapon': 9, 'spell': 11},
        	11: {'death_paral_poison': 7, 'rod_staff_wand': 9, 'petrification_polymorph': 8, 'breath_weapon': 8, 'spell': 10},
        	12: {'death_paral_poison': 7, 'rod_staff_wand': 9, 'petrification_polymorph': 8, 'breath_weapon': 8, 'spell': 10},
        	13: {'death_paral_poison': 5, 'rod_staff_wand': 7, 'petrification_polymorph': 6, 'breath_weapon': 5, 'spell': 8},
        	14: {'death_paral_poison': 5, 'rod_staff_wand': 7, 'petrification_polymorph': 6, 'breath_weapon': 5, 'spell': 8},
        	15: {'death_paral_poison': 4, 'rod_staff_wand': 6, 'petrification_polymorph': 5, 'breath_weapon': 4, 'spell': 7},
        	16: {'death_paral_poison': 4, 'rod_staff_wand': 6, 'petrification_polymorph': 5, 'breath_weapon': 4, 'spell': 7},
        	17: {'death_paral_poison': 3, 'rod_staff_wand': 5, 'petrification_polymorph': 4, 'breath_weapon': 4, 'spell': 6},
        	18: {'death_paral_poison': 3, 'rod_staff_wand': 5, 'petrification_polymorph': 4, 'breath_weapon': 4, 'spell': 6},
        	19: {'death_paral_poison': 3, 'rod_staff_wand': 5, 'petrification_polymorph': 4, 'breath_weapon': 4, 'spell': 6},
        	20: {'death_paral_poison': 3, 'rod_staff_wand': 5, 'petrification_polymorph': 4, 'breath_weapon': 4, 'spell': 6},
		},
              'Priest': {
        	1:  {'death_paral_poison': 10, 'rod_staff_wand': 14, 'petrification_polymorph': 13, 'breath_weapon': 16, 'spell': 15},
        	2:  {'death_paral_poison': 10, 'rod_staff_wand': 14, 'petrification_polymorph': 13, 'breath_weapon': 16, 'spell': 15},
        	3:  {'death_paral_poison': 10, 'rod_staff_wand': 14, 'petrification_polymorph': 13, 'breath_weapon': 16, 'spell': 15},
        	4:  {'death_paral_poison': 9, 'rod_staff_wand': 13, 'petrification_polymorph': 12, 'breath_weapon': 15, 'spell': 14},
        	5:  {'death_paral_poison': 9, 'rod_staff_wand': 13, 'petrification_polymorph': 12, 'breath_weapon': 15, 'spell': 14},
        	6:  {'death_paral_poison': 9, 'rod_staff_wand': 13, 'petrification_polymorph': 12, 'breath_weapon': 15, 'spell': 14},
        	7:  {'death_paral_poison': 7, 'rod_staff_wand': 11, 'petrification_polymorph': 10, 'breath_weapon': 13, 'spell': 12},
        	8:  {'death_paral_poison': 7, 'rod_staff_wand': 11, 'petrification_polymorph': 10, 'breath_weapon': 13, 'spell': 12},
        	9:  {'death_paral_poison': 7, 'rod_staff_wand': 11, 'petrification_polymorph': 10, 'breath_weapon': 13, 'spell': 12},
        	10: {'death_paral_poison': 6, 'rod_staff_wand': 10, 'petrification_polymorph': 9, 'breath_weapon': 12, 'spell': 11},
        	11: {'death_paral_poison': 6, 'rod_staff_wand': 10, 'petrification_polymorph': 9, 'breath_weapon': 12, 'spell': 11},
        	12: {'death_paral_poison': 6, 'rod_staff_wand': 10, 'petrification_polymorph': 9, 'breath_weapon': 12, 'spell': 11},
        	13: {'death_paral_poison': 5, 'rod_staff_wand': 9, 'petrification_polymorph': 8, 'breath_weapon': 11, 'spell': 10},
        	14: {'death_paral_poison': 5, 'rod_staff_wand': 9, 'petrification_polymorph': 8, 'breath_weapon': 11, 'spell': 10},
        	15: {'death_paral_poison': 5, 'rod_staff_wand': 9, 'petrification_polymorph': 8, 'breath_weapon': 11, 'spell': 10},
        	16: {'death_paral_poison': 4, 'rod_staff_wand': 8, 'petrification_polymorph': 7, 'breath_weapon': 10, 'spell': 9},
        	17: {'death_paral_poison': 4, 'rod_staff_wand': 8, 'petrification_polymorph': 7, 'breath_weapon': 10, 'spell': 9},
        	18: {'death_paral_poison': 4, 'rod_staff_wand': 8, 'petrification_polymorph': 7, 'breath_weapon': 10, 'spell': 9},
        	19: {'death_paral_poison': 2, 'rod_staff_wand': 6, 'petrification_polymorph': 5, 'breath_weapon': 8, 'spell': 7},
        	20: {'death_paral_poison': 2, 'rod_staff_wand': 6, 'petrification_polymorph': 5, 'breath_weapon': 8, 'spell': 7},
    		},
	      'Rogue': {
        	1:  {'death_paral_poison': 13, 'rod_staff_wand': 14, 'petrification_polymorph': 12, 'breath_weapon': 16, 'spell': 15},
        	2:  {'death_paral_poison': 13, 'rod_staff_wand': 14, 'petrification_polymorph': 12, 'breath_weapon': 16, 'spell': 15},
        	3:  {'death_paral_poison': 13, 'rod_staff_wand': 14, 'petrification_polymorph': 12, 'breath_weapon': 16, 'spell': 15},
        	4:  {'death_paral_poison': 13, 'rod_staff_wand': 14, 'petrification_polymorph': 12, 'breath_weapon': 16, 'spell': 15},
        	5:  {'death_paral_poison': 12, 'rod_staff_wand': 12, 'petrification_polymorph': 11, 'breath_weapon': 15, 'spell': 13},
        	6:  {'death_paral_poison': 12, 'rod_staff_wand': 12, 'petrification_polymorph': 11, 'breath_weapon': 15, 'spell': 13},
        	7:  {'death_paral_poison': 12, 'rod_staff_wand': 12, 'petrification_polymorph': 11, 'breath_weapon': 15, 'spell': 13},
        	8:  {'death_paral_poison': 12, 'rod_staff_wand': 12, 'petrification_polymorph': 11, 'breath_weapon': 15, 'spell': 13},
        	9:  {'death_paral_poison': 11, 'rod_staff_wand': 10, 'petrification_polymorph': 10, 'breath_weapon': 14, 'spell': 11},
        	10: {'death_paral_poison': 11, 'rod_staff_wand': 10, 'petrification_polymorph': 10, 'breath_weapon': 14, 'spell': 11},
        	11: {'death_paral_poison': 11, 'rod_staff_wand': 10, 'petrification_polymorph': 10, 'breath_weapon': 14, 'spell': 11},
        	12: {'death_paral_poison': 11, 'rod_staff_wand': 10, 'petrification_polymorph': 10, 'breath_weapon': 14, 'spell': 11},
        	13: {'death_paral_poison': 10, 'rod_staff_wand': 8, 'petrification_polymorph': 9, 'breath_weapon': 13, 'spell': 9},
        	14: {'death_paral_poison': 10, 'rod_staff_wand': 8, 'petrification_polymorph': 9, 'breath_weapon': 13, 'spell': 9},
        	15: {'death_paral_poison': 10, 'rod_staff_wand': 8, 'petrification_polymorph': 9, 'breath_weapon': 13, 'spell': 9},
        	16: {'death_paral_poison': 10, 'rod_staff_wand': 8, 'petrification_polymorph': 9, 'breath_weapon': 13, 'spell': 9},
        	17: {'death_paral_poison': 9, 'rod_staff_wand': 6, 'petrification_polymorph': 8, 'breath_weapon': 12, 'spell': 7},
        	18: {'death_paral_poison': 9, 'rod_staff_wand': 6, 'petrification_polymorph': 8, 'breath_weapon': 12, 'spell': 7},
        	19: {'death_paral_poison': 9, 'rod_staff_wand': 6, 'petrification_polymorph': 8, 'breath_weapon': 12, 'spell': 7},
        	20: {'death_paral_poison': 9, 'rod_staff_wand': 6, 'petrification_polymorph': 8, 'breath_weapon': 12, 'spell': 7},
        	21: {'death_paral_poison': 8, 'rod_staff_wand': 4, 'petrification_polymorph': 7, 'breath_weapon': 11, 'spell': 5},
    		},
    	      'Wizard': {
        	1:  {'death_paral_poison': 14, 'rod_staff_wand': 11, 'petrification_polymorph': 13, 'breath_weapon': 15, 'spell': 12},
        	2:  {'death_paral_poison': 14, 'rod_staff_wand': 11, 'petrification_polymorph': 13, 'breath_weapon': 15, 'spell': 12},
        	3:  {'death_paral_poison': 14, 'rod_staff_wand': 11, 'petrification_polymorph': 13, 'breath_weapon': 15, 'spell': 12},
        	4:  {'death_paral_poison': 14, 'rod_staff_wand': 11, 'petrification_polymorph': 13, 'breath_weapon': 15, 'spell': 12},
        	5:  {'death_paral_poison': 14, 'rod_staff_wand': 11, 'petrification_polymorph': 13, 'breath_weapon': 15, 'spell': 12},
        	6:  {'death_paral_poison': 13, 'rod_staff_wand': 9, 'petrification_polymorph': 11, 'breath_weapon': 13, 'spell': 10},
        	7:  {'death_paral_poison': 13, 'rod_staff_wand': 9, 'petrification_polymorph': 11, 'breath_weapon': 13, 'spell': 10},
        	8:  {'death_paral_poison': 13, 'rod_staff_wand': 9, 'petrification_polymorph': 11, 'breath_weapon': 13, 'spell': 10},
        	9:  {'death_paral_poison': 13, 'rod_staff_wand': 9, 'petrification_polymorph': 11, 'breath_weapon': 13, 'spell': 10},
        	10: {'death_paral_poison': 13, 'rod_staff_wand': 9, 'petrification_polymorph': 11, 'breath_weapon': 13, 'spell': 10},
        	11: {'death_paral_poison': 11, 'rod_staff_wand': 7, 'petrification_polymorph': 9, 'breath_weapon': 11, 'spell': 8},
        	12: {'death_paral_poison': 11, 'rod_staff_wand': 7, 'petrification_polymorph': 9, 'breath_weapon': 11, 'spell': 8},
        	13: {'death_paral_poison': 11, 'rod_staff_wand': 7, 'petrification_polymorph': 9, 'breath_weapon': 11, 'spell': 8},
        	14: {'death_paral_poison': 11, 'rod_staff_wand': 7, 'petrification_polymorph': 9, 'breath_weapon': 11, 'spell': 8},
        	15: {'death_paral_poison': 11, 'rod_staff_wand': 7, 'petrification_polymorph': 9, 'breath_weapon': 11, 'spell': 8},
        	16: {'death_paral_poison': 10, 'rod_staff_wand': 5, 'petrification_polymorph': 7, 'breath_weapon': 9, 'spell': 6},
        	17: {'death_paral_poison': 10, 'rod_staff_wand': 5, 'petrification_polymorph': 7, 'breath_weapon': 9, 'spell': 6},
        	18: {'death_paral_poison': 10, 'rod_staff_wand': 5, 'petrification_polymorph': 7, 'breath_weapon': 9, 'spell': 6},
        	19: {'death_paral_poison': 10, 'rod_staff_wand': 5, 'petrification_polymorph': 7, 'breath_weapon': 9, 'spell': 6},
        	20: {'death_paral_poison': 10, 'rod_staff_wand': 5, 'petrification_polymorph': 7, 'breath_weapon': 9, 'spell': 6},
        	21: {'death_paral_poison': 8,  'rod_staff_wand': 3, 'petrification_polymorph': 5, 'breath_weapon': 7, 'spell': 4},
    		},
	      'Psionicist': {
        	1:  {'death_paral_poison': 13, 'rod_staff_wand': 15, 'petrification_polymorph': 10, 'breath_weapon': 16, 'spell': 15},
        	2:  {'death_paral_poison': 13, 'rod_staff_wand': 15, 'petrification_polymorph': 10, 'breath_weapon': 16, 'spell': 15},
        	3:  {'death_paral_poison': 13, 'rod_staff_wand': 15, 'petrification_polymorph': 10, 'breath_weapon': 16, 'spell': 15},
        	4:  {'death_paral_poison': 13, 'rod_staff_wand': 15, 'petrification_polymorph': 10, 'breath_weapon': 16, 'spell': 15},
        	5:  {'death_paral_poison': 12, 'rod_staff_wand': 13, 'petrification_polymorph': 9, 'breath_weapon': 15, 'spell': 14},
        	6:  {'death_paral_poison': 12, 'rod_staff_wand': 13, 'petrification_polymorph': 9, 'breath_weapon': 15, 'spell': 14},
        	7:  {'death_paral_poison': 12, 'rod_staff_wand': 13, 'petrification_polymorph': 9, 'breath_weapon': 15, 'spell': 14},
        	8:  {'death_paral_poison': 12, 'rod_staff_wand': 13, 'petrification_polymorph': 9, 'breath_weapon': 15, 'spell': 14},
        	9:  {'death_paral_poison': 11, 'rod_staff_wand': 11, 'petrification_polymorph': 8, 'breath_weapon': 13, 'spell': 12},
        	10: {'death_paral_poison': 11, 'rod_staff_wand': 11, 'petrification_polymorph': 8, 'breath_weapon': 13, 'spell': 12},
        	11: {'death_paral_poison': 11, 'rod_staff_wand': 11, 'petrification_polymorph': 8, 'breath_weapon': 13, 'spell': 12},
        	12: {'death_paral_poison': 11, 'rod_staff_wand': 11, 'petrification_polymorph': 8, 'breath_weapon': 13, 'spell': 12},
        	13: {'death_paral_poison': 10, 'rod_staff_wand': 9, 'petrification_polymorph': 7, 'breath_weapon': 12, 'spell': 11},
        	14: {'death_paral_poison': 10, 'rod_staff_wand': 9, 'petrification_polymorph': 7, 'breath_weapon': 12, 'spell': 11},
        	15: {'death_paral_poison': 10, 'rod_staff_wand': 9, 'petrification_polymorph': 7, 'breath_weapon': 12, 'spell': 11},
        	16: {'death_paral_poison': 10, 'rod_staff_wand': 9, 'petrification_polymorph': 7, 'breath_weapon': 12, 'spell': 11},
        	17: {'death_paral_poison': 9,  'rod_staff_wand': 7, 'petrification_polymorph': 6, 'breath_weapon': 11, 'spell': 9},
        	18: {'death_paral_poison': 9,  'rod_staff_wand': 7, 'petrification_polymorph': 6, 'breath_weapon': 11, 'spell': 9},
        	19: {'death_paral_poison': 9,  'rod_staff_wand': 7, 'petrification_polymorph': 6, 'breath_weapon': 11, 'spell': 9},
        	20: {'death_paral_poison': 9,  'rod_staff_wand': 7, 'petrification_polymorph': 6, 'breath_weapon': 11, 'spell': 9},
        	21: {'death_paral_poison': 8,  'rod_staff_wand': 5, 'petrification_polymorph': 5, 'breath_weapon': 9,  'spell': 7},
	    },
        }
    
    def get_saving_throw(self, character_class, level, throw_type):
        if character_class not in self.saving_throw_data:
            raise ValueError("Invalid character class")
        if level not in self.saving_throw_data[character_class]:
            raise ValueError("Invalid level")
        if throw_type not in self.saving_throw_data[character_class][level]:
            raise ValueError("Invalid saving throw type")
        
        return self.saving_throw_data[character_class][level][throw_type]
    
    def print_saving_throws(self, character_class, level):
        if character_class not in self.saving_throw_data:
            raise ValueError("Invalid character class")
        if level not in self.saving_throw_data[character_class]:
            raise ValueError("Invalid level")

        saving_throws = self.saving_throw_data[character_class][level]
        print(f"Saving Throws for {character_class} at Level {level}:")
        for throw_type, value in saving_throws.items():
            print(f"{throw_type.replace('_', ' ').title()}: {value}")

# Example usage:
manager = SavingThrowManager()
manager.print_saving_throws('Fighter', 1)