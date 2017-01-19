
  ######二叉树
#题目4—	二叉搜索树//特别加分
<pre>
D:\PycharmProjects\DS2>python BST.py -h
usage: BST.py [-h] [-d KEY]

optional arguments:
  -h, --help  show this help message and exit
  -d KEY      please input the num you want to del

D:\PycharmProjects\DS2>python BST.py
[41, 467, 334, 500, 169, 724, 478, 358, 962, 464, 705, 145, 281, 827, 961, 491, 995, 942, 827, 436]

41_____________________________
                               \
                  _____________467_________
                 /                         \
          _____334_                   _____500_____
         /         \                 /             \
      _169_        358_____        478_           _724_________________
     /     \               \           \         /                     \
   145     281            _464         491     705            _________962_
                         /                                   /             \
                       436                                _827_____        995
                                                         /         \
                                                       827        _961
                                                                 /
                                                               942
</pre>
<pre>
D:\PycharmProjects\DS2>python BST.py -d 467
[41, 467, 334, 500, 169, 724, 478, 358, 962, 464, 705, 145, 281, 827, 961, 491, 995, 942, 827, 436]

41_____________________________
                               \
                  _____________467_________
                 /                         \
          _____334_                   _____500_____
         /         \                 /             \
      _169_        358_____        478_           _724_________________
     /     \               \           \         /                     \
   145     281            _464         491     705            _________962_
                         /                                   /             \
                       436                                _827_____        995
                                                         /         \
                                                       827        _961
                                                                 /
                                                               942


41_________________________
                           \
                  _________464_________
                 /                     \
          _____334_               _____500_____
         /         \             /             \
      _169_        358_        478_           _724_________________
     /     \           \           \         /                     \
   145     281         436         491     705            _________962_
                                                         /             \
                                                      _827_____        995
                                                     /         \
                                                   827        _961
                                                             /
                                                           942
</pre>
#选做：题目8—倒排索引//特别加分
<pre>
D:\PycharmProjects\DS2>python reverse.py -h
usage: reverse.py [-h] [-f FILENAME]

optional arguments:
  -h, --help   show this help message and exit
  -f FILENAME  FILENAME

D:\PycharmProjects\DS2>python reverse.py -f reverse.txt
a: 2
is: 0 1 2
it: 0 1 2
banana: 2
what: 0 1
</pre>
#选做：题目6—索引查找及改进//特别加分
1.	3.new一个n=5w个大小的int型数组BigIntArr，里面填写从0到50000的随机数。现在需要频繁的根据在该数组中查看某个数是否存在 (但又不想对该数组进行排序),如果使用顺序查找，效率很低。如何改进？ 
2.	输出你改进的查找所需要的比较次数并和普通线性查找Search进行对比？试分析比较次数与n之间的关系是什么？即时间复杂度是多少?
3.	提示：稠密索引(尝试打印出比较次数)
4.	查看程序运行时间：在排序开始前 cout << "开始查找" << endl;结束后 cout << "结束查找" << endl;查看排序耗费时间。进一步，修改n=50w，查看排序耗费时间。n=5kw呢。
##思考
其实本题我的实现并没有很贴近实际，因为我的做法是把一个列表复制过来之后再快速排序，然后使用折半查找，时间自然比普通查找方法快，而且索引有一个好处就算一次建索引，以后都可以用这个索引。。而我这题索引是每次都要建，但是时间不算在里面，这就出现一个尴尬的事--用索引明明时间更长，显示的确实时间更短，因为我建立索引的时间不算在里面。。后来，我想把索引藏在文件里面，以后调用。但是却发现每次都是新的随机树数，索引藏文件并没有意义，，不过随机数也就测试用，实际中倒不会出现这个问题，应该可以存在文件里面。。
###还有一点
其实我把那个列表快排之后然后用快排，就不用这么麻烦，为什么还要建索引。后来，在谷歌的帮助下，我想到一下几个原因。。有不足之处
	
1. 原数列可能不想或者不能修改
2. 原数列不仅仅本体这么简单，，它每一项可能有一大排。而我们拿过来排序的只是它的关键点而已。。比如我常用的光速查找这个软件。。用建索引所花的空间就很小
<pre>
D:\PycharmProjects\DS2>python indexSearch.py -h 
usage: indexSearch.py [-h] [-b] [-key KEY] [-i] [-c]

optional arguments:
  -h, --help  show this help message and exit
  -b          build an index
  -key KEY    please input the num you want to find
  -i          find by index
  -c          find by common

