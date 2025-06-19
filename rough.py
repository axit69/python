lst = [1,2,3,1,1]
my_str = "this is monday"
my_int = 155


# print(lst.count(1))

# print(my_str.translate(""))

from oops_proj import chatbook
user1 = chatbook()
print(user1.id)

user2 = chatbook()
chatbook.get_id(99, 10)
print(user2._chatbook__user_id)

# user2 = chatbook()
# print(user1._chatbook__name)     # to access hidden attribute , name is hidden in using "__" in oops_proj.py. object name . followed by _classname and then __attribute

# user1.get_name("Axit")
# print(user1._chatbook__name)

# print(user1.id)
# print(user2.id)





# test code

# class car:
#     def __init__(self, type, company):
#         self.type = type
#         self.company = company
    
#     def driving(self, roads):
#         print(f"this car is for {roads}")

# car1 = car("sedan", "toyota")
# print("car1.company")

# car1.driving("offroading")

        