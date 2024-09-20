class NonWeaponProficiency:
    def __init__(self, name, slots_required, relevant_ability, check_modifier):
        self.name = name
        self.slots_required = slots_required
        self.relevant_ability = relevant_ability
        self.check_modifier = check_modifier

        # Chronomancer non-weapon proficiencies
chronomancer_proficiencies = [
    NonWeaponProficiency("Appraising", 1, "Intelligence", 0),
    NonWeaponProficiency("Disguise", 1, "Charisma", -1),
    NonWeaponProficiency("Future History", 1, "Intelligence", -2),
    NonWeaponProficiency("Languages, Future", 1, "Intelligence", 0),
    NonWeaponProficiency("Local History", 1, "Charisma", 0),
    NonWeaponProficiency("Prophecy", 1, "Wisdom", -1),
    NonWeaponProficiency("Time Sense", 1, "Wisdom", -2)
]