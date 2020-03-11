l=[-1,2,3,4,-5,99,-100]
def remove_negatives(nums):
    return list(filter(lambda l: l >=0,nums))

print(remove_negatives(l))