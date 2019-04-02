array=[2,1,4,6,7,8,5,10,9]
a=len(array)
for j in range (1,a):
    key= array[j]
    i=j-1
    while i>=0 and array[i]>key:
        array[i+1]=array[i]
        i=i-1
    array[i+1]=key
    
print(array)
