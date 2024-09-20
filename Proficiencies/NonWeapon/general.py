class NonWeaponProficiency:
    def __init__(self, name, slots_required, relevant_ability, check_modifier):
        self.name = name
        self.slots_required = slots_required
        self.relevant_ability = relevant_ability
        self.check_modifier = check_modifier

# List of general non-weapon proficiencies
general_proficiencies = [
    NonWeaponProficiency("Agriculture", 1, "Intelligence", 0),
    NonWeaponProficiency("Alertness", 1, "Wisdom", 1),
    NonWeaponProficiency("Animal Handling", 1, "Wisdom", -1),
    NonWeaponProficiency("Animal Rending", 1, "Dexterity", 2),
    NonWeaponProficiency("Animal Training", 1, "Wisdom", 0),
    NonWeaponProficiency("Artistic Ability", 1, "Wisdom", 0),
    NonWeaponProficiency("Begging", 1, "Charisma", "Special"),
    NonWeaponProficiency("Blacksmithing", 1, "Strength", 0),
    NonWeaponProficiency("Boat Piloting", None, None, None),
    NonWeaponProficiency("Boating", 1, "Wisdom", 1),
    NonWeaponProficiency("Boatwright", 1, "Intelligence", -2),
    NonWeaponProficiency("Brewing", 1, "Intelligence", 0),
    NonWeaponProficiency("Carpentry", 1, "Strength", 0),
    NonWeaponProficiency("Cartography", 1, "Intelligence", -2),
    NonWeaponProficiency("Cheesemaking", 1, "Intelligence", 0),
    NonWeaponProficiency("City Familiarity", 1, "Intelligence", 0),
    NonWeaponProficiency("Clothesmaking, Crude", 1, "Intelligence", -1),
    NonWeaponProficiency("Cobbling", 1, "Dexterity", 0),
    NonWeaponProficiency("Contact", 1, "Wisdom", 0),
    NonWeaponProficiency("Cooking", 1, "Intelligence", 0),
    NonWeaponProficiency("Curtain Cognizance", 2, "Intelligence", -2),
    NonWeaponProficiency("Dancing", 1, "Dexterity", 0),
    NonWeaponProficiency("Danger Sense", 2, "Wisdom", 1),
    NonWeaponProficiency("Debate", 1, "Intelligence", 0),
    NonWeaponProficiency("Direction Sense", 1, "Wisdom", 1),
    NonWeaponProficiency("Distance Sense", 1, "Wisdom", 1),
    NonWeaponProficiency("Drinking", 1, "Constitution", 0),
    NonWeaponProficiency("Dwarf Runes", 1, "Intelligence", 2),
    NonWeaponProficiency("Eating", 1, "Constitution", 0),
    NonWeaponProficiency("Ethereal Sight", 1, "Wisdom", -1),
    NonWeaponProficiency("Etiquette", 1, "Charisma", 0),
    NonWeaponProficiency("Feign Magic", 1, "Intelligence", -1),
    NonWeaponProficiency("Fire-building", 1, "Wisdom", -1),
    NonWeaponProficiency("Fishing", 1, "Wisdom", -1),
    NonWeaponProficiency("Flintworking", 1, "Dexterity", 1),
    NonWeaponProficiency("Folklore", 1, "Charisma", 0),
    NonWeaponProficiency("Foraging", 1, "Intelligence", -2),
    NonWeaponProficiency("Fungi Recognition", 1, "Intelligence", 3),
    NonWeaponProficiency("Haggling", 2, "Wisdom", 0),
    NonWeaponProficiency("Heraldry", 1, "Intelligence", 0),
    NonWeaponProficiency("Hiding", 2, "Intelligence", -1),
    NonWeaponProficiency("Languages, Modern", 1, "Intelligence", 0),
    NonWeaponProficiency("Leatherworking", 1, "Intelligence", 0),
    NonWeaponProficiency("Local Dwarf History", 1, "Charisma", 2),
    NonWeaponProficiency("Mental Armor", 1, "Wisdom", -2),
    NonWeaponProficiency("Metalworking", 1, "Dexterity", 0),
    NonWeaponProficiency("Mining", 2, "Wisdom", -3),
    NonWeaponProficiency("Nutriment", 1, "Wisdom", -2),
    NonWeaponProficiency("Painting", None, None, None),
    NonWeaponProficiency("Poetry", 1, "Intelligence", -2),
    NonWeaponProficiency("Pottery", 1, "Dexterity", -2),
    NonWeaponProficiency("Prospecting", 1, "Dexterity", -1),
    NonWeaponProficiency("Psychic Defense", 2, "Wisdom", -2),
    NonWeaponProficiency("Riding, Airborne", 2, "Wisdom", -2),
    NonWeaponProficiency("Riding, Land-Based", 1, "Wisdom", 3),
    NonWeaponProficiency("Riding, Sea-based", 2, "Dexterity", -2),
    NonWeaponProficiency("Rope Use", 1, "Dexterity", 0),
    NonWeaponProficiency("Sculpting", None, None, None),
    NonWeaponProficiency("Seamanship", 1, "Dexterity", 1),
    NonWeaponProficiency("Seamstress/Tailor", 1, "Dexterity", -1),
    NonWeaponProficiency("Signalling", 1, "Intelligence", 2),
    NonWeaponProficiency("Sign Language", 1, "Intelligence", 2),
    NonWeaponProficiency("Singing", 1, "Charisma", 0),
    NonWeaponProficiency("Slow Respiration", 1, None, None),
    NonWeaponProficiency("Smelting", 1, "Intelligence", 0),
    NonWeaponProficiency("Sound Analysis", 1, "Wisdom", 0),
    NonWeaponProficiency("Stonemasonry", 1, "Strength", -2),
    NonWeaponProficiency("Survival, Underground", 1, "Intelligence", 0),
    NonWeaponProficiency("Swimming", 1, "Strength", 0),
    NonWeaponProficiency("Underground Navigation", 1, "Intelligence", 0),
    NonWeaponProficiency("Underwater Riding", 2, "Dexterity", -2),
    NonWeaponProficiency("Voice Mimicry", 2, "Charisma", "Special"),
    NonWeaponProficiency("Weather Sense", 1, "Wisdom", -1),
    NonWeaponProficiency("Weaving", 1, "Intelligence", -1),
    NonWeaponProficiency("Winemaking", 1, "Intelligence", 0)
]