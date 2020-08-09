
###composite datatype

##tuple--immutable
dog = ('Bruce', 'cocker spaniel', 19, False)#notice it is not square bracket
print(dog[0])		# output: Bruce
#dog[1] = 'dachshund'

# lists
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']#notice square bracket
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists
new_person['hobbies'] = ['climbing', 'coding']	# adds a key-value pair if the key doesn't exist
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}       


###common funcitons

print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11


#Type Casting or Explicit Type Conversion

#print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
#total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61
print(total)

