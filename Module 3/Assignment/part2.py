def input_time():
  # Define time
  time = -1
  
  # While time is not valid
  while True:
    # Input time in hours
    time = input('Enter time in hours: ')
    
    # Convert time to integer
    try:
      time = int(time)
      # Validate time is greater than or equal to 0 and less than or equal 23
      if time < 0 or time > 23:
        raise ValueError
    except ValueError:
      print('Invalid time entered')
      continue
    
    return time

def output_clock_time(time):
  # Define number of hours
  number_of_hours = 0

  # While number of hours is not valid
  while True:
    # Input number of hours
    number_of_hours = input('Enter number of hours: ')
    
    try:
      # Convert number of hours to integer
      number_of_hours = int(number_of_hours)
      # Validate number of hours is greater than 0
      if number_of_hours < 0:
        raise ValueError
    except ValueError:
      print('Invalid number of hours entered')
      continue
    
  
    # Define total hours to equal time plus number of hours
    total_hours = time + number_of_hours
    
    # Divide by 24 and get remainder
    hours = total_hours % 24
    
    return hours
    
def main():
  time = input_time()
  hours = output_clock_time(time)
  print(hours)
  
main()
