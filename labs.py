'''using the fold function'''
from functools import reduce
# total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
# print(total)


''' a function to join a group of words '''
# def join_strings(words: list[str]):
#     join = reduce(lambda x,y: x + y, words)
#     return join
# word=["hello ","hiii ","byee"]
# final=join_strings(word)
# print(final)


'''list comprehensions'''
# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()

# print([len(word) for word in words])

# print([len(word) for word in words if word != "the"])

#


'''checking for positive numbers'''
# def positive(number):
#         if number>0:
#             return number
numbers= [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# print([positive(number) for number in numbers])
print([x for x in numbers if (lambda x: x>0)(x)])
print([x for x in numbers if  x>0])

'''Uppercase'''
# def upper_case(word):
#     return word.upper(),len(word.upper())
# words = ["hello", "my", "name", "is", "Sam"]
# print([upper_case(word) for word in words])

'''even numbers'''
# def even(x):
#     if x%2==0:
#         return x
# numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
# print([ even(number) for number in numbers])

