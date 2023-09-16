def main():
  # input two numbers
  num1 = input('Input the first number: ')
  num2 = input('Input the second number: ')

  # convert the strings into regular numbers
  try:
    num1 = int(num1)
    num2 = int(num2)
  except ValueError():
    print('You must enter a number.')
    main()
    exit()

  # multiply the numbers
  multiply_total = num1 * num2

  # divide the numbers
  divide_total = num1 / num2

  # output the results
  print(num1, '*', num2, '=', multiply_total)
  print(num1, '/', num2, '=', divide_total)
  
main()