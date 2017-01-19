import argparse
def sta(s):
    dic={}
    for i in s.split():
        i=i.lower()
        if dic.has_key(i):
            dic[i]+=1
        else:
            dic[i]=1
    dic=sorted(dic.iteritems(),key=lambda d:d[1],reverse=False)
    for i in dic:
        print i[0],
        print '------>',
        print i[1]

if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-r', dest='file', action='store', help="please input a inorderteaver")
    args = parse.parse_args()
    filename=args.file
    with open(filename,'r') as f:
        s=f.read()
        sta(s)