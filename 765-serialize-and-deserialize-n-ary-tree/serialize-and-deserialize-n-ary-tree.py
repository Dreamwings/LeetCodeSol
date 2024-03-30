"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        def ser_helper(node, arr):
            if not node: return
            arr.append(str(node.val))
            arr.append(str(len(node.children)))
            
            for child in node.children:
                ser_helper(child, arr)
        
        arr = []
        ser_helper(root, arr)
        return ','.join(arr)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data: return None
        arr = data.split(',')
        self.idx = 0
        
        def des_helper(arr):
            if self.idx == len(arr): return None
            
            node = Node(arr[self.idx], [])
            self.idx += 1
            num = int(arr[self.idx])
            self.idx += 1
            for _ in range(num):
                x = des_helper(arr)
                node.children.append(x)
            return node
        
        root = des_helper(arr)
        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))