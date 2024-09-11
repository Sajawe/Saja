def displayInventory(inventory):
    # Print the header
    print("Inventory:")
    
    # Calculate the total number of items
    total_items = sum(inventory.values())
    
    # Sort the inventory items alphabetically by item name
    for item in sorted(inventory.keys()):
        # Print each item with its quantity
        print(f"{inventory[item]} {item}")
    
    # Print the total number of items
    print(f"Total number of items: {total_items}")

# Example usage
inventory = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
}

displayInventory(inventory)
