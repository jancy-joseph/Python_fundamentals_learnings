# python code below!
arr = [1,3,5,7]
arr[0], arr[1] = arr[1], arr[0]
print(arr)
#simple swap
low =0;
high= len(arr)-1
while(low<high):
    arr[low],arr[high]=arr[high],arr[low]
    low+=1
    high-=1
print(arr)