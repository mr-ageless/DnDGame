class NonWeaponProficiency:
    def __init__(self, name, slots_required, relevant_ability, check_modifier):
        self.name = name
        self.slots_required = slots_required
        self.relevant_ability = relevant_ability
        self.check_modifier = check_modifier

# List of priest non-weapon proficiencies
priest_proficiencies = [
    NonWeaponProficiency("Administration", 1, "Intelligence", 1),
    NonWeaponProficiency("Alchemy", 3, "Intelligence", -2),
    NonWeaponProficiency("Alms", 1, "Charisma", 0),
    NonWeaponProficiency("Ancient History", 1, "Intelligence", -1),
    NonWeaponProficiency("Astrology", 2, "Intelligence", 0),
    NonWeaponProficiency("Bartering", 1, "Intelligence", -2),
    NonWeaponProficiency("Bookbinding", 1, "Intelligence", 0),
    NonWeaponProficiency("Burial Customs", 1, "Intelligence", 0),
    NonWeaponProficiency("Bureaucracy", 2, "Intelligence", 0),
    NonWeaponProficiency("Ceremony", 1, "Wisdom", 0),
    NonWeaponProficiency("Diagnostics", 1, "Wisdom", -1),
    NonWeaponProficiency("Diplomacy", 1, "Charisma", -1),
    NonWeaponProficiency("Engineering", 2, "Intelligence", -3),
    NonWeaponProficiency("Genie Lore", 1, "Intelligence", 0),
    NonWeaponProficiency("Healing", 2, "Wisdom", -2),
    NonWeaponProficiency("Herbalism", 2, "Intelligence", -2),
    NonWeaponProficiency("Inquisitor", 2, "Wisdom", 0),
    NonWeaponProficiency("Investigation", 1, "Intelligence", -2),
    NonWeaponProficiency("Languages, Ancient", 1, "Intelligence", 0),
    NonWeaponProficiency("Law", 1, "Intelligence/Wisdom", 0),
    NonWeaponProficiency("Local History", 1, "Charisma", 0),
    NonWeaponProficiency("Musical Instrument", 1, "Dexterity", -1),
    NonWeaponProficiency("Navigation", 1, "Intelligence", -2),
    NonWeaponProficiency("Observation", 1, "Intelligence", 0),
    NonWeaponProficiency("Omen Reading", 1, "Wisdom", -2),
    NonWeaponProficiency("Oratory", 1, "Charisma", -1),
    NonWeaponProficiency("Papermaking", 1, "Intelligence", 0),
    NonWeaponProficiency("Persuasion", 1, "Charisma", -2),
    NonWeaponProficiency("Reading/Writing", 1, "Intelligence", 1),
    NonWeaponProficiency("Religion", 1, "Wisdom", 0),
    NonWeaponProficiency("Sage Knowledge", 2, "Intelligence", -2),
    NonWeaponProficiency("Scribe", 1, "Dexterity", 1),
    NonWeaponProficiency("Soothsaying", 2, "Intelligence", 0),
    NonWeaponProficiency("Spellcraft", 1, "Intelligence", -2),
    NonWeaponProficiency("Undead Lore", 1, "Intelligence", -1),
    NonWeaponProficiency("Veterinary Healing", 1, "Intelligence", -3)
]