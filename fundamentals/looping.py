for x in range(10,1,-1):#<1 not 1 will print 10,9,8,7,6,5,4,3,2 and not 1
    print(x)
for x in range(10):
    print(x)# default incerement +1 from 0 till 9 0,1,2,3,4,5,6,7,8,9 but not 10



# for loop through lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v) 
# output: abc, 123, xyz


#For Loops through Dictionaries
test ={"name":"jancy","age":37}
for key in test:
    print(key,test[key])

capitals={"washington":"seattle","illinois":"chicago"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
#to iterate through the values
for val in capitals.values():
     print(val)
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)


#While Loops

count = 0
while count < 5:
    print("looping - ", count)
    count += 1



y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

