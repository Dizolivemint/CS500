class ItemToPurchase:
    def __init__(self, item):
      self.item_name = item.get('item_name', 'none')
      self.item_price = item.get('item_price', 0.0)
      self.item_quantity = item.get('item_quantity', 0)
      self.item_description = item.get('item_description', 'none')
      
    def print_item_cost(self):
      item_total_cost = self.item_quantity * self.item_price
      print(item_total_cost)
      return item_total_cost

class ShoppingCart:
  def __init__(self, cart_info={}):
    self.customer_name = cart_info.get('customer_name', 'none')
    self.current_date = cart_info.get('current_date', 'January 1, 2020')
    self.item_quantity = cart_info.get('item_quantity', 0)
    self.cart_items = []

  def add_item(self, item_info):
    self.cart_items.append(ItemToPurchase(item_info))

  def remove_item(self, item_name):
    isFound = False
    for item in self.cart_items:
      if item.item_name == item_name:
        self.cart_items.remove(item)
        found = True
        break
    if not isFound:
      print("Item not found in cart. Nothing removed.")

  def modify_item(self, modified_item):
    isFound = False
    for item in self.cart_items:
      if item.item_name == modified_item['item_name']:
        if modified_item.get('item_price') is not None:
          item.item_price = modified_item['item_price']
        if modified_item.get('item_quantity') is not None:
          item.item_quantity = modified_item['item_quantity']
        if modified_item.get('item_description') is not None:
          item.item_description = modified_item['item_description']
        isFound = True
        break
    if not isFound:
      print("Item not found in cart. Nothing modified.")

  def get_num_items_in_cart(self):
    return sum(item.item_quantity for item in self.cart_items)

  def get_cost_of_cart(self):
    return sum(item.item_quantity * item.item_price for item in self.cart_items)

  def print_total(self):
    print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
    print("Number of Items:", self.get_num_items_in_cart())
    for item in self.cart_items:
        item.print_item_cost()
    total_cost = self.get_cost_of_cart()
    print("Total:", f"${total_cost}")

  def print_descriptions(self):
    print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
    print("Item Descriptions")
    for item in self.cart_items:
      print(f"{item.item_name}: {item.item_description}")
                  
def main():
  print()

  cart = ShoppingCart()

  while True:
    print_menu()
    choice = input("Choose an option: ").strip().lower()

    if choice == 'a':
      item_info = {
        'item_name': input("Enter the item name: "),
        'item_description': input("Enter the item description: ") or None,
        'item_price': float(input("Enter the item price: ")),
        'item_quantity': int(input("Enter the item quantity: "))
      }
      cart.add_item(item_info)
    elif choice == 'r':
      item_name = input("Enter the name of the item to remove: ")
      cart.remove_item(item_name)
    elif choice == 'c':
      item_info = {
        'item_name': input("Enter the name of the item to modify: "),
        'item_price': float(input("Enter the new price (press Enter to keep the same): ") or None),
        'item_quantity': int(input("Enter the new quantity (press Enter to keep the same): ") or None),
        'item_description': input("Enter the new description (press Enter to keep the same): ") or None,
      }
      cart.modify_item(item_info)
    elif choice == 'i':
      cart.print_descriptions()
    elif choice == 'o':
      cart.print_total()
    elif choice == 'q':
      break
    else:
      print("Invalid option. Please choose a valid option.")

def print_menu():
  print(
    "MENU\n"
    "a - Add item to cart\n"
    "r - Remove item from cart\n"
    "c - Change item quantity\n"
    "i - Output items' descriptions\n"
    "o - Output shopping cart\n"
    "q - Quit"
  )

if __name__ == "__main__":
  main()
