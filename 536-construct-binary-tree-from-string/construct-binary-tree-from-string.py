# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        

        ## S1: DFS
        ## T: O(N^2)
        ## S: O(N)

        def dfs(s):
            if not s:
                return None
            p = s.find('(')
            if p == -1:
                return TreeNode(int(s))
            root = TreeNode(int(s[:p]))
            start = p
            cnt = 0
            for i in range(p, len(s)):
                if s[i] == '(':
                    cnt += 1
                elif s[i] == ')':
                    cnt -= 1
                if cnt == 0:
                    if start == p:
                        root.left = dfs(s[start + 1 : i])
                        start = i + 1
                    else:
                        root.right = dfs(s[start + 1 : i])
            return root

        return dfs(s)

        """
        ## S2: Stack

        if not s:
            return None
        
        root = TreeNode()
        stack = [root]
        
        index = 0
        while index < len(s):
            
            node = stack.pop()

            # NOT_STARTED
            if s[index].isdigit() or s[index] == '-':
                value, index = _getNumber(s, index)
                node.val = value

                # Next, if there is any data left, we check for the first subtree
                # which according to the problem statement will always be the left child.
                if index < len(s) and s[index] == '(':
                    stack.append(node)

                    node.left = TreeNode()
                    stack.append(node.left)
            
            # LEFT_DONE
            elif node.left and s[index] == '(':
                stack.append(node)

                node.right = TreeNode()
                stack.append(node.right)
            
            index += 1
        return stack.pop() if stack else root
    
        def _getNumber(s: str, index: int) -> (int, int):
            
            is_negative = False
            
            # A negative number
            if s[index] == '-':
                is_negative = True
                index = index + 1
            
            number = 0
            while index < len(s) and s[index].isdigit():
                number = number * 10 + int(s[index])
                index += 1
            
            return number if not is_negative else -number, index

        """
