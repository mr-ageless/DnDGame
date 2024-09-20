class FoodAndLodgingManager:
    def __init__(self):
        # Dictionary of food and lodging items and their costs
        self.food_and_lodging_items = {
            "Ale (per gallon)": "2 sp",
            "Banquet (per person)": "10 gp",
            "Bread": "5 cp",
            "Cheese": "4 sp",
            "City rooms (per month), Common": "20 gp",
            "City rooms (per month), Poor": "6 sp",
            "Common wine (pitcher)": "2 sp",
            "Egg or fresh vegetables": "1 cp",
            "Grain and stabling for horse (daily)": "5 sp",
            "Honey": "5 sp",
            "Inn lodging (per day), Common": "5 sp",
            "Inn lodging (per week), Common": "3 gp",
            "Inn lodging (per day), Poor": "5 cp",
            "Inn lodging (per week), Poor": "2 sp",
            "Meat for one meal": "1 sp",
            "Meals (per day), Good": "5 sp",
            "Meals (per day), Common": "3 sp",
            "Meals (per day), Poor": "1 sp",
            "Separate latrine for rooms (per month)": "2 gp",
            "Small beer (per gallon)": "5 cp",
            "Soup": "5 cp"
        }

    def purchase_item(self, character, item):
        # Check if the item exists in the list of food and lodging items
        if item in self.food_and_lodging_items:
            cost = self.food_and_lodging_items[item]
            print(f"{character} purchased {item}, which costs {cost}.")
        else:
            print(f"Item '{item}' not found in the food and lodging items list.")

    def get_item_cost(self, item):
        # Return the cost of an item
        return self.food_and_lodging_items.get(item, "Item not found")


# Example of how to use this class with other classes
class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []
    
    def purchase(self, food_and_lodging_manager, item):
        food_and_lodging_manager.purchase_item(self.name, item)
        self.inventory.append(item)


# Example usage
food_and_lodging_manager = FoodAndLodgingManager()
character = Character("Barcus")

# Purchase some items
character.purchase(food_and_lodging_manager, "Bread")
character.purchase(food_and_lodging_manager, "Inn lodging (per day), Common")

# Print the character's inventory
print(f"{character.name}'s inventory: {character.inventory}")
