import argparse
from itertools import izip
def bracketMatch(s):
    q=list();
    left=('(','[','{')
    right=(')',']','}')
    all=set(left) | set(right)
    dic = dict(izip(right, left))
    for i in s:
        if i in all:
            if i in left:
                q.append(i)
            else:
                if q==[]:
                    print 'Extra right brackets'
                    return
                elif q[-1]==dic[i]:
                    q.pop()
                elif q[-1]!=dic[i]:
                    print 'Brackets not match'
                    return
    if q==[]:
        print 'Brackets match'
    else:
        print 'Extra left brackets'
if __name__=='__main__':
    parse=argparse.ArgumentParser()
    parse.add_argument('-s',dest='STRINGS',help='please input a tring')
    s=parse.parse_args().STRINGS
    bracketMatch(s)
