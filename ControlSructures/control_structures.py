
#if/else/elif
age = 21

if age >= 18:
	print 'Adult!'
elif age >= 12:
	print 'is a teenager!'
elif age >= 3:
	print 'child'
else:
	print 'baby'	


#ternary
old_enough = True if age >= 21 else False
print(old_enough)

# While loops

while age < 50:
	print('Not old enough! Current age is: %s') % age
	age += 1