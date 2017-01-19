#coding=utf-8
from collections import deque
def preorderTraver(node):
    if node!=None:
        print node.value,
        preorderTraver(node.left)
        preorderTraver(node.right)
def prenoRe(root):
    if root==None:
        return
    stack=[]
    node=root
    while node!=None or stack!=[]:
        while node!=None:
            stack.append(node)
            print node.value,
            node=node.left
        node=stack.pop().right
def inorderTraver(node):
    if node!=None:
        inorderTraver(node.left)
        print node.value,
        inorderTraver(node.right)
def postorderTraver(node):
    if node!=None:
        postorderTraver(node.left)
        postorderTraver(node.right)
        print node.value,
def layerTraver(node):
    a=deque([node])
    while a!=deque([]):
        a = deque([node])
        while a != deque([]):
            node = a[0]
            print node.value,
            if node.left != None:
                a.append(node.left)
            if node.right != None:
                a.append(node.right)
            a.popleft()
