def contains_purple(*args):
    if "Purple".lower() in args:
        return True
    return False

print(contains_purple(1,2,3,4,False,"purple"))

