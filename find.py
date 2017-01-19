#coding=utf-8
#题目3—折半查找
import time

def search(list,key):
    compare=0
    for i in range(len(list)):
        compare+=1
        if key==list[i]:
            return i,compare
    return -1,compare
def binsearch(list,key):
    low=0
    high=len(list)-1
    compare=0
    while low<=high:
        compare+=1
        mid=(low+high)/2
        if key==list[mid]:
            return mid,compare
        elif key<list[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1,compare
if __name__=='__main__':
    list=[]
    for i in range(100)[1:]:
        list.append(i)
    print "common search:",
    location,compare=search(list,99)
    if location==-1:
        print 'No found'
    else:
        print location,
        print "compare=%d" %compare
    print "binsearch:",
    location, compare = binsearch(list, 99)
    if location == -1:
        print 'No found'
    else:
        print location,
        print "compare=%d" % compare
