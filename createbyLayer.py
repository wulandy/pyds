#coding=utf-8
import argparse

from binarytree import  Node,pprint
#题目5—建立二叉树3(由层序字符序列建立二叉树) //加分
def cbl(s):
    t=[]
    for i in s:
        if i=='*':
            n=None
        else:
            n=Node(i)
        t.append(n)
    for i in range(len(s)):
        if 2*i+1<len(s):
            t[i].left=t[2*i+1]
        if 2 * i + 2 < len(s):
            t[i].right = t[2 * i + 2]
    return t[0]
if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-s', dest='Strings', action='store', help="input a string")
    args = parse.parse_args()
    s=args.Strings
    pprint(cbl(s))