gioielli=['anello', 'collana', 'ciondolo','bracciale']
valore=[30,15,100,50]
peso=[15,2,70,9]
capienza=66
def knap(item,v,w,W):
    ratio=[]
    for i in range(len(item)):
        val=v[i]/w[i]
        ratio.append((val,i))
    #print(ratio)
    ratio.sort(reverse=True,key=lambda x: x[0]) #sorts from the higest to the lowest according to ratio
    print(ratio)
    knap=0 #peso aggiornato del sacco
    knapel=[] #lista di elementi messi nel sacco
    for el in ratio:
        if knap + w[el[1]] < W:
            knap=knap + w[el[1]]
            knapel.append(item[el[1]])
        else:
            diff= W-knap
            fract= float(diff/w[el[1]])
            knapel.append('the %s of ' %(round((fract),2)) + item[el[1]])
            knap= knap + float(fract)* float( w[el[1]])

    print(knap)
    print(knapel)
print(knap(gioielli,valore,peso,capienza))