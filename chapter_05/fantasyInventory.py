theInventory={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print('Inventory:')
    totalCount = 0
    for k, v in inventory.items():
        totalCount += v
        print(str(v) + ' ' + k)
    print('Total number of items: ' + str(totalCount))

displayInventory(theInventory)