class NonWeaponProficiency:
    def __init__(self, name, slots_required, relevant_ability, check_modifier):
        self.name = name
        self.slots_required = slots_required
        self.relevant_ability = relevant_ability
        self.check_modifier = check_modifier

# List of wizard non-weapon proficiencies
wizard_proficiencies = [
    NonWeaponProficiency("Alchemy", 2, "Intelligence", -3),
    NonWeaponProficiency("Alchemy (Warriors & Priests of the Realms)", 3, "Intelligence", -2),
    NonWeaponProficiency("Anatomy", 2, "Intelligence", -2),
    NonWeaponProficiency("Ancient History", 1, "Intelligence", -1),
    NonWeaponProficiency("Arcanology", 1, "Intelligence", -3),
    NonWeaponProficiency("Astrology", 2, "Intelligence", 0),
    NonWeaponProficiency("Astronomy", "N/A", "N/A", "N/A"),
    NonWeaponProficiency("Body Manipulation", 2, "Dexterity", -3),
    NonWeaponProficiency("Bookbinding", 1, "Intelligence", 0),
    NonWeaponProficiency("Concentration", 2, "Wisdom", -2),
    NonWeaponProficiency("Cryptography", "N/A", "N/A", "N/A"),
    NonWeaponProficiency("Dowsing", 1, "Wisdom", -3),
    NonWeaponProficiency("Dowsing (Dragon Magazine 229)", 2, "Wisdom", -1),
    NonWeaponProficiency("Engineering", 2, "Intelligence", -3),
    NonWeaponProficiency("Gem Cutting", 2, "Dexterity", -2),
    NonWeaponProficiency("Genie Lore", 1, "Intelligence", 0),
    NonWeaponProficiency("Glassblowing", 1, "Dexterity", 0),
    NonWeaponProficiency("Herbalism", 2, "Intelligence", -2),
    NonWeaponProficiency("Hypnotism", 1, "Charisma", -2),
    NonWeaponProficiency("Illusion Pierce", 3, "N/A", "N/A"),
    NonWeaponProficiency("Languages, Ancient", 1, "Intelligence", 0),
    NonWeaponProficiency("Mental Resistance", 1, "Wisdom", -1),
    NonWeaponProficiency("Navigation", 1, "Intelligence", -2),
    NonWeaponProficiency("Omen Reading", 1, "Wisdom", -2),
    NonWeaponProficiency("Papermaking", 1, "Intelligence", 0),
    NonWeaponProficiency("Prestidigitation", 1, "Dexterity", -1),
    NonWeaponProficiency("Reading/Writing", 1, "Intelligence", 1),
    NonWeaponProficiency("Religion", 1, "Wisdom", 0),
    NonWeaponProficiency("Research", 1, "Intelligence", 0),
    NonWeaponProficiency("Sage Knowledge", 2, "Intelligence", -2),
    NonWeaponProficiency("Scribe", 1, "Dexterity", 1),
    NonWeaponProficiency("Spellcraft", 1, "Intelligence", -2),
    NonWeaponProficiency("Tactics of Magic", 1, "Intelligence", -1),
    NonWeaponProficiency("Thaumaturgy", 1, "Intelligence", -2),
    NonWeaponProficiency("Vapor Weave", 3, "Constitution", -3)
]