from WeaponList import WeaponsList
from Weapon import Weapon

def main():
    weapons_list = WeaponsList()

    # Create a weapon based on user input
    weapon = Weapon.create_weapon(weapons_list)
    
    if weapon:
        # Display weapon details
        print(weapon.display_details())
        
        # Ask for target size
        target_size = input("Enter the target size (sm_med/large): ").strip().lower()
        
        try:
            damage_roll = weapon.calculate_damage(target_size)
            print(f"Damage roll against {target_size} target: {damage_roll}")
        except ValueError as e:
            print(f"Error: {e}")
            return  # Exit if invalid size or damage

if __name__ == "__main__":
    main()
