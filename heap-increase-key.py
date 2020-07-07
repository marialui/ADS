def increase_key(heap, i,key):
    if key< heap[i-1]:
        print('error:new key is smaller than current key')
    i=i-1
    heap[i]=key

    while i>0 and heap[((i-1)//2)]< heap[i]:

        parent=heap[(i-1)//2]
        heap[(i-1 )// 2]=heap[i]
        heap[i]=parent
        i=((i-1)//2)



happy=[16,14,10,8,7,9,3,2,4,1]
print(increase_key(happy,8,15))
print(happy)