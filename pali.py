#coding=utf-8
from collections import deque
import argparse
def pali(s):
    q = list(s)
    for i in range(len(s)):
        if q.pop()!=s[i]:
            return False
    return True
parse=argparse.ArgumentParser()
parse.add_argument('-s',dest='strings',action='store',help="please input a string")
args=parse.parse_args()
print pali(args.strings)