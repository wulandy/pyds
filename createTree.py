import argparse
from collections import deque
from binarytree import Node, pprint
import traver
class createTree(object):
    def __init__(self, s, n):
        self.s = s
        self.i = 0
        self.n = n
        self.n = self.create(self.n)

    def create(self, n):
        ch = self.s[self.i]
        self.i += 1
        if ch == '*':
            n = None
        else:
            n = Node(value=ch)
            n.left = self.create(n.left)
            n.right = self.create(n.right)
        return n
def depth(root):
    if root==None:
        return 0
    m=depth(root.left)
    n=depth(root.right)
    return max(m,n)+1

if __name__=="__main__":
    parse = argparse.ArgumentParser()
    parse.add_argument('-s', dest='Strings', action='store', help="input a string")
    args = parse.parse_args()
    s=args.Strings
    root=createTree(s,Node(0)).n
    pprint(root)
    print "preorder;",
    traver.preorderTraver(root)
    print
    print "preorder Without Rec;",
    traver.prenoRe(root)
    print
    print "inorder;",
    traver.inorderTraver(root)
    print
    print "postorder;",
    traver.postorderTraver(root)
    print
    print "layorder:",
    traver.layerTraver(root)
    print
    print "depth:%d"   %depth(root)
