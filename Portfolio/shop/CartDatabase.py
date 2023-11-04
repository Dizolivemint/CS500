from tinydb import TinyDB

class CartDatabase:
  def __init__(self, db_file):
    self.db = TinyDB(db_file)

  def add_item(self, item):
    self.db.table('items').insert(item)
    
  def get_all_items(self):
    items = self.db.table('items').all()
    return items

  def get_items_by_name(self, item_name):
    items = self.db.table('items').search(self.Item.item_name == item_name)
    return items
  
  def create_cart(self, cart):
    self.db.table('carts').insert(cart)
    
  def get_cart(self, cart_id):
    cart = self.db.table('carts').get(doc_id=cart_id)
    return cart
  
  def empty_cart(self, cart_id):
    self.db.table('carts').truncate()
    self.db.table('items').truncate()
    
  def update_item(self, item_id, item):
    self.db.table('items').update(item, doc_ids=[item_id])
    
  def remove_item(self, item_id):
    self.db.table('items').remove(doc_ids=[item_id])