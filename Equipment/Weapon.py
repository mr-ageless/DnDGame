import random
import re

# Conversion constant for pounds to kilograms
LB_TO_KG = 0.453592  

class Weapon:
    def __init__(self, name, damage_sm_med, damage_large, weight, weapon_type, damage_type, melee_reach, unit='lb'):
        self.name = name
        self.damage_sm_med = damage_sm_med  # Example: '1d8'
        self.damage_large = damage_large  # Example: '2d6'
        self.weight = weight
        self.unit = unit  # Default to pounds ('lb')
        self.weapon_type = weapon_type  # e.g., "sword", "dagger"
        self.damage_type = damage_type  # e.g., "S/P"
        self.melee_reach = melee_reach  # e.g., 1 (melee reach multiplier)

    def calculate_damage(self, target_size='sm_med'):
        # Select the correct damage value based on target size
        damage = self.damage_large if target_size == 'large' else self.damage_sm_med
        
        # Use regex to handle dice rolls with optional modifiers (e.g., 1d4+1, 2d6-2)
        dice_match = re.match(r'(\d+)d(\d+)([+-]\d+)?', damage)
        if not dice_match:
            raise ValueError(f"Invalid damage format: {damage}")
        
        dice_count = int(dice_match.group(1))  # Number of dice (e.g., 1 in '1d4')
        dice_sides = int(dice_match.group(2))  # Sides on the dice (e.g., 4 in '1d4')
        modifier = int(dice_match.group(3)) if dice_match.group(3) else 0  # Modifier (e.g., +1 or -1)

        # Roll the dice
        total_damage = sum(random.randint(1, dice_sides) for _ in range(dice_count))

        # Add the modifier to the total damage
        total_damage += modifier

        return total_damage

    def convert_weight(self, to_metric=False):
        # Converts the weight to metric if requested
        if to_metric and self.unit == 'lb':
            return round(self.weight * LB_TO_KG, 2)
        return self.weight

    def get_weight(self, unit='lb'):
        # Return weight in the preferred unit (either 'lb' or 'kg')
        if unit == 'kg':
            return self.convert_weight(to_metric=True)
        return self.weight
    
    def display_details(self):
        # Display weapon details in title case
        return (f"Name: {self.name.title()}\n"
                f"Damage (Small/Medium): {self.damage_sm_med}\n"
                f"Damage (Large): {self.damage_large}\n"
                f"Damage Type: {self.damage_type}\n"
                f"Melee Reach: {self.melee_reach}x reach\n"
                f"Weight: {self.weight} {self.unit}\n"
                f"Type: {self.weapon_type}")

    @staticmethod
    def create_weapon(weapons_list):
        # Get weapon name from user and normalize case
        weapon_name = input("Enter the weapon name: ").strip().title()
        weapon_data = weapons_list.get_weapon_data(weapon_name)

        if weapon_data:
            return Weapon(
                name=weapon_name,
                damage_sm_med=weapon_data.get('Damage vs Sm-Med', 'Unknown'),  # Default to 'Unknown' if key not found
                damage_large=weapon_data.get('Damage vs Large', 'Unknown'),  # Default to 'Unknown' if key not found
                weight=weapon_data['Weight'],
                weapon_type=weapon_data['Type'],
                damage_type=weapon_data.get('Type', 'Unknown'),  # Add damage type (B/P/S)
                melee_reach=weapon_data.get('Melee Reach', 1),  # Add melee reach
            )
        else:
            raise ValueError(f"Weapon '{weapon_name}' not found in the weapon list.")
