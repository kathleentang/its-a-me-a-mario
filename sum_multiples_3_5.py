###If we list all the natural numbers below 10 that are multiples of 3 or 5, 
### we get 3, 5, 6 and 9. The sum of these multiples is 23.
## Define a function that finds the sum of all the multiples of 3 or 5 below any number.

def sum_35(number):
    result = 0
    for i in range(3,number):
      if i % 3 == 0:
         result = result + i
      elif i % 5 == 0:
        result = result + i
      else:
        pass
    return result