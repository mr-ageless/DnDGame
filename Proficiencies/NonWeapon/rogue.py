class NonWeaponProficiency:
    def __init__(self, name, slots_required, relevant_ability, check_modifier):
        self.name = name
        self.slots_required = slots_required
        self.relevant_ability = relevant_ability
        self.check_modifier = check_modifier

# List of rogue non-weapon proficiencies
rogue_proficiencies = [
    NonWeaponProficiency("Acting", 1, "Charisma", -1),
    NonWeaponProficiency("Ancient History", 1, "Intelligence", -1),
    NonWeaponProficiency("Appraising", 1, "Intelligence", 0),
    NonWeaponProficiency("Assimilation", 1, "Intelligence", 0),
    NonWeaponProficiency("Awareness", 2, "Wisdom", 0),
    NonWeaponProficiency("Begging", 1, "Charisma", 0),
    NonWeaponProficiency("Blind-fighting", 2, "NA", "NA"),
    NonWeaponProficiency("Bribery", 1, "Charisma", 0),
    NonWeaponProficiency("Bureaucracy", 2, "Intelligence", 0),
    NonWeaponProficiency("Camouflage", 1, "Wisdom", 0),
    NonWeaponProficiency("Close-quarter Fighting", 2, "Dexterity", 0),
    NonWeaponProficiency("Cryptography", "N/A", "N/A", "N/A"),
    NonWeaponProficiency("Detect Signing", 1, "Intelligence", 1),
    NonWeaponProficiency("Disguise", 1, "Charisma", -1),
    NonWeaponProficiency("Enamor", 1, "Charisma", -2),
    NonWeaponProficiency("Escape", 2, "Dexterity", 0),
    NonWeaponProficiency("Feign/Detect Sleep", 1, "Intelligence", 0),
    NonWeaponProficiency("Forgery", 1, "Dexterity", -1),
    NonWeaponProficiency("Gaming", 1, "Charisma", 0),
    NonWeaponProficiency("Gem Cutting", 2, "Dexterity", -2),
    NonWeaponProficiency("Giant Kite Flying", 1, "Dexterity", -3),
    NonWeaponProficiency("Grooming", 2, "Dexterity", 0),
    NonWeaponProficiency("Hold Breath", 1, "Constitution", 0),
    NonWeaponProficiency("Information Gathering", 1, "Intelligence", "Var"),
    NonWeaponProficiency("Juggling", 1, "Dexterity", -1),
    NonWeaponProficiency("Jumping", 1, "Strength", 0),
    NonWeaponProficiency("Local History", 1, "Charisma", 0),
    NonWeaponProficiency("Locksmithing", 1, "Dexterity", 0),
    NonWeaponProficiency("Musical Instrument", 1, "Dexterity", -1),
    NonWeaponProficiency("Night Vision", 1, "Wisdom", -2),
    NonWeaponProficiency("Observation", 1, "Intelligence", 0),
    NonWeaponProficiency("Pest Control", 1, "Wisdom", 0),
    NonWeaponProficiency("Quick Study", 2, "Varies", -3),
    NonWeaponProficiency("Reading Lips", 2, "Intelligence", -2),
    NonWeaponProficiency("Riding, Horse Specialization", 2, "Wisdom", 4),
    NonWeaponProficiency("Riding, Camel Specialization", 2, "Wisdom", 4),
    NonWeaponProficiency("Set Snares", 1, "Dexterity", -1),
    NonWeaponProficiency("Toxicology", 2, "Intelligence", 0),
    NonWeaponProficiency("Throwing", "N/A", "N/A", "N/A"),
    NonWeaponProficiency("Tightrope Walking", 1, "Dexterity", 0),
    NonWeaponProficiency("Trail Signs", 1, "Intelligence", -1),
    NonWeaponProficiency("Trailing", 1, "Dexterity", "Special"),
    NonWeaponProficiency("Tumbling", 1, "Dexterity", 0),
    NonWeaponProficiency("Underclass", 1, "Wisdom", 0),
    NonWeaponProficiency("Underwater Combat", 2, "Dexterity", 0),
    NonWeaponProficiency("Ventriloquism", 1, "Intelligence", -2),
    NonWeaponProficiency("Voice Mimicry", 2, "Charisma", "Var"),
    NonWeaponProficiency("Water Walking", 1, "Dexterity", -1)
]