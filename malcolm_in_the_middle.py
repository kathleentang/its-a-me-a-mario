#You are going to be given a word. Your job is to return the middle character of the word. If the word's #length is odd, return the middle character. If the word's length is even, return the middle 2 characters.
#("test") should return "es"  
#("testing") should return "t"  
#("middle") should return "dd"  
#("A") should return "A"

def malcolm_in_the_middle(word):
    if len(word) == 1:
        return word
    elif len(word) % 2 == 0:
       return word[((len(word)/2)-1):((len(word)/2)+1)]
    else:
      return word[((len(word)/2))