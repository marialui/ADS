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
    for i in range((len(array)//2)-1,-1,-1):
        max_heapify(array,i)

def heapsort(lista):
    build_max_heap(lista)
    size =len(lista)
    k=0
    for i in range((size-1),0,-1):
        top=lista[0]
        lista[0]=lista[i]
        lista[i]=top
        k=k+1
        nuovalista=lista[:-k]
        max_heapify(nuovalista,0)
        lista[:-k]=nuovalista


A=[7,4,3,2,1]


heapsort(A)
print(A)