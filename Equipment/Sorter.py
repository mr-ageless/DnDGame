from WeaponList import WeaponsList  # Import the WeaponsList class

def reformat_weapon_dict(weapon_instance, output_file):
    # Access the weapons dictionary from the weapon_instance
    weapon_dict = weapon_instance.weapons
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("weapons = {\n")
        for name, details in weapon_dict.items():
            f.write(f'    "{name}": {{\n')
            for key, value in details.items():
                f.write(f'        "{key}": {repr(value)},\n')
            f.write("    },\n")
        f.write("}\n")

# Create an instance of WeaponsList
weapons_list_instance = WeaponsList()

# Pass the instance to the function to reformat the dictionary
reformat_weapon_dict(weapons_list_instance, 'reformatted_weapons.py')
