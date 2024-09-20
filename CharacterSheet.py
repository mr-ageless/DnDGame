class CharacterSheet:
    def __init__(self, name='', character_class='', race='', hit_die = 0, strength=10, dexterity=10, constitution=10, intelligence=10, wisdom=10, charisma=10):
        self.name = name
        self.character_class = character_class
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hit_die = hit_die

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Class: {self.character_class}\n"
                f"Race: {self.race}\n"
                f"Strength: {self.strength}\n"
                f"Dexterity: {self.dexterity}\n"
                f"Constitution: {self.constitution}\n"
                f"Intelligence: {self.intelligence}\n"
                f"Wisdom: {self.wisdom}\n"
                f"Charisma: {self.charisma}\n"
                f"Hit Die: {self.hit_die}\n")
                
