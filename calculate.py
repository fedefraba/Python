def calculate(**kwargs):
    msg = kwargs['message']
    first = kwargs['first']
    second = kwargs['second']
    op = kwargs['op']

    if op == 'add':
        if kwargs['make_float'] == True:
            return 'The result is' + str(first + second) if msg == None else msg + str(first + second) 
        else:
            return 'The result is' + str(int(first + second)) if msg == None else msg + str(first + second)
    elif op == 'subtract':
        if kwargs['make_float'] == True:
            return 'The result is' + str(first - second) if msg == None else msg + str(first - second)
        else:
            return 'The result is' + str(int(first - second)) if msg == None else msg + str(first - second)
    elif op == 'multiply':
        if kwargs['make_float'] == True:
            return 'The result is' + str(first * second) if msg == None else msg + str(first * second)
        else:
            return 'The result is' + str(int(first * second)) if msg == None else msg + str(int(first * second))
    elif op == 'divide':
        if kwargs['make_float'] == True:
            return 'The result is' + str(first % second) if msg == None else msg + str(first % second)
        else:
            return 'The result is' + str(int(first % second)) if msg == None else msg + str(int(first % second))
    else:
        return "please select valid operation"

print(calculate(make_float= True, message='La suma da ', first= 3.25, second= 3, op='divide'))