class AnimalManager:
    def __init__(self):
        # Dictionary of animals and their costs
        self.animal_items = {
            "Boar": "10 gp",
            "Bull": "20 gp",
            "Calf": "5 gp",
            "Camel": "50 gp",
            "Capon": "3 cp",
            "Cat": "1 sp",
            "Chicken": "2 cp",
            "Cow": "10 gp",
            "Dog (Guard)": "25 gp",
            "Dog (Hunting)": "17 gp",
            "Dog (War)": "20 gp",
            "Donkey, mule, or ass": "8 gp",
            "Elephant (Labor)": "200 gp",
            "Elephant (War)": "500 gp",
            "Falcon (trained)": "1,000 gp",
            "Goat": "1 gp",
            "Goose": "5 cp",
            "Guinea hen": "2 cp",
            "Horse (Draft)": "200 gp",
            "Horse (Heavy war)": "400 gp",
            "Horse (Light war)": "150 gp",
            "Horse (Medium war)": "225 gp",
            "Horse (Riding)": "75 gp",
            "Hunting cat (jaguar, etc.)": "5,000 gp",
            "Ox": "15 gp",
            "Partridge": "5 cp",
            "Peacock": "5 sp",
            "Pig": "3 gp",
            "Pigeon": "1 cp",
            "Pigeon (Homing)": "100 gp",
            "Pony": "30 gp",
            "Ram": "4 gp",
            "Sheep": "2 gp",
            "Songbird": "10 sp",
            "Swan": "5 sp"
        }

    def purchase_item(self, character, item):
        # Check if the item exists in the animal items list
        if item in self.animal_items:
            cost = self.animal_items[item]
            print(f"{character} purchased {item}, which costs {cost}.")
        else:
            print(f"Item '{item}' not found in the animal items list.")

    def get_item_cost(self, item):
        # Return the cost of an item
        return self.animal_items.get(item, "Item not found")


# Example of how to use this class with other classes
class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def purchase(self, animal_manager, item):
        animal_manager.purchase_item(self.name, item)
        self.inventory.append(item)


# Example usage
animal_manager = AnimalManager()
character = Character("Barcus")

# Purchase some animals
character.purchase(animal_manager, "Falcon (trained)")
character.purchase(animal_manager, "Horse (Riding)")

# Print the character's inventory
print(f"{character.name}'s inventory: {character.inventory}")
