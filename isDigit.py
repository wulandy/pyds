import argparse


def isDigit(s):
    try:
        int(s)
        return True
    except:
        return False
if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-s', dest='strings', action='store', help="please input a string")
    args = parse.parse_args()
    s=args.strings
    print isDigit(s)