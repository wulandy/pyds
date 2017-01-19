#coding=utf-8
import argparse
from collections import deque
def yanghui(i):
    s=deque([])
    s.append(1)
    s.append(0)
    i-=1
    num=9999
    while i>=0:
        i-=1
        s.append(1)
        while True:
            num=s[0]
            if num==0:
                s.popleft()
                break
            s.append(s[0]+s[1])
            s.popleft()
            print num,
        s.append(0)
        print

parse=argparse.ArgumentParser()
parse.add_argument('-n',dest='num',action='store',help="please input a number")
args=parse.parse_args()
yanghui(int(args.num))