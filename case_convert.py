#Define a function that takes an string and converts all lowercase letters to uppercase letters and vice versa.


def case_convert(string):
    new_string = ''
    for x in string:
      if x == x.lower():
         new_string+=x.upper()
      else:
        new_string+=x.lower()
    return new_string