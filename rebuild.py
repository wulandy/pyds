import argparse

from binarytree import Node,pprint
import traver
def create(list1,list2):
    if len(list2)==0:
        return None
    root=Node(list2[-1])
    try:
        str1 = list1[0:list1.index(list2[-1])]
    except:
        str1=''
    try:
        str2 = list1[list1.index(list2[-1]) + 1:]
    except:
        str2=''
    text1=[]
    text2=[]
    for i in list2:
        if i in str1:
            text1.append(i)
    for i in list2:
        if i in str2:
            text2.append(i)
    text1=''.join(text1)
    text2=''.join(text2)
    root.left=create(str1,text1)
    root.right = create(str2,text2)
    return root
if __name__=="__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-in', dest='list1', action='store', help="please input a inorderteaver")
    parse.add_argument('-post', dest='list2', action='store', help="please input a postordertraver")
    args = parse.parse_args()
    # list1="ADEFGHMZ"
    # list2="AEFDHZMG"
    list1=args.list1
    list2=args.list2
    root=create(list1,list2)
    pprint(root)
    print 'layertarver:',
    traver.layerTraver(root)