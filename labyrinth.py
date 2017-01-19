import random
import time
class labyrinth():
    def __init__(self,map):
        self.map=map
        self.stack=[]
        self.acrossed=[]
    def canrun(self,point):
        x,y=point
        if point  in self.acrossed:
            return False
        if x<0 or y<0:
            return False
        if x>len(self.map)-1 or y>len(self.map[0])-1:
            return False
        try:
            if self.map[x][y]==1:
                return False
        except:
            print 'x,y=' + str(x)+ ','+ str(y)
        return True
    def right(self,point):
        x,y=point
        return x,y+1
    def down(self,point):
        x, y = point
        return x+1, y
    def left(self,point):
        x, y = point
        return x, y -1
    def up(self,point):
        x, y = point
        return x-1, y
    def run(self):
        self.stack.append((0,0))
        self.acrossed.append((0,0))
        dic={
            1:self.right,
            2:self.down,
            3:self.left,
            4:self.up
        }
        while self.stack!=[]:
            nowpoint = self.stack[-1]
            if nowpoint==(len(self.map)-1,len(self.map[0])-1):
                return self.stack
            else:
                i=1
                while i<=4:
                    if self.canrun(dic[i](nowpoint)):
                        self.stack.append(dic[i](nowpoint))
                        self.acrossed.append(dic[i](nowpoint))
                        break
                    else:
                        i+=1
                if i==5:
                    self.stack.pop()
        return None



s=[[0,0,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,0]]
# for i in range(len(s)):
#     for j in range(len(s[0])):
#         s[i][j]=random.randint(0,1)
# s[0][0]=0
for i in range(len(s)):
    for j in range(len(s[0])):
        print s[i][j],
    print
t=labyrinth(s)
road=t.run()
if road==None:
    print 'no road'
else:
    for i in road:
        print i
