import random
def randInt(min=0  , max=100):
    if(min==None or max ==None):
        num = round(random.random()*max)
    elif (min == None):
        num = round(random.random()*max)
    elif (max == None):
    #  num= random.randrange(min,100)
        num= round(random.random()*(100-min)+min)
    else:
    #num=random.randrange(min,max)
        num= round(random.random()*(max-min)+min)
    return num
print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
#print(randInt(max=-1))
#print(randInt(min=70,max=50))