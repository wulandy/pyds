import argparse

if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-f', dest='FILENAME', action='store', help="FILENAME")
    parse.add_argument('-s', dest='string', action='store',  help="please input the num you want to tranlate")
    args = parse.parse_args()
    filename=args.FILENAME
    with open(filename,'r') as f:
        s=f.readlines()
    dic={}
    for i in s:
        i=i.strip()
        i=i.split(' ')
        dic[i[1]]=i[0]
    s=args.string
    if dic.has_key(s):
        print dic[s]