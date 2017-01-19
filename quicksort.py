import random

def once(list):
    low=0
    high=len(list)-1
    privo=list[0]
    while low<high:
        while list[high]>=privo and low<high:
            high-=1
        list[low]=list[high]
        while list[low]<=privo and low <high:
            low+=1
        list[high]=list[low]
    list[low]=privo
    return low

def quicksort(list):
    if len(list)<=1:
        return list
    else:
        num=once(list)
        return quicksort(list[:num])+[list[num]]+quicksort(list[num+1:])

if __name__=='__main__':
    list=[]
    for i in range(10):
        list.append(random.randint(0, 1000))
    list=quicksort(list)
    print list