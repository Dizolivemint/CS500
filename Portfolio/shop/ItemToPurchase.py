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