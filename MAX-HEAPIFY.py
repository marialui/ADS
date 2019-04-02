def max_heapify (heap,i):
    l= (2*i)+1
    r= (2*i) +2
    if l<= len(heap)-1 and heap[l] > heap[i]:
            largest= l
            #print(largest)
    else:
        largest= i
        #print(largest)
    if r<= len(heap)-1 and heap[r] > heap[largest]:
        largest= r
    if largest != i:
        massimo=heap[largest]
        heap[largest]=heap[i]
        heap[i]= massimo

        max_heapify(heap,largest)


array=[16,4,10,14,7,9,3,2,8,1]
print(array)

max_heapify(array,1)
print(array)