D:\PycharmProjects\DS2>python indexSearch.py -key 28 -c
1362
time is 0.00799989700317

D:\PycharmProjects\DS2>python indexSearch.py -key -b -key 28 -i
usage: indexSearch.py [-h] [-b] [-key KEY] [-i] [-c]
indexSearch.py: error: argument -key: expected one argument
D:\PycharmProjects\DS2>python indexSearch.py -b -key 28 -i
14158
time is 0.000999927520752
</pre>
#题目5—字典//考核+1
<pre>
D:\PycharmProjects\DS2>python dic.py -h
usage: dic.py [-h] [-f FILENAME] [-s STRING]

optional arguments:
  -h, --help   show this help message and exit
  -f FILENAME  FILENAME
  -s STRING    please input the num you want to tranlate

D:\PycharmProjects\DS2>python dic.py -f dic.txt -s igpay
pig
</pre>
=============================================================

  ######二叉树 栈和队列
#选做：题目5—走迷宫//特别加分
labyrinth.py  在命令行下执行python labyrinth.py 其中迷宫是默认的，可以去掉随机数那几行的注释产生随机地图（不过这种正常都没有路)，输出迷宫地图和路径
<pre>
C:\Users\dai\Desktop\083戴志斌数据结构\201521123083戴志斌第三次>python labyrinth.py
0 0 1 1 1
1 0 0 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 0 0
(0, 0)
(0, 1)
(1, 1)
(1, 2)
(1, 3)
(2, 3)
(3, 3)
(4, 3)
(4, 4)
</pre>
#题目2—	回文数字(栈和队列)
pali.py 在命令行下执行python pali.py -s 字符串 （可以输入-h查看帮助)
<pre>
C:\Users\dai\Desktop\083戴志斌数据结构\201521123083戴志斌第三次>python pali.py -h
usage: pali.py [-h] [-s STRINGS]

optional arguments:
  -h, --help  show this help message and exit
  -s STRINGS  please input a string

C:\Users\dai\Desktop\083戴志斌数据结构\201521123083戴志斌第三次>python pali.py -s 123
False

C:\Users\dai\Desktop\083戴志斌数据结构\201521123083戴志斌第三次>python pali.py -s asdfdsa
True
</pre>
#选做：题目6—杨辉三角(队列)
yanghui.py 在命令行下执行python yanghui.py -n  行数
<pre>
C:\Users\dai\Desktop\083戴志斌数据结构\201521123083戴志斌第三次>python yanghui.py -n 5
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
</pre>
#选做：题目7—括号匹配
bracket.py 在命令行下执行python bracket.py -s 字符串
<pre>
C:\Users\dai\Desktop\083戴志斌数据结构\201521123083戴志斌第三次>python bracket.py -h
usage: bracket.py [-h] [-s STRINGS]

optional arguments:
  -h, --help  show this help message and exit
  -s STRINGS  please input a tring

