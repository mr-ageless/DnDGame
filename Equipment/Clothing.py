class ClothingManager:
    def __init__(self):
        # Dictionary of clothing items and their costs
        self.clothing_items = {
            "Belt": "3 sp",
            "Boots, Riding": "3 gp",
            "Boots, Soft": "1 gp",
            "Breeches": "2 gp",
            "Cap, Hat": "1 sp",
            "Cloak, Good cloth": "8 sp",
            "Cloak, Fine fur": "50 gp",
            "Girdle": "3 gp",
            "Gloves": "1 gp",
            "Gown, Common": "12 sp",
            "Hose": "2 gp",
            "Knife sheath": "3 cp",
            "Mittens": "3 sp",
            "Pin": "6 gp",
            "Brooch, Plain": "10 gp",
            "Robe, Common": "9 sp",
            "Robe, Embroidered": "20 gp",
            "Sandals": "5 cp",
            "Sash": "2 sp",
            "Shoes": "1 gp",
            "Silk Jacket": "80 gp",
            "Surcoat": "6 sp",
            "Sword scabbard, hanger, baldric": "4 gp",
            "Tabard": "6 sp",
            "Toga, Coarse": "8 cp",
            "Tunic": "8 sp",
            "Vest": "6 sp"
        }

    def equip_item(self, character, item):
        # Check if the item is in the list of clothing items
        if item in self.clothing_items:
            cost = self.clothing_items[item]
            print(f"{character} is now equipped with {item}, which costs {cost}.")
        else:
            print(f"Item '{item}' not found in the clothing items list.")

    def get_item_cost(self, item):
        # Return the cost of an item
        return self.clothing_items.get(item, "Item not found")


# Example of how to use this class with other classes
class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def equip(self, clothing_manager, item):
        clothing_manager.equip_item(self.name, item)
        self.inventory.append(item)


# Example usage
clothing_manager = ClothingManager()
character = Character("Barcus")

# Equip the character with some items
character.equip(clothing_manager, "Breeches")
character.equip(clothing_manager, "Silk Jacket")

# Print the character's inventory
print(f"{character.name}'s inventory: {character.inventory}")
