
# Intitialize
my_dict = {}

# Add item
my_dict['name'] = 'brian'
my_dict['state'] = 'Ca'
my_dict['age'] = 31

# Access item
print my_dict['name']

# Change item
my_dict['state'] = 'Nunya'

# Remove item
del my_dict['age']
print my_dict

# Iterate
for k, v in my_dict.iteritems():
	print k, v
