tup = (1,2,1,11.21,"SIT",[10,20,30],(40,50,60),False)

print(tup)
# print(type(tup))
# print(len(tup))

# print(tup[3])

# tup[2] = 10 #Can not change and will throw exception

# print(tup.count(1))
# print(tup.index(3))

tup1 = tuple([10])
tup2 = (10,)
print(tup1,type(tup1))
# lst = list(tup)
# lst[1]= 23
# tup = tuple(lst)
# print(tup)

tup3 = tuple()
print(tup3,type(tup3))

tup = (1,2)
var1,var2  = tup
print(tup,var1,var2)