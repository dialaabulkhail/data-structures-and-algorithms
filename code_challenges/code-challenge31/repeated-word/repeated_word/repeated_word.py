# from ast import excepthandler


def repeated_word(string):
    lst = []
    try:
        for word in string.split():
            if word not in lst: 
                lst.append(word)
            else:
                return word
    except:
        raise Exception("Error")




