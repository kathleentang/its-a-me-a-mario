def reverse_it(string):
    rv = []
    for word in string.split():
      rv.append(word)
    rv.reverse()
    return ' '.join(rv)
