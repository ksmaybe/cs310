from math import inf
def pun(l,lst):
    fees=[[0]* len(lst) for i in range(len(lst))]
    for i in range(len(lst)):
        length=len(lst[i])
        fees[i][i]=(l-length)**3
        k=1
        fee=l-length
        for j in range(i+1,len(lst)):
            fee-=len(lst[j])+1
            k+=1
            fees[i][j]=((fee)/k)**3
            if fees[i][j]<0:
                fees[i][j]=inf
    print(fees)

    min_fees=[inf for i in range(len(lst))]
    min_prev=[0 for i in range(len(lst))]
    for i in range(len(lst)):
        for j in range(i+1):
            if fees[j][i]!=inf:
                if j-1<0:
                    if min_fees[i]>0+fees[j][i]:
                        min_fees[i]=fees[j][i]
                        min_prev[i]=j
                if min_fees[i]>min_fees[j-1]+fees[j][i]:
                    min_fees[i]=min_fees[j-1]+fees[j][i]
                    min_prev[i]=j
    return min_fees[-1]


results = []
    i = len(words) - 1
    while i >= 0 :
        results.append(words[best_prev[i] : (i + 1)])
        i = best_prev[i] - 1
    print(best_cost)
    print(best_prev)

    return results[::-1]