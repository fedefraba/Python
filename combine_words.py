def combine_words(word,**kwargs):
    if 'prefix' and 'suffix' in kwargs:
        return kwargs['prefix'] + word + kwargs['suffix']
    elif 'prefix' in kwargs:
        return kwargs['prefix'] + word
    elif 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word    

print(combine_words("regard"))
