theInventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(message, inventory):
    print(message)
    totalCount = 0
    for k, v in inventory.items():
        totalCount += v
        print(' ' + str(v) + ' ' + k)
    print('Total number of items: ' + str(totalCount))

def addToInventory(inventory, addedItems):
    for v in addedItems:
        inventory.setdefault(v, 0)
        inventory[v] += 1

displayInventory('Inventory before dragon was vanquished', theInventory)
addToInventory(theInventory, dragonLoot)
displayInventory('Inventory after dragon was vanquished', theInventory)