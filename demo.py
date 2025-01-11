#this is just a git tutorial for myself

print('helloWorld')

#Exercise 1: simple function in Python
print('Exercise 1:')
def checkOdd(num1):
    if(num1 % 2 == 0):
        return True
    
if(checkOdd(3)):
    print('This is not an odd number.')
else:
    print('This is an odd number')
    
#added a function just to test git

# Python program to square and cube every number in a given list of integers using Lambda.
# Original list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

given_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squareFunc = lambda a: a*a
cubeFunc = lambda a: a*a*a

mapFunc1 = lambda jinish: list(map(squareFunc, jinish))
mapFunc2 = lambda jinish: list(map(cubeFunc, jinish))


print(mapFunc1(given_List))
print(mapFunc2(given_List))