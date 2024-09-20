class MiscellaneousEquipmentManager:
    def __init__(self):
        # Dictionary of miscellaneous equipment items with their cost and weight
        self.miscellaneous_items = {
            "Backpack": {"cost": "2 gp", "weight": "2 lbs."},
            "Barrel, small": {"cost": "2 gp", "weight": "30 lbs."},
            "Basket (Large)": {"cost": "3 sp", "weight": "1 lbs."},
            "Basket (Small)": {"cost": "5 cp", "weight": "*"},
            "Bell": {"cost": "1 gp", "weight": "—"},
            "Belt pouch (Large)": {"cost": "1 gp", "weight": "1 lbs."},
            "Belt pouch (Small)": {"cost": "7 sp", "weight": "1/2 lbs."},
            "Block and tackle": {"cost": "5 gp", "weight": "5 lbs."},
            "Bolt case": {"cost": "1 gp", "weight": "1 lbs."},
            "Bucket": {"cost": "5 sp", "weight": "3 lbs."},
            "Chain (Heavy, per ft.)": {"cost": "4 gp", "weight": "3 lbs."},
            "Chain (Light, per ft.)": {"cost": "3 gp", "weight": "1 lbs."},
            "Chest (Large)": {"cost": "2 gp", "weight": "25 lbs."},
            "Chest (Small)": {"cost": "1 gp", "weight": "10 lbs."},
            "Cloth (Common, per 10 sq. yds.)": {"cost": "7 gp", "weight": "10 lbs."},
            "Cloth (Fine, per 10 sq. yds.)": {"cost": "50 gp", "weight": "10 lbs."},
            "Cloth (Rich, per 10 sq. yds.)": {"cost": "100 gp", "weight": "10 lbs."},
            "Candle": {"cost": "1 cp", "weight": "*"},
            "Canvas (per sq. yard)": {"cost": "4 sp", "weight": "1 lbs."},
            "Chalk": {"cost": "1 cp", "weight": "*"},
            "Crampons": {"cost": "4 gp", "weight": "2 lbs."},
            "Fishhook": {"cost": "1 sp", "weight": "**"},
            "Fishing net (10 ft. sq.)": {"cost": "4 gp", "weight": "5 lbs."},
            "Flint and steel": {"cost": "5 sp", "weight": "*"},
            "Glass bottle": {"cost": "10 gp", "weight": "*"},
            "Grappling hook": {"cost": "8 sp", "weight": "4 lbs."},
            "Holy item (symbol, water, etc.)": {"cost": "25 gp", "weight": "*"},
            "Hourglass": {"cost": "25 gp", "weight": "1 lbs."},
            "Iron pot": {"cost": "5 sp", "weight": "2 lbs."},
            "Ladder (10 ft.)": {"cost": "5 cp", "weight": "20 lbs."},
            "Lantern (Beacon)": {"cost": "150 gp", "weight": "50 lbs."},
            "Lantern (Bullseye)": {"cost": "12 gp", "weight": "3 lbs."},
            "Lantern (Hooded)": {"cost": "7 gp", "weight": "2 lbs."},
            "Lock (Good)": {"cost": "100 gp", "weight": "1 lbs."},
            "Lock (Poor)": {"cost": "20 gp", "weight": "1 lbs."},
            "Magnifying glass": {"cost": "100 gp", "weight": "*"},
            "Map or scroll case": {"cost": "8 sp", "weight": "1/2 lbs."},
            "Merchant's scale": {"cost": "2 gp", "weight": "1 lbs."},
            "Mirror, small metal": {"cost": "10 gp", "weight": "*"},
            "Musical instrument": {"cost": "5-100 gp", "weight": "1/2-3 lbs."},
            "Oil (per flask)": {"cost": "—", "weight": "—"},
            "Greek fire": {"cost": "10 gp", "weight": "2 lbs."},
            "Lamp": {"cost": "6 cp", "weight": "1 lbs."},
            "Paper (per sheet)": {"cost": "2 gp", "weight": "**"},
            "Papyrus (per sheet)": {"cost": "8 sp", "weight": "**"},
            "Parchment (per sheet)": {"cost": "1 gp", "weight": "**"},
            "Perfume (per vial)": {"cost": "5 gp", "weight": "*"},
            "Piton": {"cost": "3 cp", "weight": "1/2 lbs."},
            "Quiver": {"cost": "8 sp", "weight": "1 lbs."},
            "Rope (Hemp, per 50 ft.)": {"cost": "1 gp", "weight": "20 lbs."},
            "Rope (Silk, per 50 ft.)": {"cost": "10 gp", "weight": "8 lbs."},
            "Sack (Large)": {"cost": "2 sp", "weight": "1/2 lbs."},
            "Sack (Small)": {"cost": "5 cp", "weight": "*"},
            "Sealing/candle wax (per lb.)": {"cost": "1 gp", "weight": "1 lbs."},
            "Sewing needle": {"cost": "5 sp", "weight": "*"},
            "Signal whistle": {"cost": "8 sp", "weight": "*"},
            "Signet ring or personal seal": {"cost": "5 gp", "weight": "*"},
            "Soap (per lb.)": {"cost": "5 sp", "weight": "1 lbs."},
            "Spyglass": {"cost": "1,000 gp", "weight": "1 lbs."},
            "Tent (Large)": {"cost": "25 gp", "weight": "20 lbs."},
            "Tent (Pavilion)": {"cost": "100 gp", "weight": "50 lbs."},
            "Tent (Small)": {"cost": "5 gp", "weight": "10 lbs."},
            "Thieves' picks": {"cost": "30 gp", "weight": "1 lbs."},
            "Torch": {"cost": "1 cp", "weight": "1 lbs."},
            "Water clock": {"cost": "1,000 gp", "weight": "200 lbs."},
            "Whetstone": {"cost": "2 cp", "weight": "1 lbs."},
            "Wineskin": {"cost": "8 sp", "weight": "1 lbs."},
            "Winter blanket": {"cost": "5 sp", "weight": "3 lbs."},
            "Writing ink (per vial)": {"cost": "8 gp", "weight": "*"}
        }

    def purchase_item(self, character, item):
        # Check if the item exists in the miscellaneous items list
        if item in self.miscellaneous_items:
            item_data = self.miscellaneous_items[item]
            cost = item_data["cost"]
            weight = item_data["weight"]
            print(f"{character} purchased {item}: Cost = {cost}, Weight = {weight}.")
        else:
            print(f"Item '{item}' not found in the miscellaneous equipment list.")

    def get_item_info(self, item):
        # Return the cost and weight of an item
        return self.miscellaneous_items.get(item, "Item not found")


# Example usage with the character class
class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def purchase(self, miscellaneous_equipment_manager, item):
        miscellaneous_equipment_manager.purchase_item(self.name, item)
        self.inventory.append(item)


# Example usage
miscellaneous_equipment_manager = MiscellaneousEquipmentManager()
character = Character("Barcus")

# Purchase some items
character.purchase(miscellaneous_equipment_manager, "Backpack")
character.purchase(miscellaneous_equipment_manager, "Spyglass")

# Print the character's inventory
print(f"{character.name}'s inventory: {character.inventory}")
