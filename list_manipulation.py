def list_manipulation(alist,command,location,value=None):
    if (command == "remove" and location == "end"):
        alist.pop()
        return alist
    elif (command == "remove" and location == "beginning"):
        return alist.pop(0)
    elif (command == "add" and location == "beginning"):
        alist.insert(0,value)
        return alist
    elif (command == "add" and location == "end"):
        alist.append(value)
        return alist

print(list_manipulation([123456],"remove","beginning",0))