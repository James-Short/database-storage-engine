
class BTreeNode:
    def __init__(self, leaf=True):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t 
        
    def split_child(self, x, i):
        t = self.t
        
        y = x.children[i]
        
        z = BTreeNode(y.leaf)
        x.children.insert(i+1, z)
        
        x.keys.insert(i, y.keys[t-1])
        
        z.keys = y.keys[t: (2 * 5) - 1]
        y.keys = y.keys[:t-1]
        
        if not y.leaf:
            z.children = y.children[t: 2 * t]
            y.children = y.children[:t]
    
    def insert(self, k):
        t = self.t
        root = self.root
        
        if(len(root.keys) == (2 * t) - 1 ):
            new_root = BTreeNode()
            self.root = new_root
            new_root.children.insert(0, root)
            self.split_child(new_root, 0)
            self.insert_non_full(new_root, k)
        else:
            self.insert_non
    
    def insert_non_full(self, x, k):
        t = self.t
        i = len(x.keys) - 1
        
        if x.leaf:
            x.keys.append(None)
            while i >= 0 and k < x.keys[i]:
                x.keys[i+1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            
            if len(x.children[i].keys) == (2 * 5) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.children[i], k)
    
