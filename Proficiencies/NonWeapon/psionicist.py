class NonWeaponProficiency:
    def __init__(self, name, slots_required, relevant_ability, check_modifier):
        self.name = name
        self.slots_required = slots_required
        self.relevant_ability = relevant_ability
        self.check_modifier = check_modifier

# Psionicist non-weapon proficiencies
psionicist_proficiencies = [
    NonWeaponProficiency("Crystal Focus", 1, "Wisdom", -1),
    NonWeaponProficiency("Gem Cutting", 2, "Dexterity", -2),
    NonWeaponProficiency("Harness Subconscious", 2, "Wisdom", -1),
    NonWeaponProficiency("Meditative Focus", 1, "Wisdom", 1),
    NonWeaponProficiency("Musical Instrument", 1, "Dexterity", -1),
    NonWeaponProficiency("Power Manipulation", 2, "Intelligence", -4),
    NonWeaponProficiency("Psionic Lore", 1, "Intelligence", 1),
    NonWeaponProficiency("Reading/Writing", 1, "Intelligence", 1),
    NonWeaponProficiency("Rejuvenation", 1, "Wisdom", -1),
    NonWeaponProficiency("Religion", 1, "Wisdom", 0)
]