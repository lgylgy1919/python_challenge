days = "Mon, Tue, Wed, Thur, Fri"
print(days)

days_list = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_list)
print(type(days_list))

print("Mon" in days_list)
print("Man" in days_list)

print(days_list[3])
print(len(days_list))

days_list.append("Sat")
print(days_list)

days_list.reverse()
print(days_list)

months_tuple = ("Jan", "Feb", "Mar", "April", "May")

print(type(months_tuple))
