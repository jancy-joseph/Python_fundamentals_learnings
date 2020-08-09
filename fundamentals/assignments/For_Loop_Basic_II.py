
#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
""" def biggie_size(mylist):
    if(len(mylist)>0):
        for i in range(len(mylist)):
            if(mylist[i]>0):
                mylist[i]="big"
        return mylist
    else:
        print("list is empty")
        return False
result = biggie_size([-1, 3, 5, -5])
print(result) """


#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
#Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
#Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
""" def count_positives(mylist):
    if(len(mylist)>0):
        count = 0
        for i in range(len(mylist)):
            if(mylist[i]>0):
                count+=1
        mylist[len(mylist)-1]=count
        return mylist
    else:
        print("list emty")
        return False

result = count_positives([-1,1,1,1])
print(result)
result1 = count_positives([1,6,-4,-2,-7,-2])
print(result1) """


#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7
""" def sum_total(mylist):
    if(len(mylist)>0):
        sum = 0  
        for i in range(len(mylist)):
            sum+=mylist[i]     
        return sum    
    else:
        print("list emty")
        return False

result =sum_total([1,2,3,4])
print(result)
result =sum_total([6,3,-2])
print(result) """

#Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5
""" def average(mylist):
    if(len(mylist)>0):
        sum= 0 
        for i in range(len(mylist)):
            sum+=mylist[i]     
        return (sum/len(mylist)) 
    else:
        print("list emty")
        return False

result =average([1,2,3,4])
print(result) """



#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0

""" def length(mylist):
    if(len(mylist)>0): 
        return len(mylist)
    else:
        return 0

result =length([37,2,1,-9]) 
print(result)
result =length([])
print(result) """


#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

""" def minimum(mylist):
    if(len(mylist)>0):
        min=mylist[0]
        for i in range(len(mylist)):
            if(mylist[i]<min):
                min=mylist[i]     
        return min
    else:
        return False

result =minimum([37,2,1,-9])
print(result) 
result =minimum([])
print(result)  """

#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False
""" def maximum(mylist):
    if(len(mylist)>0):
        max=mylist[0]
        for i in range(len(mylist)):
            if(mylist[i]>max):
                max=mylist[i]     
        return max
    else:
        return False

result =maximum([37,2,1,-9])
print(result) 
result =maximum([])
print(result)
"""
#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

""" def ultimate_analysis(mylist):
    if(len(mylist)>0):
        sumTotal=0
        minimum =mylist[0]
        maximum=mylist[0]
        for i in range(len(mylist)):
            if(mylist[i]>maximum):
                maximum=mylist[i]
            if(mylist[i]<minimum):
                minimum=mylist[i]
            sumTotal+=mylist[i]
        average = sumTotal/len(mylist)
        length= len(mylist)
        newobj ={}
        newobj["sumTotal"]=sumTotal
        newobj["average"]=average
        newobj["minimum"]=minimum
        newobj["maximum"]=maximum
        newobj["length"]=length
        return newobj
    else:
        return False

result =ultimate_analysis([37,2,1,-9])
print(result) 
result =ultimate_analysis([])
print(result) """

#Reverse List - Create a function that takes a list and return that list with values reversed. 
#Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(mylist):
    if(len(mylist)>0):
        low = 0
        high = len(mylist) -1
        mid = (low+high)/2
        while(low<round(mid)):
            temp = mylist[low]
            mylist[low] = mylist[high]
            mylist[high] = temp
            low+=1
            high-=1
        return mylist 
    else:
        print("nothing to do as array is empty")
        return false
result = reverse_list([37,2,1,-9])
print(result)