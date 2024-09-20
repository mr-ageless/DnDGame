class HouseholdProvisioningManager:
    def __init__(self):
        # Dictionary of household provisioning items and their costs
        self.household_items = {
            "Barrel of pickled fish": "3 gp",
            "Butter (per lb.)": "2 sp",
            "Coarse sugar (per lb.)": "1 gp",
            "Dry rations (per week)": "10 gp",
            "Eggs (per 100)": "8 sp",
            "Eggs (per two dozen)": "2 sp",
            "Figs (per lb.)": "3 sp",
            "Firewood (per day)": "1 cp",
            "Herbs (per lb.)": "5 cp",
            "Nuts (per lb.)": "1 gp",
            "Raisins (per lb.)": "2 sp",
            "Rice (per lb.)": "2 sp",
            "Salt (per lb.)": "1 sp",
            "Salted herring (per 100)": "1 gp",
            "Exotic spice (per lb.)": "15 gp",
            "Rare spice (per lb.)": "2 gp",
            "Uncommon spice (per lb.)": "1 gp",
            "Tun of cider (250 gal.)": "8 gp",
            "Tun of good wine (250 gal.)": "20 gp"
        }

    def purchase_item(self, character, item):
        # Check if the item exists in the household items list
        if item in self.household_items:
            cost = self.household_items[item]
            print(f"{character} purchased {item}, which costs {cost}.")
        else:
            print(f"Item '{item}' not found in the household items list.")

    def get_item_cost(self, item):
        # Return the cost of an item
        return self.household_items.get(item, "Item not found")


# Example of how to use this class with other classes
class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def purchase(self, household_manager, item):
        household_manager.purchase_item(self.name, item)
        self.inventory.append(item)


# Example usage
household_manager = HouseholdProvisioningManager()
character = Character("Barcus")

# Purchase some items
character.purchase(household_manager, "Butter (per lb.)")
character.purchase(household_manager, "Salt (per lb.)")

# Print the character's inventory
print(f"{character.name}'s inventory: {character.inventory}")
