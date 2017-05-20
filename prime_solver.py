#Define a function that takes a number and tells you if the number is prime or not

def prime(x):
  numbers = [i for i in range(2,(x/2)+1)]
  answer = [float(x) % float(i) for i in numbers]
  if 0 in answer:
    return "This is not Prime"
  else:
    return "This is a Prime"