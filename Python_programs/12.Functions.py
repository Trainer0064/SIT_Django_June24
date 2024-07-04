# def greet():
#     print("Welcome to the Training Program")
#     print("SIlicon University")
#     print("Django with Python")

# greet()

# """
# No Arguments No Return Value
# """

# def NANR():
#     print("No Arguments No Return Value")

# NANR()

# """
# No Arguments With Return Value
# """

# def NARV():
#     message  = "No Arguments With Return Value"
#     return message

# print(NARV())

# """
# With Arguments No Return Value
# """

# def WANR(msg):
#     print(msg)

# WANR("With Arguments No Return Value")

# """
# With Arguments With Return Value
# """

# def add(a,b):
#     result = a + b
#     return result

# print(add(10,20))

# WANR("Value")

# # lst = [10,20,30,40,50]
# # total = 0
# # for var in lst:
# #     total += var
# # print(total)

"""
Requirements for function: Multiple Arguments and get the sum
"""

# def Addition(*args):
#     total = 0
#     for var in args:
#         total += var
#     return total

# var_sum=Addition(1,2,3)
# print(var_sum)

# def PrintItems(**kwargs):
#     for item in kwargs:
#         print(f"{item} : {kwargs[item]}")

# PrintItems(name = "Arpit",age = 22, place = "BBSR",branch = "CS")


def factorial_iterative(num):
    fact = 1
    for i in range(2,num+1):
        fact*=i
    return fact


def factorial_recursive(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial_recursive(num-1)

# print("Imported Module name is ",__name__)
if __name__ == "__main__":
    print("Func",factorial_iterative(5))
    print(factorial_recursive(5))