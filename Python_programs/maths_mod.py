class Maths:
    def add(*args):
        total = 0
        for arg in args:
            total += arg
        return total

def factorial(num):
    fact = 1
    for i in range(2,num+1):
        fact *= i
    return fact

var_college = "Silicon University"