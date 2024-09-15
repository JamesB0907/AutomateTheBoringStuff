dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

character_inventory = {'thieves tools': 1, 'trap disarming kit': 1, 'daggers': 3, 'gold coin': 100, 'healing potion': 2}

def display_inventory(inventory):
    item_count = 0
    print('Inventory:')
    for item, quantity in inventory.items():
        print(f'  - {quantity} {item}')
        if item != 'gold coin':
            item_count += quantity
    print(f'Total number of items: {item_count}')


display_inventory(character_inventory)

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

character_inventory = add_to_inventory(character_inventory, dragon_loot)

display_inventory(character_inventory)


