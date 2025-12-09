from array import array
# integer array
arr = array('i' , [1,2,3,4])
# here in the | the 'i' means integer , we can use 'f' for float.....

# access
print(arr[0])

# update
arr[2] = 30

# add element
arr.append(5)    #at end
arr.extend([6,7,8])  #many at once
arr.insert(1,99)

#length
print(len(arr))
