# Using recursion to implement power and factorial functions


def power(num, pwr):
    x=0
    if x == pwr:
        print ("done")
    else:
        e = num * num
        ee = num *e
        x += 1
    return ee


def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
        
        
    


print("{} to the power of {} is {}".format(5, 3, power(5, 3)))
print("{} to the power of {} is {}".format(1, 5, power(1, 5)))
print("{}! is {}".format(4, factorial(4)))
print("{}! is {}".format(0, factorial(0)))