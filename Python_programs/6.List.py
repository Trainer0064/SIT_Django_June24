lst = [1,2,30.4,"SIT",[1,2,3],True]
print(lst[3])
print(lst[3][2])
lst[3]="College"
print(lst[3])
# print(type(lst))
# print(lst)

# # # print(lst[3])
# # lst[1] = 20
# # print(lst)

# lst.append("Pragyan")
# lst.insert(4,"Clg")
# # [1, 2, 30.4, 'SIT', 'Clg', [1, 2, 3], True, 'Pragyan']
# print(lst)
# lst.remove(30.4)
# print(lst)
# # lst.remove(30.4) # it throws an exception as the item doesn't exist
# # print(lst)

# lst.pop() #it pops out the last item
# print(lst)
# print(len(lst))
# lst.pop(4)
# print(lst)

lst1 = [1,0,4,2,4,7,5,0,4,19]
print(lst1)
# lst1.sort()
# print(lst1)
# lst1.sort(reverse=True)
# print(lst1)
# print(lst1.count(4)) #3
# lst1.clear()
print(lst1[::-1])
lst1=lst1[::2]
print(lst1)