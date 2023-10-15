def get_number_of_books():
  number_of_books = 0
  while True:
    try:
      number_of_books = int(input('Enter the number of books: '))
    except ValueError:
      print('Enter a number')
      continue
    if number_of_books < 0:
      print('Enter a number greater than 0')
      continue
    return number_of_books

def get_points(number_of_books, points_schema):
  points = 0
  for key, value in points_schema.items():
    if number_of_books >= key:
      points = value
  return points

def main():
  points_schema = {
    1: 0,
    2: 5,
    4: 15,
    6: 30,
    8: 60
  }
  
  number_of_books = get_number_of_books()
  points = get_points(number_of_books, points_schema)
  print(f'You earned {points} points')
  
main()