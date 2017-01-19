import argparse

if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-f', dest='FILENAME', action='store', help="FILENAME")
    args=parse.parse_args()
    with open(args.FILENAME,'r') as f:
        s=f.readlines()
    list=[]
    j=0
    for i in s:
        i=i.split()
        list.append(i)
    dic={}
    for i in range(len(list)):
        for j in list[i]:
            if not dic.has_key(j):
                dic[j]=set([i])
            else:
                dic[j].add(i)
    for i ,sets in dic.iteritems():
        print i+":",
        for j in sets:
            print j,
        print