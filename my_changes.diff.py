#I was responsible for sell_product(), restock_product(),low_stock_report(),
#inventory_summary() and main() functions in this module.

#sell a product by product ID and quantity
def sell_product(products):
    #ask for product ID
    product_id = input("Enter ID:").strip()
    while product_id not in [p.get_product_id() for p in products]:
        print("Product not found.")
        product_id = input("Enter ID:").strip()
        
    #find the product object
    for p in products:
        if p.get_product_id() == product_id:
            product = p
            break
        
    #ask for quantity to sell
    quantity = input("Enter quantity:").strip()
    while not quantity.isdigit() or int(quantity) <=0 or int(quantity) > product.get_quantity():
        print("System prevents oversell, allows valid quantity sale.")
        quantity = input("Enter quantity:").strip()
    quantity = int(quantity)
    
    #Update inventory if sale is successful
    # get the current quantity
    current_quantity = product.get_quantity()

    # calculate the new quantity
    new_quantity = current_quantity - quantity

    # set the updated quantity
    product.set_quantity(new_quantity)
    if product.get_quantity() == 0:
        print("Quantity reduces to 0, sale successful.")
    else:
        print(f"Sale successful. Remaining quantity of {product.get_name()}: {product.get_quantity()}")
    
#restock a product by product ID and amount
def restock_product(products):
    #ask for product ID
    product_id = input("Enter ID: ").strip()
    while product_id not in [p.get_product_id() for p in products]:
        print("Product not found.")
        product_id = input("Enter ID: ").strip()
    
    #ask for restock amount
    amount = input("Enter restock amount: ").strip()
    while not amount.isdigit() or int(amount) <=0:
        print("Reject negative value; accept valid input.")
        amount = input("Enter restock amount: ").strip()
    amount = int(amount)
    
    # Find the product and restock it
    for p in products:
        if p.get_product_id() == product_id:
            # update quantity
            current_quantity = p.get_quantity()
            new_quantity = current_quantity + amount
            p.set_quantity(new_quantity)

            print(f"Product {p.get_name()} restocked successfully. New quantity: {p.get_quantity()}")
            return
        
#Scans all products and displays those with quantity less than or equal to their reorder level.
def low_stock_report(products):
    found = False  # flag to check if any product is low
    for p in products:
        quantity = p.get_quantity()
        reorder_level = p.get_reorder_level()

        # Check if the product needs restocking
        if quantity <= reorder_level:
            print(f"Product ID: {p.get_product_id()}, Name: {p.get_name()}, Quantity: {quantity}, Reorder Level: {reorder_level}")
            found = True

    if not found:
        print("No products below reorder level.")
        
#Displays summary statistics such as total number of products and total quantity of all products combined.
def inventory_summary(products):
    print("\nView Inventory Summary")
    
    #total number of products
    product_count = len(products)
    
    #total quantity of all products
    total_quantity = sum(p.get_quantity() for p in products)
    
    #print the summary
    print(f"Total number of products: {product_count}, Total quantity of all products: {total_quantity}")
    
#Prompts the user to select a category and then displays all products that belong to that category.
def list_products_by_category(products):
    #ask for category
    category = input("Enter category: ").strip()
    
    while not category.isdigit() or not (0 <= int(category) <= 9):
        print("<--INVALID (not in 0-9)")
        category = input("Enter category: ").strip()
    category = int(category)
    
    found = False
    for p in products:
        if p.get_category() == category:
            print(f"Product ID: {p.get_product_id()}, Name: {p.get_name()}, Quantity: {p.get_quantity()}, Price: {p.get_price():.2f}")
            found = True
    if not found:
        print(f"No products found in category '{category}'.")
        
#searches for a product by ID and returns its index in the list of products.
def product_index(products, product_id):
    for index in range(len(products)):#loop through the list
        if products[index].get_product_id() == product_id:  #check for a match
            return index                      #return the index if found
    return -1   #return -1 if not found

#displays all products in a formatted table
def print_products(products):
    list_products = []
    
    #print table header
    print(f"{'Product ID':<10}  {'Name':<20}  {'Category Index':<12}  {'Quantity':>8}  {'Price':>10}  {'Reorder Level':>14}")
    print("-" * 80)
    
    #print each product's details
    for p in products:
        d= (f"{p.get_product_id():<10}  {p.get_name():<20}  {p.get_category():<12}  {p.get_quantity():>8}  {p.get_price():>10.1f}  {p.get_reorder_level():>14}")
        list_products.append(d)
    
    for line in list_products:
        print(line)
    print("-" * 80)

#main function to run the inventory management system
def main():
    filename = "inventory.csv"
    products = load_products(filename)
    
    #print welcome message
    print("-" * 50)
    print("Welcome to the Product Inventory Management System")
    print("-" * 50)
    
    choice = 0
    while choice != 14:
        choice = print_menu()

        if choice == 1:
            products = load_products(filename)

        elif choice == 2:
            save_products(filename, products)

        elif choice == 3:
            print_products(products)

        elif choice == 4:
            term = input("Enter search term (ID, name, or category): ").strip()
            matches = search_product(products, term)
            if matches:
                for p in matches:
                    print(f"{p.get_product_id()}  {p.get_name()}")
            else:
                category_matches = [p for p in products if Product.category[p.get_category()].lower() == term.lower()]
                if category_matches:
                    for p in category_matches:
                        print(f"{p.get_product_id()}  {p.get_name()}")
                else:
                    print("No matching products.")

        elif choice == 5:
            add_product(products)

        elif choice == 6:
            remove_product(products)

        elif choice == 7:
            edit_product(products)

        elif choice == 8:
            sell_product(products)

        elif choice == 9:
            restock_product(products)

        elif choice == 10:
            low_stock_report(products)

        elif choice == 11:
            inventory_summary(products)

        elif choice == 12:
            list_products_by_category(products)

        elif choice == 13:
            product_id = input("Enter product ID to find index: ").strip()
            index = product_index(products, product_id)
            print("Index:", index)

        elif choice == 14:
            print("Exiting program...")

        else:
            print("Invalid choice. Please enter a number between 1 and 14.")

if __name__ == "__main__":
    main()