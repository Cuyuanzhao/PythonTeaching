class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs(treeNode):
    if not treeNode:
        return
    dfs(treeNode.left)
    dfs(treeNode.right)
    print(treeNode.val)



if __name__ == '__main__':
    treeNode1 = TreeNode(1)
    treeNode2 = TreeNode(2)
    treeNode3 = TreeNode(3)
    treeNode4 = TreeNode(4)
    treeNode5 = TreeNode(5)
    treeNode3.left = treeNode2
    treeNode3.right = treeNode4
    treeNode2.left = treeNode1
    treeNode4.right = treeNode5
    dfs(treeNode3)

