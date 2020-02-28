
def partition(alist,callback):
    Truthy = []
    Falsy = []
    Result = [Truthy,Falsy]
    for i in alist:
        if callback(i):
            Truthy.append(i)
        else:
            Falsy.append(i)
    return Result

print(partition([0,1,2,True,False],))