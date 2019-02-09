#initialize list

my_list = [1,2,3,4 , ":)", True, 4.5]

#add item 
my_list.append(88)

#access item
print my_list[4]

# Change item
my_list[0] = 'pooBearGang'
print my_list

# remove item by index
del my_list[0]

# iterate
for item in my_list:
	print item