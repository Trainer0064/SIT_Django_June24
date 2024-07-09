# class College:
#     college_name = "SIT"
#     address = "Patia, BBSR"

# obj = College()
# print(obj)
# print(obj.college_name)
# print(obj.address)

# obj2 = College()
# obj2.college_name = "KIIT"

# print(obj2)
# print(obj2.college_name)
# print(obj2.address)

# print(obj.college_name)
# print(College.college_name)

class College:
    city = "BBSR"
    def __init__(self,college_name,address):
        self.college_name = college_name
        self.address = address

    def display_info(self):
        print(f"College Name: {self.college_name}")
        print(f"Address: {self.address}")
        print(f"City: {College.city}")
    
    def __str__(self):
        return f"object is created for {self.college_name}"

obj = College("Silicon University","Bhubaneswar")

print(obj,type(obj))
# print(obj.college_name)
# print(obj.address)
# print(College.city)

# obj.display_info()

obj2 = College("KIIT","Kolkata")
print(obj2)
# obj2.display_info()