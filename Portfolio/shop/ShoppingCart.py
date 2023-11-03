class ShoppingCart:
  def __init__(self, cart_info={}):
    self.customer_name = cart_info.get('customer_name', 'none')
    self.current_date = cart_info.get('current_date', 'January 1, 2020')
    self.item_quantity = cart_info.get('item_quantity', 0)
    self.cart_items = []

  def add_item(self, item_info):
    self.cart_items.append(item_info)

  def remove_item(self, item_name):
    isFound = False
    for item in self.cart_items:
      if item.item_name == item_name:
        self.cart_items.remove(item)
        found = True
        break
    if not isFound:
      print("Item not found in cart. Nothing removed.")
  
  def clear(self):
    self.cart_items.clear()

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
    self.print_title()
    print("Number of Items:", self.get_num_items_in_cart())
    for item in self.cart_items:
        item.print_item_cost()
    total_cost = self.get_cost_of_cart()
    print("Total:", f"${total_cost}")

  def print_descriptions(self):
    self.print_title()
    print("Item Descriptions")
    for item in self.cart_items:
      print(f"{item.item_name}: {item.item_description}")
      
  def print_title(self):
    print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")