def partition(lista,p,r):
    x=lista[r]
    i= p-1

    for j in range (p,r):
        if lista[j]< x:
            i=i+1
            estremo=lista[i]
            lista[i] = lista[j]
            lista[j]= estremo


    lista[i+1], lista[r] = lista[r] , lista[i+1]

    return (i+1)

#x, y = y, x is a good way to exchange variables values.

def quick_sort(lista,p,r):
     if p<r:
         q= partition(lista,p,r)
         print('sortint on', lista[p:q - 1])
         quick_sort(lista,p,q-1)
         print(lista[p:q - 1])
         print('sortint on', lista[q + 1:r])


         quick_sort(lista, q+1,r)


array=[2,8,7,1,3,5,6,4]
quick_sort(array,0,len(array)-1)
print(array)