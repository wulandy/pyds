#coding=utf-8
# 给定两个字符串s和t，你需要判断s是否是t的“子列”。也就是说，如果你去掉t中的某些字符，剩下字符将连接而成为s。
import argparse


def allin(s,q):
    t=0
    for i in s:
        t=q.find(i,t)
        if t==-1:
            return False
    return True
if __name__=='__main__':
    parse = argparse.ArgumentParser('if list1 is the substr of list2 print \'YES\',else \'NO\'')
    parse.add_argument('-s', dest='list1', action='store', help="please input a string")
    parse.add_argument('-t', dest='list2', action='store', help="please input a string")
    args = parse.parse_args()
    s=args.list1
    t=args.list2
    # sequence
    # subsequence
    #person
    #compression
    # VERDI
    # vivaVittorioEmanueleReDiItalia
    # caseDoesMatter
    # CaseDoesMatter
    if allin(s,t):
        print "YES"
    else:
        print "No"

