'''
DEVELOPER(S): Param Raj
COLLABORATORS: None
DATE: 4/15/26
'''

"""
The Photography Gear & Packing Manager

This program tracks photography equipment inventory and creates packing lists
for different types of photo shoots

I utilized a Dictionary for the main inventory becuase it allows the user to map
the gear's name with it's specific details. This makes it easy to retrieve the data
in an organized fashion for the users

I did, however, use a list for the 'Shoot Packing List' because that section was meant
to be more of a quick, sequential list where the order mattered for the user's priorities.  
"""

##########################################
# FUNCTIONS:
##########################################

def load_gear(filename):                                     #Reads the gear from the file and returns a dictionary.
   
    inventory = {}
    try:
        file = open(filename, "r")
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 2:
                inventory[parts[0]] = parts[1]
        file.close()
    except FileNotFoundError:
        print("Inventory file not found. Creating a new one on exit.")
    return inventory
    

def save_gear(filename, inventory):                          #Saves dictionary to a file.
    
    file = open(filename, "w")
    for item , detail in inventory.items():
        file.write(item + "," + detail + "\n")
    file.close()


##########################################
# MAIN PROGRAM:
##########################################

def main():
    
    gear_file = "camera_gear.txt"
    my_gear = load_gear(gear_file)

    print("--- Photography Gear + Packing Manager ---")

    while True:
        print("\n1. View Inventory")
        print("2. Add New Gear")
        print("3. Create Shoot Packing List")
        print("4. Save and Exit")

        choice = input("Select an option: ")

        if choice == "1":
            print("\n--- Current Equipment ---")
            print(f"{'Item':<20} | {'Details':<15}")
            print("-" * 40)
            for item, detail in my_gear.items():
                print(f"{item:<20} | {detail:<15}")

        elif choice == "2":
            new_item = input("Enter item name: ")
            detail = input("Enter detail (e.g. aperture or type): ")
            my_gear[new_item] = detail
            print(f"Added {new_item} to inventory.")

        elif choice == "3":
            packing_list = []
            print("\n--- Packing List Creator ---")
            print("Enter items to pack (type 'done' when finished): ")

            while True:
                item = input("> ")
                if item.lower() == 'done':
                    break
                packing_list.append(item)
            
            print("\nFinal Checklist for you shoot:")
            for i in range(len(packing_list)):
                print(f"{i+1}. [ ] {packing_list[i]}")
        
        elif choice == "4":
            save_gear(gear_file, my_gear)
            print("Changes saved. Good luck with your next shoot!")
            break
        else:
            print("Invalid choice. Please select a number 1-4")
main()
