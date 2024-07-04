"""
Single Inheritance
"""

# class Parent:
#     wealth = 100000

# class Child(Parent):
#     age = 20

# child_obj = Child()

# print(child_obj.age)
# print(child_obj.wealth)

# child_obj.name = "Trisha"

# print(f"{child_obj.name} with age of {child_obj.age} have a wealth of {child_obj.wealth}")

# child_obj2 = Child()
# child_obj2.name = "Arpit"

# print(f"{child_obj2.name} with age of {child_obj2.age} have a wealth of {child_obj2.wealth}")

"""
Multiple Inheritance
"""

# class Father:
#     last_name = "Agrawal"

#     def greet_f(self):
#         print("Hello Father!")

# class Mother:
#     emotion = "Affection"

#     def greet_m(self):
#         print("Hello Mother!")

# class Child(Father,Mother):
#     name = "Aarav"

# obj = Child()

# print(f"{obj.name} {obj.last_name} has an emotions of his mother e.g {obj.emotion}")
# print(obj.wealth)


"""
Multilevel Inheritance
"""

# class GrandParent:
#     property_land = 10000000

# class Parent(GrandParent):
#     wealth = 1000000

# class Child(Parent):
#     money = 100000

# child_obj = Child()

# print(f"Total wealth of {type(child_obj)} is {child_obj.property_land+child_obj.wealth+child_obj.money}")

# parent_obj = Parent()

# print(f"Total wealth of {type(parent_obj)} is {parent_obj.property_land+parent_obj.wealth}")

# grand_obj = GrandParent()

# print(f"Total wealth of {type(grand_obj)} is {grand_obj.property_land+grand_obj.money}")

"""
Hierarchical Inheritance
"""

# class Parent:
#     wealth = 1000000

#     def intro(self):
#         print("My name ABC")

# class Child1(Parent):
#     def intro(self):
#         super().intro()
#         print("My parents wealth is",super().wealth)
#         print("I am a child 1")

# class Child2(Parent):

#     def intro(self):
#         print("I am a child 2")

# child1_obj = Child1()
# child2_obj = Child2()

# print(child1_obj.wealth)
# child1_obj.intro()
# print(child2_obj.wealth)
# child2_obj.intro()