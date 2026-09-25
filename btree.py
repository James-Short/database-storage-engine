
class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf

class BTree:
    def __init__(self):
        self.root = BTreeNode(True)
        self.t = 3
        
    def split_child(self, node, child_index):
        
        target = node.keys[child_index]
        
        new_node = BTreeNode(target.leaf)
        node.children.insert(child_index+1, new_node)
        
        node.keys.insert(child_index, target.keys[self.t-1])
        
        #New_node gets keys to the right of median and target gets the ones to the left
        new_node.keys = target.keys[self.t:]
        target.keys = target.keys[:self.t-1]
        
        if not target.leaf:
            new_node.children = target.children[self.t:]
            target.children = target.children[:self.t]
    
    def insert(self, val):
        
        #If the root is full, create a new root and split the old one to open up space for insertions.
        #The new root will be the parent of the old one
        if len(self.root.keys) == 2 * self.t - 1:
            new_root = BTreeNode()
            old_root = self.root
            self.root = new_root
            new_root.children.insert(0, old_root)
            self.split_child(new_root, 0)
        
        #Continue with the insertion after correcting root if needed
        self.insert_non_full(self.root, val)
    
    def insert_non_full(self, node, val):
        insertionIndex = len(node.keys) - 1
        
        if node.leaf:
            node.keys.append(None)
            while insertionIndex >= 0 and val < node.keys[insertionIndex]:
                node.keys[insertionIndex + 1] = node.keys[insertionIndex]
                i -= 1
            node.keys[insertionIndex+1] = val 
        else:
            while insertionIndex >= 0 and val < node.keys[insertionIndex]:
                insertionIndex -= 1
            insertionIndex += 1
            
            if len(node.children[insertionIndex].keys) == 2 * self.t - 1:
                self.split_child(node, insertionIndex)
                if val > node.keys[insertionIndex]:
                    insertionIndex += 1
            self.insert_non_full(node.children[insertionIndex], val)
            