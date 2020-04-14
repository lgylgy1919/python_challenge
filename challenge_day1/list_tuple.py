days = "Mon, Tue, Wed, Thur, Fri"
print(days)
# Mon, Tue, Wed, Thur, Fri
days_list = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_list)
# ['Mon', 'Tue', 'Wed', 'Thur', 'Fri']
print(type(days_list))
# <class 'list'>
print("Mon" in days_list)
# True
print("Man" in days_list)
# False
print(days_list[3])
# Thur
print(len(days_list))
# 5
days_list.append("Sat")
print(days_list)
# ['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat']
days_list.reverse()
print(days_list)
# ['Sat', 'Fri', 'Thur', 'Wed', 'Tue', 'Mon']
months_tuple = ("Jan", "Feb", "Mar", "April", "May")

print(type(months_tuple))
# <class 'tuple'>
