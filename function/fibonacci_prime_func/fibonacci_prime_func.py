def fibonacci_prime(n):

  '''
  Function to generate fibonacci prime number

  Parameters
  ----------
  n : int
     total fibonacci prime numbers will be generate

  Returns
  --------
  numbers : list
      The list of fibonacci prime numbers generated

  example
  --------

  if variable n was given 5 then this function will
  be generated 5 first number that included in fibonacci prime
  numbers

  n = 5
  numbers = [2, 3, 5, 13, 89]
  '''

  numbers = [] # output variable
  fibonacci = [1, 1] # first fibonacci numbers
  num = 0 # while index variable for define prime numbers

  # function to generate fibonacci prime numbers
  while len(numbers) < n:

    fibonacci.append(fibonacci[-1] + fibonacci[-2]) # line to generate fibonacci numbers

    # variable for define prime numbers
    i = 2
    prime = True

    # multi line to define prime numbers in fibonacci
    if fibonacci[num] > 1:
      while i <= fibonacci[num] / 2:
        if fibonacci[num] % i == 0:
          prime = False
          break
        i += 1
      if prime == True:
        numbers.append(fibonacci[num])

    num += 1

  return numbers # return numbers (list) as output of this function