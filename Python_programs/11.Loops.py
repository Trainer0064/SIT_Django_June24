lst = [20,34,43,76,24,78]
# print(lst)
# while num<=10 :
#     print(num)
#     num+=1
# index = 0
# while index <len(lst):
#     print(lst[index])
#     index+=1

"""
*
**
***
****
"""

# num = 1

# while num<=4:
#     print("*"*num)
#     num+=1

# row,col = 1,1

# while row<=4:
#     while col<=row:
#         print("*",end="")
#         col+=1
#     print()
#     row+=1
#     col=1

"""
For Loops
"""

# for item in lst:
#     print(item)

# if 201 in lst:
#     print("PRESENT")
# else :
#     print("NOT PRESENT")

# for index in range(len(lst)):
#     print(lst[index])

# print(list(range(8)))

d = {
    "name":"Pragyan",
    "age":20,
    "city":"Bangalore"
}

# for pair in d.items():
    # print(f"{pair[0]} : {pair[1]}")

# for key,value in d.items():
#     print(f"{key} : {value}")

for var in range(10):
    if var%2==0:
        continue
    print(var)