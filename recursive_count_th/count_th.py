'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # find index with "th"
    idx = word.find("th")
    # if found
    if idx > -1: 
        #   set ths to 1
        ths = 1
        #   remove everything to "th" inclusive
        word = word[idx + 2:]
        #   pass the remaining word to itself and add returned value to ths
        ths += count_th(word)
        #   return ths
        return ths
    # return 0
    return 0