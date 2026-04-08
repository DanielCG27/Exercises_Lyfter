my_list= ["Dog", "Cat", "Bunny", "Chicken", "Mouse"]
change= my_list[0]
my_list[0] = my_list[-1]
my_list[-1]= change
print(my_list)