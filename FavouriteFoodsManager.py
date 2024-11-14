favourite_food=[]

while True:
    print("Favourite Foods Manager")
    print("0. Exit")
    print("1. Add food")
    print("2. Remove food")
    print("3. View your favourite foods")

    choose=input("Choose an option: ")

    if choose=='0':
        print("Thanks for using our favourite foods manager project.")
        break;

    elif choose=='1':
        food=input("Enter your favourite food name: ")
        favourite_food.append(food)
        print("Your favorite food added successfully.")

    elif choose=='2':
        rfood=input("Enter the name of food you want to remove: ")
        if rfood in favourite_food:
            favourite_food.remove(rfood)
            print("The name of food you entered removed successfully.")
        else:
            print("The name of food you entered is not in the list.")


    elif choose=='3':
        if favourite_food:
            print("Your favourite foods list:")
            for index,food in enumerate(favourite_food,start=1):
                print(f"{index}:{food}")
        else:
            print("Food list is empty or didn't create yet.")

    else:
        print("Invalid option.")

