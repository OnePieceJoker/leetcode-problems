## 700. Search in a Binary Search Tree ![](https://img.shields.io/badge/-easy-green.svg)

给定二叉搜索树（BST）的根节点和一个值。你需要在BST中找到节点值等于给定值的节点。返回以该节点为根的子树。如果节点不存在，就返回NULL。

### 例如
    给定二叉搜索树：
            4
           / \
          2   7
         / \
        1   3

    和值：2

    你应该返回如下子树：
          2 
         / \
        1   3

    在上述示例中，如果要找的值是5，但因为没有节点值为5，我们应该返回NULL。