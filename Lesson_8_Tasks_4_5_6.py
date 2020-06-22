# Pavel Krupenya
# Storage

class Storage:

    storage_total = {}
    count = 0
    branch = {}
    basket = {}

    @staticmethod
    def branch_to_storage():
        print("Move item from branch to storage")
        i = int(input("Please enter item number -  "))
        Storage.storage_total[i] = Storage.branch[i]
        del Storage.branch[i]

    @staticmethod
    def storage_to_branch():
        print("Move item from storage to branch")
        i = int(input("Please enter item number -  "))
        Storage.branch[i] = Storage.storage_total[i]
        del Storage.storage_total[i]

    @staticmethod
    def storage_to_basket():
        print("Move item to basket")
        i = int(input("Please enter item number -  "))
        Storage.basket[i] = Storage.storage_total[2]
        del Storage.storage_total[i]

    @staticmethod
    def clean_basket():
        print("Clean basket")
        Storage.basket = {}

class Office_equipment:
    def __init__(self, equipment_name, equipment_model):
        self.equipment_name = equipment_name
        self.equipment_model = equipment_model

    count = 0

class Printers(Office_equipment):
    def __init__(self, equipment_name, equipment_model, equipment_type):
        self.equipment_name = equipment_name
        self.equipment_model = equipment_model
        self.equipment_type = equipment_type
        Office_equipment.count += 1
        Storage.count += 1
        (Storage.storage_total)[Storage.count] = {"printers": [self.equipment_name, self.equipment_model, self.equipment_type]}

class Scanners(Office_equipment):
    def __init__(self, equipment_name, equipment_model, equipment_type):
        self.equipment_name = equipment_name
        self.equipment_model = equipment_model
        self.equipment_type = equipment_type
        Office_equipment.count += 1
        Storage.count += 1
        (Storage.storage_total)[Storage.count] = {"scanner": [self.equipment_name, self.equipment_model, self.equipment_type]}

class Copiers(Office_equipment):
    def __init__(self, equipment_name, equipment_model, equipment_type):
        self.equipment_name = equipment_name
        self.equipment_model = equipment_model
        self.equipment_type = equipment_type
        Office_equipment.count += 1
        Storage.count += 1
        (Storage.storage_total)[Storage.count] = {"copier": [self.equipment_name, self.equipment_model, self.equipment_type]}

while True:
    try:
        choise = input(
            "\n1. Add printer\n2. Add scanner\n3. Add copier\n4. Check storage, branch and basket\n5. Move/delete an item\n\nPlease enter the number from menu or press enter to exit: ")
        if choise == "":
            break
        elif choise == "1":
            printer = Printers(input("Please enter the name: "), input("Please enter the model: "),
                               input("Please enter the type: "))
        elif choise == "2":
            scanner = Scanners(input("Please enter the name: "), input("Please enter the model: "),
                              input("Please enter the type: "))
        elif choise == "3":
            copier = Copiers(input("Please enter the name: "), input("Please enter the model: "),
                                 input("Please enter the type: "))
        elif choise == "4":
            d = (Storage.storage_total)
            print(f"\nStorage -- {d}")
            print(f"Branch -- {Storage.branch}")
            print(f"Basket -- {Storage.basket}")
        elif choise == "5":
            move = input(
                "1. Move item from storage to branch\n2. Move item from branch to storage\n3. Move item from storage to basket\n4. Clean the basket\n5. Return to previous menu\n6. Check storage, branch and basket\n\nPlease enter the number from menu or press enter to exit: ")
            if move == "":
                break
            elif move == "1":
                print(Storage.storage_to_branch())
                print(f"Branch -- {Storage.branch}")
                print(f"Storage -- {Storage.storage_total}")
                print(f"Basket -- {Storage.basket}")
                print()
            elif move == "2":
                print(Storage.branch_to_storage())
                print(f"Branch -- {Storage.branch}")
                print(f"Storage -- {Storage.storage_total}")
                print(f"Basket -- {Storage.basket}")
                print()
            elif move == "3":
                print(Storage.storage_to_basket())
                print(f"Branch -- {Storage.branch}")
                print(f"Storage -- {Storage.storage_total}")
                print(f"Basket -- {Storage.basket}")
                print()
            elif move == "4":
                (Storage.clean_basket())
                print(f"Branch -- {Storage.branch}")
                print(f"Storage -- {Storage.storage_total}")
                print(f"Basket -- {Storage.basket}")
                print()
            elif move == "5":
                continue
            elif move == "6":
                d = (Storage.storage_total)
                print(f"\nStorage -- {d}")
                print(f"Branch -- {Storage.branch}")
                print(f"Basket -- {Storage.basket}")
            else:
                print("You entered wrong value")
                continue
        else:
            print("You entered wrong value")
            continue
    except KeyError:
        print("You entered wrong value")
    except ValueError:
        print("You entered wrong value")

