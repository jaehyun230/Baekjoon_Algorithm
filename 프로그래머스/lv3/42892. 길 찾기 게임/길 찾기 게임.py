import sys
sys.setrecursionlimit(10**4)

class Tree :
    def __init__(self, datalist) :
        self.val= max(datalist, key=lambda x :x[1])
        leftList =list(filter(lambda x :x[0] < self.val[0] , datalist))
        rightList = list(filter(lambda x :x[0] > self.val[0] , datalist))
        
        if leftList != []:
            self.left=Tree(leftList)
        else :
             self.left=None
        if rightList != []:
            self.right=Tree(rightList)
        else :
             self.right=None

def solution(nodeinfo):
    answer = []
    preorder = []
    postorder = []
    
    root = Tree(nodeinfo)
    
    def dfs(node) :
        if not node :
            return
        preorder.append(node.val)
        if node.left :
            dfs(node.left)
        if node.right :
            dfs(node.right)
        postorder.append(node.val)
    
    dfs(root)
    
    pre = []
    post = []
    
    for i in preorder :
        pre.append(nodeinfo.index(i)+1)
    for j in postorder:
        post.append(nodeinfo.index(j)+1)
    answer.append(pre)
    answer.append(post)
    
    return answer