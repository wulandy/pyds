#coding=utf-8
import argparse
from collections import deque
from binarytree import Node, pprint
'''708:Huffman编码树
描述
    构造一个具有n个外部节点的扩充二叉树，每个外部节点Ki有一个Wi对应，作为该外部节点的权。使得这个扩充二叉树的叶节点带权外部路径长度总和最小：
                                         Min( W1 * L1 + W2 * L2 + W3 * L3 + … + Wn * Ln)
    Wi:每个节点的权值。
    Li:根节点到第i个外部叶子节点的距离。
    编程计算最小外部路径长度总和。
输入
    输入n个整数，代表各个外部节点的权值。
    2<=N<=100
输出
    输出最小外部路径长度总和。
样例输入
    1 1 3 5
样例输出
    17
'''

def sort(list):
    return sorted(list,key=lambda node:node.value)

def huffman(list,wpl):
     while len(list)!=1:
         list=sort(list)
         left=list[0]
         right=list[1]
         node=Node(left.value+right.value)
         wpl+=node.value
         node.left=left
         node.right=right
         list.remove(left)
         list.remove(right)
         list.append(node)
     return list,wpl
def orderTraver(node):
    if node!=None:
        orderTraver(node.left)
        print node.value
        orderTraver(node.right)
'''样例输入
    1 1 3 5
样例输出
    17'''

list = []
parse=argparse.ArgumentParser()
parse.add_argument('-n',dest='num',action='store',help="how many number?")
args=parse.parse_args()
b=int(args.num)
i=1
while i<=b:
   i++1
   print 'please input the %dth number' % i,
   i=input()
   list.append(Node(i))
wpl = 0
list, wpl = huffman(list, wpl)
pprint(list)
   # wpl=wplclass(node=list[0]).wplreturn()
print  "wpl=%d" %wpl




'''
#从一个已知的huffman树中计算wpl的算法
# wpl=wplclass(node=根节点).wplreturn()
class wplclass(object):
    def __init__(self, w=0, node=None):
        self.w = w
        self.node = node

    def isLeafNode(self, Node):
        if Node.left == None and Node.right == None:
            return True
        return False

    def wpldef(self, node):
        if node != None:
            print node, self.isLeafNode(node)
            self.wpldef(node.left)
            if self.isLeafNode(node) == False:
                self.w += node.value
            self.wpldef(node.right)

    def wplreturn(self):
        self.wpldef(self.node)
        return self.w
'''

