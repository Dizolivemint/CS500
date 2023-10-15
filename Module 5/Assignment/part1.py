def get_number_of_years():
  number_of_years = 0
  while True:
    try:
      number_of_years = int(input('Enter the number of years: '))
    except ValueError:
      print('Enter a number')
      continue
    if number_of_years < 0:
      print('Enter a number greater than 0')
      continue
    return number_of_years

def get_rainfall_data(number_of_years):
  number_of_months = 12
  total_rainfall = 0
  for year in range(1, number_of_years + 1):
    for month in range(1, number_of_months + 1):
      inches_of_rainfall = 0
      while True:
        try:
          inches_of_rainfall = int(input(f'Enter inches of rainfall for month {month}: '))
        except ValueError:
          print('Enter a number')
          continue
        if inches_of_rainfall < 0:
          print('Enter a number greater than 0')
          continue
        break
      total_rainfall += inches_of_rainfall
  total_months = number_of_years * number_of_months
  average_rainfall = total_rainfall / total_months
  
  return {
    "Number of months": total_months,
    "Total inches of rainfall": total_rainfall,
    "Average rainfall per month": average_rainfall
  }
        
def main():
  number_of_years = get_number_of_years()
  result = get_rainfall_data(number_of_years)
  for key, value in result.items():
    print(f'{key}: {value}')
      
main()