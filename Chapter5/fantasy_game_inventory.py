# You are creating a fantasy video game. The data structure to model the player’s inventory will be a dictionary where the keys are string values describing the item in the inventory and the value is an integer value detailing how many of that item the player has. For example, the dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the player has 1 rope, 6 torches, 42 gold coins, and so on.
import pprint

character_inventory = {'thieves tools': 1, 'trap disarming kit': 1, 'daggers': 3, 'gold coins': 100, 'healing potion': 2}

def display_inventory(inventory):
    item_count = 0
    print('Inventory:')
    for item, quantity in inventory.items():
        print(f'  - {quantity} {item}')
        if item != 'gold coins':
            item_count += quantity
    print(f'Total number of items: {item_count}')


display_inventory(character_inventory)