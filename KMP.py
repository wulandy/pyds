import argparse


def same(pattern):
    length = len(pattern)
    max_same_len = 0
    for i in range(1, length):
        if (pattern[0:i] == pattern[length - i:length]):
            max_same_len = i
    return max_same_len
def getnext(pattern):
    t=[]
    for i in range(len(pattern)+1)[1:]:
        t.append(same(pattern[0:i]))
    return t
def kmp(t, p,post=0):
    n = len(t)
    m = len(p)
    next = getnext(p)
    j = post
    for i in range(n):
        while j > 0 and p[j] != t[i]:
            j = next[j - 1]
        if p[j] == t[i]:
            j = j + 1
        if j == m:
            return i - m + 1
    return -1
if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-t', dest='text', action='store', help="please input text")
    parse.add_argument('-p', dest='pattern', action='store', help="please input a pattern")
    parse.add_argument('-post', dest='post', action='store', help="please input a inorderteaver")
    args = parse.parse_args()
    s1=args.text
    s2=args.pattern
    post=int(args.post)
    print kmp(s1,s2,post)