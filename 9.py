def load_shopping_list(file_name):
    shopping_list = {}
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                product, quantity = line.strip().split(', ')
                shopping_list[product] = int(quantity)
    except FileNotFoundError:
        print(f"The file {file_name} does not exist. Starting with an empty shopping list.")
    return shopping_list

def save_shopping_list(file_name, shopping_list):
    with open(file_name, 'w', encoding='utf-8') as file:
        for product, quantity in shopping_list.items():
            file.write(f"{product}, {quantity}\n")

def add_product(shopping_list):
    product = input("Enter the product name: ")
    quantity = int(input("Enter the quantity: "))
    if product in shopping_list:
        shopping_list[product] += quantity
    else:
        shopping_list[product] = quantity
    print(f"Added {quantity} of {product} to the shopping list.")

def view_shopping_list(shopping_list):
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        for product, quantity in shopping_list.items():
            print(f"{product}: {quantity}")

def edit_product(shopping_list):
    product = input("Enter the product name to edit: ")
    if product in shopping_list:
        quantity = int(input("Enter the new quantity: "))
        shopping_list[product] = quantity
        print(f"Updated {product} to {quantity}.")
    else:
        print(f"{product} not found in the shopping list.")

def delete_product(shopping_list):
    product = input("Enter the product name to delete: ")
    if product in shopping_list:
        del shopping_list[product]
        print(f"Deleted {product} from the shopping list.")
    else:
        print(f"{product} not found in the shopping list.")

def main():
    file_name = 'shopping_list.txt'
    shopping_list = load_shopping_list(file_name)

    while True:
        print("\nShopping List Menu")
        print("1. Add product")
        print("2. View shopping list")
        print("3. Edit product")
        print("4. Delete product")
        print("5. Save and exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product(shopping_list)
        elif choice == '2':
            view_shopping_list(shopping_list)
        elif choice == '3':
            edit_product(shopping_list)
        elif choice == '4':
            delete_product(shopping_list)
        elif choice == '5':
            save_shopping_list(file_name, shopping_list)
            print("Shopping list saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
