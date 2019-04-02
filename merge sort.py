from math import inf
array=[5,7,44,2,34,99,1,22,4,8,5]
p= 0
r =len(array)

def mergesort (lista,beg,end):
    if beg < end-1:
        q=int((beg + end)/2)
        
        mergesort (lista,beg,q)
        mergesort(lista,q,end)
        merge (lista, beg,q,end)
    return lista

def merge (lista, beg,q,end):
    
    left=lista[beg:q]
    right=lista[q:end]
    right.append(inf)
    left.append(inf)
    i=0
    j=0
    
    for k in range(beg,end):
        if left[i]<= right[j]:
            lista[k] = left[i]
            i=i+1
        else:
            lista[k]=right[j]
            j=j+1
    
    return lista

print(mergesort(array,p,r))


