#coding=utf-8
#二叉搜索树的创建
import argparse

from binarytree import Node,pprint
def insertBST(s,node):
    if s==None:
        s=node
    elif node.value<=s.value:
        s.left=insertBST(s.left,node)
    else:
        s.right=insertBST(s.right,node)
    return s

def createBST():
    N=None
    list=[41 ,467 ,334 ,500, 169 ,724, 478 ,358, 962 ,464,705 ,145 ,281 ,827 ,961, 491 ,995 ,942, 827 ,436]
    for i in list:
        nodes=Node(i)
        N=insertBST(N,nodes)
    return N
def find(f,value):
    if f==None:
        return None
    if f.value==value:
        return f
    if value<=f.value:
        return find(f.left,value)
    else:
        return find(f.right,value)

def findMin(root):
    if root.left:
        return findMin(root.left)
    else:
        return root

def findMax(root):
    if root.right:
        return findMax(root.right)
    else:
        return root

def delete(root,x):
    if find(root,x):
        if x<root.value:
            root.left=delete(root.left,x)
            return root
        elif x>root.value:
             root.right=delete(root.right,x)
             return root
        elif root.left and root.right:
             last=findMax(root.left)
             root.value=last.value
             root.left=delete(root.left,last.value)
             return root
        else:
            if root.left:
                return root.left
            else:
                return root.right
    else:
        return root

if __name__=='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-d', dest='key', action='store', type=int, help="please input the num you want to del")
    args=parse.parse_args()
    list = [41, 467, 334, 500, 169, 724, 478, 358, 962, 464, 705, 145, 281, 827, 961, 491, 995, 942, 827, 436]
    print list
    root=createBST()
    pprint(root)
    if args.key:
        delete(root,args.key)
        pprint(root)
'''样例输入：41 467 334 500 169 724 478 358 962 464 705 145 281 827 961 491 995 942 827 436 '''
'''样例输出：41 467 334 169 145 281 358 464 436 500 478 491 724 705 962 827 961 942 995 '''




