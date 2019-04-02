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
        max_heapify(heap, largest)

def build_max_heap(array):
    for i in range ((len(array)//2)-1,-1,-1):
        max_heapify(array,i)

lista=[4,1,3,2,16,9,10,14,8,7]
build_max_heap(lista)
print(lista)