C:\Users\dai\Desktop\083戴志斌数据结构\201521123083戴志斌第三次>python bracket.py -s ((())
Extra left brackets
</pre>
===========================================================

  ######字符串
#KMP算法
<pre>
D:\PycharmProjects\DS>python KMP.py -h
usage: KMP.py [-h] [-t TEXT] [-p PATTERN] [-post POST]

optional arguments:
  -h, --help  show this help message and exit
  -t TEXT     please input text
  -p PATTERN  please input a pattern
  -post POST  please input a inorderteaver

D:\PycharmProjects\DS>python KMP.py -t "abcadfr" -p "cad" -post 0
2
</pre>
# 选做：题目4—统计单词的出现次数并输出(特别加分)
message.txt的内容 This is just a test test test test for this
<pre>
D:\PycharmProjects\DS>python tongji.py -h
usage: tongji.py [-h] [-r FILE]

optional arguments:
  -h, --help  show this help message and exit
  -r FILE     please input a inorderteaver

D:\PycharmProjects\DS>python tongji.py -r message.txt
a ------> 1
just ------> 1
for ------> 1
is ------> 1
this ------> 2
test ------> 4
</pre>
#选做：题目5—判断字符串是否为数(特别加分)
<pre>
D:\PycharmProjects\DS>python isDigit.py -h
usage: isDigit.py [-h] [-s STRINGS]

optional arguments:
  -h, --help  show this help message and exit
  -s STRINGS  please input a string

D:\PycharmProjects\DS>python isDigit.py -s 123
True

D:\PycharmProjects\DS>python isDigit.py -s -123
True

D:\PycharmProjects\DS>python isDigit.py -s a13
False
</pre>
#	全在其中(考核+1)
给定两个字符串s和t，你需要判断s是否是t的“子列”。也就是说，如果你去掉t中的某些字符，剩下字符将连接而成为s。
<pre>
例子：
sequence  subsequence -->YES34
person   compression -->NO
VERDI	 vivaVittorioEmanueleReDiItalia	-->YES
caseDoesMatter  CaseDoesMatter	-->NO
</pre>
<pre>
D:\PycharmProjects\DS>python allin.py -h
usage: if list1 is the substr of list2 print 'YES',else 'NO'
       [-h] [-s LIST1] [-t LIST2]

optional arguments:
  -h, --help  show this help message and exit
  -s LIST1    please input a string
  -t LIST2    please input a string

D:\PycharmProjects\DS>python allin.py -s VERDI -t vivaVittorioEmanueleReDiItalia
YES

D:\PycharmProjects\DS>python allin.py -s caseDoesMatter -t CaseDoesMatter
No
</pre>
# 英语数字转换器  
<pre>
例子:  
	six   6  
	negative seven hundred twenty nine   -729  
	one million one hundred one  1000101  
	eight hundred fourteen thousand twenty two   814022  
</pre>
<pre>
D:\PycharmProjects\DS>python dic.py -h
usage: dic.py [-h] [-s STRINGS]

optional arguments:
  -h, --help  show this help message and exit
  -s STRINGS  please input a string

D:\PycharmProjects\DS>python dic.py -s  "eight hundred fourteen thousand twenty two"
814022
</pre>
==============================

   ######查找排序
>tip：画图使用一个模块binarytree  
>运行下面代码先安装(pip install binarytree)  
>该模块github地址[https://github.com/joowani/binarytree](https://github.com/joowani/binarytree "https://github.com/joowani/binarytree")  
>这个模块集成很多二叉树功能，但我这次作业除了使用它的画图功能，其他都是自己实现的
#题目6—Huffman编码树//特别加分
<pre>
D:\PycharmProjects\DS>python Huffman.py -h
usage: Huffman.py [-h] [-n NUM]

optional arguments:
  -h, --help  show this help message and exit
  -n NUM      how many number?

D:\PycharmProjects\DS>python Huffman.py -n 4
please input the 1th number 1
please input the 1th number 1
please input the 1th number 3
please input the 3th number 5


  10______
 /        \
5        __5
        /   \
       2     3
      / \
     1   1

                                                                                                                      
wpl=17
</pre>
#先序字符串建立二叉树与遍历   
并且使用递归实现先序遍历，中序遍历，后序遍历，使用栈实现先序遍历，使用队列实现层序遍历并求深度
<pre>
D:\PycharmProjects\DS>python createTree.py -h
usage: createTree.py [-h] [-s STRINGS]

optional arguments:
  -h, --help  show this help message and exit
  -s STRINGS  input a string

D:\PycharmProjects\DS>python createTree.py -s ABC**DE*G**F**HI**J**

    ________A__
   /           \
  B____         H
 /     \       / \
C     __D     I   J
     /   \
    E     F
     \
      G
preorder; A B C D E G F H I J
preorder Without Rec; A B C D E G F H I J
inorder; C B E G D F A I H J
postorder; C G E F D B I J H A
layorder: A B H C D I J E F G
depth:5
</pre>
#给定一棵二叉树的中序遍历和后序遍历的结果，求其层序遍历
<pre>
参考（中序:"ADEFGHMZ",后序:"AEFDHZMG"）
D:\PycharmProjects\DS>python rebuild.py -h
usage: rebuild.py [-h] [-in LIST1] [-post LIST2]

optional arguments:
  -h, --help   show this help message and exit
  -in LIST1    please input a inorderteaver
  -post LIST2  please input a postordertraver

D:\PycharmProjects\DS>python rebuild.py -in ADEFGHMZ -post AEFDHZMG

    ____G__
   /       \
  D__       M
 /   \     / \
A     F   H   Z
     /
    E

layertarver: G D M A F H Z E
</pre>
（四）题目5—建立二叉树3(由层序字符序列建立二叉树) //加分
<pre>
D:\PycharmProjects\DS>python createbyLayer.py -h
usage: createbyLayer.py [-h] [-s STRINGS]

optional arguments:
  -h, --help  show this help message and exit
  -s STRINGS  input a string

D:\PycharmProjects\DS>python createbyLayer.py -s ACD*EF*

  __A__
 /     \
C       D
 \     /
  E   F
</pre>
