#Fantasy Game Inventory

def display_inventory(inventory):
    total = 0
    print ('Inventory:')
    for k, v in inventory.items():
        print (str(v)+' ' + k)
        total += v
    print ('Total number of items: '+ str(total))

def add_to_inventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory 

if __name__ == '__main__':
    inv = {'gold coin': 42, 'rope': 1}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragonLoot)
    display_inventory(inv)
