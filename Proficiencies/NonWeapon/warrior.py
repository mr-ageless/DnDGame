class NonWeaponProficiency:
    def __init__(self, name, slots_required, relevant_ability, check_modifier):
        self.name = name
        self.slots_required = slots_required
        self.relevant_ability = relevant_ability
        self.check_modifier = check_modifier

# List of warrior non-weapon proficiencies
warrior_proficiencies = [
    NonWeaponProficiency("Animal Lore", 1, "Intelligence", 0),
    NonWeaponProficiency("Armorer", 2, "Intelligence", -2),
    NonWeaponProficiency("Armorer, Crude", 1, "Intelligence", -1),
    NonWeaponProficiency("Artillerist", 1, "Charisma", "?"),
    NonWeaponProficiency("Awareness", 2, "Wisdom", 0),
    NonWeaponProficiency("Blind-fighting", 2, "NA", "NA"),
    NonWeaponProficiency("Bowyer/Fletcher", 1, "Dexterity", -1),
    NonWeaponProficiency("Bowyer/Fletcher, Crude", 1, "Dexterity", 0),
    NonWeaponProficiency("Camouflage", 1, "Wisdom", 0),
    NonWeaponProficiency("Charioteering", 1, "Dexterity", 2),
    NonWeaponProficiency("Close-quarter Fighting", 2, "Dexterity", 0),
    NonWeaponProficiency("Display Weapon Prowess", 1, "Dexterity", 0),
    NonWeaponProficiency("Endurance", 2, "Constitution", 0),
    NonWeaponProficiency("Ethereal Tracking", 2, "Wisdom", -2),
    NonWeaponProficiency("Gaming", 1, "Charisma", 0),
    NonWeaponProficiency("Gunsmithing", 2, "Intelligence", -3),
    NonWeaponProficiency("Horde Summoning", 2, "Charisma", -2),
    NonWeaponProficiency("Hunting", 1, "Wisdom", -1),
    NonWeaponProficiency("Jousting", 1, "Dexterity", 2),
    NonWeaponProficiency("Law", 1, "Wisdom", 0),
    NonWeaponProficiency("Leadership", 1, "Charisma", 0),
    NonWeaponProficiency("Light Sleeping", 1, "Constitution", -1),
    NonWeaponProficiency("Mountaineering", 1, "NA", "NA"),
    NonWeaponProficiency("Natural Fighting", 2, "Strength", 1),
    NonWeaponProficiency("Naval Combat", 1, "Intelligence", 0),
    NonWeaponProficiency("Navigation", 1, "Intelligence", -2),
    NonWeaponProficiency("Oratory", 1, "Charisma", 0),
    NonWeaponProficiency("Riding, Horse Specialization", 2, "Wisdom", 4),
    NonWeaponProficiency("Riding, Camel Specialization", 2, "Wisdom", 4),
    NonWeaponProficiency("Running", 1, "Constitution", -6),
    NonWeaponProficiency("Set Snares", 1, "Dexterity", -1),
    NonWeaponProficiency("Spelunking", 1, "Intelligence", -1),
    NonWeaponProficiency("Style Analysis", 1, "Intelligence", -1),
    NonWeaponProficiency("Survival", 2, "Intelligence", 0),
    NonWeaponProficiency("Tracking", 2, "Wisdom", 0),
    NonWeaponProficiency("Trail Marking", 1, "Wisdom", 0),
    NonWeaponProficiency("Trail Signs", 1, "Intelligence", -1),
    NonWeaponProficiency("Underwater Combat", 2, "Dexterity", 0),
    NonWeaponProficiency("Vehicle Handling", 1, "Dexterity", "?"),
    NonWeaponProficiency("Weapon Improvisation", 1, "Wisdom", -1),
    NonWeaponProficiency("Weaponsmithing", 3, "Intelligence", -3),
    NonWeaponProficiency("Weaponsmithing, Crude", 1, "Wisdom", -3),
    NonWeaponProficiency("Wild Fighting", 2, "Constitution", 0)
]