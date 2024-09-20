class TackAndHarnessManager:
    def __init__(self):
        # Dictionary of tack and harness items with their cost and weight
        self.tack_and_harness_items = {
            "Barding (Chain)": {"cost": "500 gp", "weight": "70 lbs."},
            "Barding (Full plate)": {"cost": "2,000 gp", "weight": "85 lbs."},
            "Barding (Full scale)": {"cost": "1,000 gp", "weight": "75 lbs."},
            "Barding (Half brigandine)": {"cost": "500 gp", "weight": "45 lbs."},
            "Barding (Half padded)": {"cost": "100 gp", "weight": "25 lbs."},
            "Barding (Half scale)": {"cost": "500 gp", "weight": "50 lbs."},
            "Barding (Leather or padded)": {"cost": "150 gp", "weight": "60 lbs."},
            "Bit and bridle": {"cost": "15 sp", "weight": "3 lbs."},
            "Cart harness": {"cost": "2 gp", "weight": "10 lbs."},
            "Halter": {"cost": "5 cp", "weight": "*"},
            "Horseshoes & shoeing": {"cost": "1 gp", "weight": "10 lbs."},
            "Saddle (Pack)": {"cost": "5 gp", "weight": "15 lbs."},
            "Saddle (Riding)": {"cost": "10 gp", "weight": "35 lbs."},
            "Saddle bags (Large)": {"cost": "4 gp", "weight": "8 lbs."},
            "Saddle bags (Small)": {"cost": "3 gp", "weight": "5 lbs."},
            "Saddle blanket": {"cost": "3 sp", "weight": "4 lbs."},
            "Yoke (Horse)": {"cost": "5 gp", "weight": "15 lbs."},
            "Yoke (Ox)": {"cost": "3 gp", "weight": "20 lbs."}
        }

    def purchase_item(self, character, item):
        # Check if the item exists in the tack and harness items list
        if item in self.tack_and_harness_items:
            item_data = self.tack_and_harness_items[item]
            cost = item_data["cost"]
            weight = item_data["weight"]
            print(f"{character} purchased {item}: Cost = {cost}, Weight = {weight}.")
        else:
            print(f"Item '{item}' not found in the tack and harness list.")

    def get_item_info(self, item):
        # Return the cost and weight of an item
        return self.tack_and_harness_items.get(item, "Item not found")


# Example usage with the character class
class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def purchase(self, tack_and_harness_manager, item):
        tack_and_harness_manager.purchase_item(self.name, item)
        self.inventory.append(item)


# Example usage
tack_and_harness_manager = TackAndHarnessManager()
character = Character("Barcus")

# Purchase some items
character.purchase(tack_and_harness_manager, "Saddle (Riding)")
character.purchase(tack_and_harness_manager, "Barding (Full plate)")

# Print the character's inventory
print(f"{character.name}'s inventory: {character.inventory}")
