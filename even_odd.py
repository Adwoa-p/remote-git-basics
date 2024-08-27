'''even numbers with for loop'''
# def is_even(numbers:list[int]):
#     even=[]
#     for num in numbers:
#         if num%2== 0:
#             even.append(num)
#     return even
# values=is_even([1,56,234,87,4,76,24,69,90,135])
# print(values)


''' even numbers with map'''
# def get_even(x:int):
#     if x%2==0: return x
# def even_map(numbers:list[int]):
#     return map(get_even,numbers)
# map_values=even_map([1,56,234,87,4,76,24,69,90,135])
# print(list(map_values))


'''even numbers with lambda and filter'''
# numbers = [1,56,234,87,4,76,24,69,90,135]
# even=filter((lambda x:(x%2==0)),numbers)
# print(list(even))

'''even numbers with filter'''
# def even(x):
#     if x%2==0:
#        return x
# def even_numbers_with_filter(numbers:list[int]):
#     return(list(filter(even,numbers)))
# numbers = [1,56,234,87,4,76,24,69,90,135]
# print(even_numbers_with_filter(numbers))


'''even numbers with map and filter'''
# def even(x):
#     if x%2==0:
#        return x
# def even_numbers_with_map_filter(numbers:list[int]):
#     return(list(map(even,numbers)))
# def none(x):
#     if x == "None":
#         return(filter(none,numbers))
# numbers = [1,56,234,87,4,76,24,69,90,135]
# print(even_numbers_with_map_filter(numbers))


'''odd numbers with lambda and filter'''
# numbers = [1,56,234,87,4,76,24,69,90,135]
# odd=filter((lambda x:(x%2==1)),numbers)
# print(list(odd))


'''odd numbers with for loop'''
def is_odd(numbers:list[int]):
    odd=[]
    for num in numbers:
        if num%2== 1:
            odd.append(num)
    return odd
# values=is_odd([1,56,234,87,4,76,24,69,90,135])
# print(values)


'''odd numbers with filter'''
# def odd(x):
#     if x%2!=0:
#        return x
# def odd_numbers_with_filter(numbers:list[int]):
#     return(list(filter(odd,numbers)))
# numbers = [1,56,234,87,4,76,24,69,90,135]
# print(odd_numbers_with_filter(numbers))


'''odd numbers with not and lambda'''
# numbers = [1,56,234,87,4,76,24,69,90,135]
# odd=filter((lambda x:not (x%2==0)),numbers)
# print(list(odd))
