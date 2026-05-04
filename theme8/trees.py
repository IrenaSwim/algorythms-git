from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
    def __repr__(self):
        return f'Node {self.val}'    

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
       self.root = self._insert(self.root, key)
    
    def _insert(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.val:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return node
    
    def _find_node(self, node, key):
        while node is not None:
            if node.val == key:
                return node
            elif key < node.val:
                return self._find_node(node.left, key)
            else:
                return self._find_node(node.right, key)
        return f'Узел со значением {key} не найден'    
            
        
    def search(self, key):
        if self.root is None:
            return None
        else:
            return self._find_node(self.root, key)
        
#вариант без рекурсии:
    # def search(self, key):
    #     if self.root is None:
    #         return None
    #     node = self.root
    #     while node is not None:
    #         if node.val == key:
    #             return node
    #         elif node.val > key:
    #             node = node.left 
    #         else:
    #             node = node.right    
    #     return f'Узел со значением {key} не найден'   

b_tree = BinaryTree() 
nodes = [10,20,30,40,50,60,70,80,90] 
for el in nodes:
    b_tree.insert(el)   
print(b_tree.search(60))
print()   
              
def breadth_first_traversal(root):
    if root is None:
        return 
    queue = deque([root]) 
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right) 
            
def traversal(root):
    if root:
        print(root.val, end=' ')
        traversal(root.left)
        traversal(root.right)
        
def sim_traversal(root):
    if root:
        sim_traversal(root.left) 
        print(root.val, end=' ')  
        sim_traversal(root.right) 
        
def reverse_traversal(root):
    if root:
        sim_traversal(root.left) 
        sim_traversal(root.right)
        print(root.val, end=' ')
        
breadth_first_traversal(b_tree.root)
print()
traversal(b_tree.root)
print()
sim_traversal(b_tree.root)
print()
reverse_traversal(b_tree.root)

class AVLNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1
        
class AVLTree(BinaryTree):
    def __init__(self):
        super().__init__()
        
    def _insert(self, node, key):
        if node is None:
            return AVLNode(key)
        elif key < node.val:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)
        if balance < -1 or balance > 1:
            return self.rebalance(balance, node, key)
        
        return node
    
    def rebalance(self, balance, node, key):
        if balance > 1 and key < node.left.val:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.val:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.val:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.val:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y
            
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        return y    

    def get_height(self, node):
        if not node:
            return 0
        return node.height  
        
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
avl_tree = AVLTree()
for el in nodes:
    avl_tree.insert(el)
print()
print(avl_tree.search(40))
print()
breadth_first_traversal(avl_tree.root)
print()
traversal(avl_tree.root)
print()
sim_traversal(avl_tree.root)
print()
reverse_traversal(avl_tree.root)