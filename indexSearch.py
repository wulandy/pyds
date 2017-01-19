import argparse
import random

import time


def binsearch(list,key):
    low=0
    high=len(list)-1
    while low<=high:
        mid=(low+high)/2
        if key==list[mid]:
            return mid
        elif key<list[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1


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

def buildindex(list):
    list2=list
    list2=quicksort(list2)
    return list2
def search(list,key):
    for i in range(len(list)):
        if list[i]==key:
            return i
    return -1

if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-b',action='store_true',help="build an index")
    parse.add_argument('-key', dest='key', action='store',type=int, help="please input the num you want to find")
    parse.add_argument('-i', action='store_true', help="find by index")
    parse.add_argument('-c',action='store_true' ,help="find by common")
    args=parse.parse_args()
    list=[]
    for i in range(500000):
        list.append(random.randint(0,1000))
    index=[]
    if args.b:
        index=buildindex(list)
    if args.c:
        start=time.time()
        if args.key:
            print search(list,args.key)
        else:
            print 'please input -key [key]'
        end=time.time()
        print 'time is',
        print end - start
    if args.i:
        start = time.time()
        if args.c:
            print 'you only can choose common search or index search!'
        elif args.key:
            if index==[]:
                print 'please input -b to build a index'
            else:
                print binsearch(index,args.key)
                end = time.time()
                print 'time is',
                print end - start
        else:
            print 'please input -key [key]'





