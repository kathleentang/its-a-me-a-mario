#Write a function that will take a given string124 and reverse the order of the words. 
#"Hello world" becomes "world Hello" and "May the Fourth be with you" becomes "you with be Fourth the May"


def reverse_it(string):
    rv = []
    for word in string.split():
      rv.append(word)
    rv.reverse()
    return ' '.join(rv)
