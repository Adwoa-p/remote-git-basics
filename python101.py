def welcome():
    print("Welcome to Advanced Python.")

welcome()

#map is used to apply a fuction to a data structureelement by element
names = ['sam','jerry','kofi']
print(list(map(len,names)))

#filter removes items rom a list, takes a function and a data structure
def too_old(x):
    return x>30
ages=[23,34,56,24,12,28]
filtered=list(filter(too_old, ages))
print(filtered)

#lambda, has no name.returns only none results
items=[1,2,3,4,5]
squares=map((lambda x: x**2),items)
print(list(squares))