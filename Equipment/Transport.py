class TransportManager:
    def __init__(self):
        # Dictionary of transport items and their costs
        self.transport_items = {
            "Barge": "500 gp",
            "Canoe (Small)": "30 gp",
            "Canoe (War)": "50 gp",
            "Caravel": "10,000 gp",
            "Carriage (Common)": "150 gp",
            "Carriage (Coach, ornamented)": "7,000 gp",
            "Chariot (Riding)": "200 gp",
            "Chariot (War)": "500 gp",
            "Coaster": "5,000 gp",
            "Cog": "10,000 gp",
            "Curragh": "500 gp",
            "Drakkar": "25,000 gp",
            "Dromond": "15,000 gp",
            "Galleon": "50,000 gp",
            "Great galley": "30,000 gp",
            "Knarr": "3,000 gp",
            "Longship": "10,000 gp",
            "Oar (Common)": "2 gp",
            "Oar (Galley)": "10 gp",
            "Raft or small keelboat": "100 gp",
            "Sail": "20 gp",
            "Sedan chair": "100 gp",
            "Wagon or cart wheel": "5 gp"
        }

    def purchase_item(self, character, item):
        # Check if the item exists in the transport items list
        if item in self.transport_items:
            cost = self.transport_items[item]
            print(f"{character} purchased {item}, which costs {cost}.")
        else:
            print(f"Item '{item}' not found in the transport items list.")

    def get_item_cost(self, item):
        # Return the cost of an item
        return self.transport_items.get(item, "Item not found")


# Example of how to use this class with other classes
class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def purchase(self, transport_manager, item):
        transport_manager.purchase_item(self.name, item)
        self.inventory.append(item)


# Example usage
transport_manager = TransportManager()
character = Character("Barcus")

# Purchase some transport items
character.purchase(transport_manager, "Barge")
character.purchase(transport_manager, "Oar (Common)")

# Print the character's inventory
print(f"{character.name}'s inventory: {character.inventory}")
