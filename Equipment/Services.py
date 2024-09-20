class ServiceManager:
    def __init__(self):
        # Dictionary of services and their costs
        self.service_items = {
            "Bath": "3 cp",
            "Clerk (per letter)": "2 sp",
            "Doctor, leech, or bleeding": "3 gp",
            "Guide, in city (per day)": "2 sp",
            "Lantern or torchbearer (per night)": "1 sp",
            "Laundry (by load)": "1 cp",
            "Messenger, in city (per message)": "1 sp",
            "Minstrel (per performance)": "3 gp",
            "Mourner (per funeral)": "2 sp",
            "Teamster w/wagon (per mile)": "1 sp"
        }

    def purchase_item(self, character, item):
        # Check if the item exists in the service items list
        if item in self.service_items:
            cost = self.service_items[item]
            print(f"{character} purchased the service: {item}, which costs {cost}.")
        else:
            print(f"Service '{item}' not found in the service items list.")

    def get_item_cost(self, item):
        # Return the cost of a service
        return self.service_items.get(item, "Service not found")


# Example of how to use this class with other classes
class Character:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def purchase(self, service_manager, item):
        service_manager.purchase_item(self.name, item)
        self.inventory.append(item)


# Example usage
service_manager = ServiceManager()
character = Character("Barcus")

# Purchase some services
character.purchase(service_manager, "Doctor, leech, or bleeding")
character.purchase(service_manager, "Minstrel (per performance)")

# Print the character's inventory
print(f"{character.name}'s inventory: {character.inventory}")
