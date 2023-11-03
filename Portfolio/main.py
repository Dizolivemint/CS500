import os
from datetime import date
from shop.ShoppingCart import ShoppingCart
from shop.ItemToPurchase import ItemToPurchase
from shop.CartDatabase import CartDatabase

def main():
  print()

  cart_persistant = CartDatabase(os.path.join('db', 'cart.json'))
  
  customer_name = None
  try:
    customer_name = cart_persistant.get_cart(1)['customer_name']
  except TypeError:
    customer_name = None
  
  while not customer_name:
    customer_name = input("Enter customer's name: ")
    if customer_name:
      break
    else:
      print("Customer's name cannot be blank.")
    
  today = date.today().strftime("%B %d, %Y")
  cart_data = {
    'customer_name': customer_name,
    'current_date': today
  }
  cart = ShoppingCart(cart_data)
  cart_persistant.create_cart(cart_data)
  
  for item in cart_persistant.get_all_items():
    cart.add_item(ItemToPurchase(item))
    
  cart.print_title()
  
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
      cart.add_item(ItemToPurchase(item_info))
      cart_persistant.add_item(item_info)
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
      print('\n')
      cart.print_descriptions()
    elif choice == 'o':
      print('\n')
      cart.print_total()
    elif choice == 'e':
      cart.clear()
      cart_persistant.empty_cart(1)
    elif choice == 'q':
      cart_persistant.db.close()
      break
    else:
      print("Invalid option. Please choose a valid option.")

def print_menu():
  print(
    "\nMENU\n"
    "a - Add item to cart\n"
    "r - Remove item from cart\n"
    "c - Change item quantity\n"
    "i - Output items' descriptions\n"
    "o - Output shopping cart\n"
    "e - Empty the cart\n"
    "q - Quit"
  )

if __name__ == "__main__":
  main()