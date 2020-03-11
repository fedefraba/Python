def is_all_strings(*args):
    return all(char for char in [args] if char is str)

print(is_all_strings('agent',0,'banks'))