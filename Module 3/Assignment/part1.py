def input_charges():
  # Define charges
  charges = []
  
  # Start loop
  while True:
    # Input charge for food
    charge = input('Enter charge for food: ')
    
    # If input is empty, prompt user to close the bill
    if charge == '':
      is_stop = input('Stop? (y/n): ')
      is_stop = is_stop.lower()
      if is_stop == 'y':
        return charges
    
    # Convert charge for food to integer
    try:
      charge = int(charge)
    except ValueError:
      print('Invalid charge entered')
      continue
    
    # Validate input
    if charge < 0:
      print('Invalid charge entered')
      continue
    
    # Push charge for food into memory
    charges.append(charge)
    
def get_total(charges):
  # Define total
  total = 0
  
  # Define tip to equal .18
  tip = .18
  
  # Define tax to equal .07
  tax = .07
  
  # Iterate through charges and add each charge to total
  total = sum(charges)

  # Multiply total by tip and by tax
  total = total * (1 + tip + tax)
  
  return total

def main():
  charges = input_charges()
  total = get_total(charges)
  print(total)
  
main()