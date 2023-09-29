def get_products(num_products=5, reverse=False):
  # products and prices from database are pulled into a tuples
  # the tuples is not mutable, so products and prices can't be altered
  product_properties = ('name', 'price')
  products=[
    ('milk', 3.57),
    ('coffee', 10.50),
    ('bread', 1.87),
    ('butter', 3.45),
    ('flour', 1.73),
    ('rice', 2.43),
    ('pasta', 2.50),
    ('eggs', 3.70),
    ('cheese', 2.90),
    ('onions', 0.49)
  ]
   
  print('Products: ')
  for i in range(0, len(product_properties)):  
    # sort the products by each property (name, then price)
    print(f'Sorted by {product_properties[i]}')
    for product, price in sorted(products[:num_products], reverse=reverse, key=lambda x: x[i]):
      print(f'{product}: ${price:.2f}')
    print()
  print()
  
get_products(5, True)
get_products(7, False)
get_products(2, True)