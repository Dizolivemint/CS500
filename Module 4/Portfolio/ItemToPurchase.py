class ItemToPurchase:
  def __init__(self, item):
    self.item_name = item.get('item_name', 'none')
    self.item_price = item.get('item_price', 0.0)
    self.item_quantity = item.get('item_quantity', 0)
    
  def print_item_cost(self):
    item_total_cost = self.item_quantity * self.item_price
    print(item_total_cost)
    return item_total_cost

# Prompt user for items  
items = []
while True:
  item_name = input('Enter item name: ')
  if item_name == '':
    is_stop = input('Stop? (y/n): ')
    is_stop = is_stop.lower()
    if is_stop == 'y':
      break
    else:
      continue
  while True:
    try:  
      item_price = float(input('Enter item price: '))
      item_quantity = int(input('Enter item quantity: '))
    except ValueError:
      print('Enter a number')
      continue
    break
  
  items.append(ItemToPurchase({
    'item_name': item_name,
    'item_price': item_price,
    'item_quantity': item_quantity
  }))

# Print receipt
total_cost = 0.0
print("TOTAL COST")
for item in items:
  cost = item.item_price * item.item_quantity
  total_cost += cost
  print(f"{item.item_name} {item.item_quantity} @ {item.item_price} = {cost}")
  
print(f"Total: {total_cost}")