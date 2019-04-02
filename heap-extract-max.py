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

def heap_extract_max (lista):
    if len(lista)<1:
        print('error :heap underflow')
    else :
        max=lista[0]
        lista.pop(0)
        lista[0] = lista[len(lista) - 1]
        max_heapify(lista,0)
        return max

happy=[16,14,10,8,7,9,3,2,4,1]
print(heap_extract_max(happy))
print(happy)