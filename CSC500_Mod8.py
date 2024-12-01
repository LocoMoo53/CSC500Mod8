## Jason Thomas CSC500 Module 8
## Creates ItemToPurchase class 
class ItemToPurchase:
    def __init__(self, name="none", description="none", price=0, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    


## Creates ShoppingCart class and attributs as listed
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

## add_item() method
    def add_item(self, item):
        self.cart_items.append(item)

## remove_item() method
    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

## Modify_item() method
    def modify_item(self, item):
        found = False
        for cart_item in self.cart_items:
            if cart_item.name == item.name:
                if item.description != "none":
                    cart_item.description = item.description
                if item.price != 0:
                    cart_item.price = item.price
                if item.quantity != 0:
                    cart_item.quantity = item.quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")
## get_num_items_in_cart() method
    def get_num_items_in_cart(self):
        total_quantity = sum(item.quantity for item in self.cart_items)
        return total_quantity

## get_cost_of_cart() method
    def get_cost_of_cart(self):
        total_cost = sum(item.price * item.quantity for item in self.cart_items)
        return total_cost

## print_total() method
    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Number of Items:", self.get_num_items_in_cart())
        
        
        total_cost = self.get_cost_of_cart()
         
        if total_cost == 0:
            print("SHOPPING CART IS EMPTY")
        else:       
            
            print(f"Total: ${total_cost}")

## print_descriptions() method
            
    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        for item in self.cart_items:
            print(f"{item.name}: {item.description}")

## print_menu()
def print_menu(cart):
    menu = (
        "\nMENU\n"
        "a - Add item to cart\n"
        "r - Remove item from cart\n"
        "c - Change item quantity\n"
        "i - Output items' descriptions\n"
        "o - Output shopping cart\n"
        "q - Quit\n"
    )
    choice = ''
    while choice != 'q':
        print(menu)
        choice = input("Choose an option: ")
        if choice == 'a':
            name = input("Enter the item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)
        elif choice == 'r':
            name = input("Enter name of item: ")
            cart.remove_item(name)
        elif choice == 'c':
            name = input("Enter item name: ")
            description = input("Enter new description : ")
            price = float(input("Enter new price: "))
            quantity = int(input("Enter new quantity: "))
            item = ItemToPurchase(name, description, price, quantity)
            cart.modify_item(item)
        elif choice == 'i':
            cart.print_descriptions()
        elif choice == 'o':
            cart.print_total()
        elif choice != 'q':
            print("Invalid option. Please try again.")

## Implement output
def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")
    cart = ShoppingCart(customer_name, current_date)
    print(f"Customer name: {cart.customer_name}")
    print(f"Today's date: {cart.current_date}")
    print_menu(cart)

if __name__ == "__main__":
    main()
