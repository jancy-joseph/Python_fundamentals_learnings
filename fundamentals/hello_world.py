import string

# 1. TASK: print "Hello World"copy
print("Hello World")
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print("Hello {}!",name)	# with a comma
print( "Hello"+name)	# with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print("Hello {}!",name)	# with a comma
print( "Hello {}"+str(name))	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat %s and %s"%(fave_food1,fave_food1)) # %
print("I love to eat %s and %s".format(fave_food1,fave_food1)) # with .format()
print("I love to eat {0} and {1}".format(fave_food1,fave_food1)) # with .format()

print(f'I love to eat{fave_food1} and {fave_food2}') # with an f string

number ="0121222"
if number not in string.digits: 
    print("not digits")
else:
    print("is digit")
number =121222
if str(number) not in string.digits:
    print("not digits")
else:
    print("is digit")



def  check(value):
    for letter in value:
        if letter not in string.digits:
            return false
    return True

numberx ="121222"
result = check(numberx)
if(result):
    print("result is digit")
else:
    print("result is not digit")


if(result ==True):
    pass

