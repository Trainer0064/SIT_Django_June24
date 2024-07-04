set1 = {10,2,3,"SIT",True,(4,5)}
print(set1,type(set1))

# set1.add(False)
# print(set1)
# set1.remove(2)
# print(set1)
# var=set1.pop()
# print(var,set1)

set1.remove("SIT")
set1.add("Silicon")
print(set1)
set1.discard("SIT")
print(set1)
set1.clear()
print(set1)