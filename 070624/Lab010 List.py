shoping_list = ["milk", "bread", "jam"]
print(shoping_list)
# Adding
# //add item in last
shoping_list.append("Buiskit")
print(shoping_list)
# add item in middle
shoping_list.insert(3 , "cake")
print(shoping_list)
# add multiple items to list
shoping_list.extend(['Salt , Chips'])
print(shoping_list)
# remove item from list
shoping_list.remove("jam")
print(shoping_list)
# remove last item in list
shoping_list.pop()
print(shoping_list)
# reverse the list
shoping_list.reverse()
print(shoping_list)
# sort the list
shoping_list.sort()
print(shoping_list)
# Mutable in nature(change the value)
print(shoping_list)
shoping_list[1]= "sachin"
print(shoping_list)