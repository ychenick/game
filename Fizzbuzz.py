print("hello world")
myarray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for x in myarray:
    #print(x)
    if x % 15 == 0:
        print("Fizzbuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("buzz")
    else:
        print(x)