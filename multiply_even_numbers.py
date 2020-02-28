def multiply_even_numbers(alist):
   result = 1 
   for num in alist:
       if num % 2 == 0:
            result = result * num
    return result

    
print(multiply_even_numbers([1,2,3,4,5,6,7,8]))