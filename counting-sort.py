#suppose to have a list of number from 1 to 5 as input to be sorted (since you have to know in advance your input)
#k=len(C)=5 #tells you that your input data are integers that go form zero to five
listabella=[2,5,3,0,2,3,0,3]
#a is actually your input list

def counting_sort(A,k):
    C=[]
    for i in range(k+1):
        C.append(0)
        #print(C)
    for j in range(len(A)):
        C[A[j]]=C[A[j]] + 1
        #print(C[A[j]])
            #C[i]= contains the number of times that i , so A[j] is preset in A.
    for i in range(1,k+1):
        C[i] = C[i] + C[i -1]
    print(C)
    #here you compute the number of elements in the list untill i.
    B=[]
    for i in range(len(A)):
        B.append(0)
    #print(B)
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] =A[j]
        C[A[j]] = C[A[j]] - 1
    print(B)

print(counting_sort(listabella,5))