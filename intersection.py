def intersection(alist,blist):
    Inter = []
    for i in alist:
        if i in alist and i in blist:
            Inter.append(i)
    return Inter

print (intersection([1,2,3,4,5,6],[1,5]))