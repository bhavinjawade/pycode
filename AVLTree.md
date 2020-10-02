# AVL-Tree
Most of the BST operations (e.g., search, max, min, insert, delete.. etc) take O(h) time where h is the height of the BST. The cost of these operations may become O(n) for a skewed Binary tree. If we make sure that height of the tree remains O(Logn) after every insertion and deletion, then we can guarantee an upper bound of O(Logn) for all these operations. The height of an AVL tree is always O(Logn) where n is the number of nodes in the tree
The main functions which this data structure can perform are :
1. insertion()
2. deletion()

# Properties of an AVL Tree
1. Maximum possible number of nodes in AVL tree of height H = 2H+1 – 1
2. Minimum number of nodes in AVL Tree of height H is given by a recursive relation-N(H) = N(H-1) + N(H-2) + 1
3. Minimum possible height of AVL Tree using N nodes = ⌊log2N⌋
4. Maximum height of AVL Tree using N nodes is calculated using recursive relation-N(H) = N(H-1) + N(H-2) + 1

## Explanation / Working
1. insertion():
    For insertion these are the steps which have to be followed while inserting a node in the AVL Tree:
Let the newly inserted node be w
- Perform standard BST insert for w.
- Starting from w, travel up and find the first unbalanced node. Let z be the first unbalanced node, y be the child of z that comes on the path from w to z and x be the grandchild of z that comes on the path from w to z.
- Re-balance the tree by performing appropriate rotations on the subtree rooted with z. There can be 4 possible cases that needs to be handled as x, y and z can be arranged in 4 ways. Following are the possible 4 arrangements:
    - y is left child of z and x is left child of y (Left Left Case)
    - y is left child of z and x is right child of y (Left Right Case)
    - y is right child of z and x is right child of y (Right Right Case)
    - y is right child of z and x is left child of y (Right Left Case)


Here is the code snippet for the insertion

```sh
def insert(self, root, key): 		 
		if not root: 
			return TreeNode(key) 
		elif key < root.val: 
			root.left = self.insert(root.left, key) 
		else: 
			root.right = self.insert(root.right, key) 

		# updating the height of our tree
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 

		# finding the balance factor 
		balance = self.getBalance(root) 

		# Checking if the node is unbalanced
		# Case 1 - Left Left 
		if balance > 1 and key < root.left.val: 
			return self.rightRotate(root) 

		# Case 2 - Right Right 
		if balance < -1 and key > root.right.val: 
			return self.leftRotate(root) 

		# Case 3 - Left Right 
		if balance > 1 and key > root.left.val: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and key < root.right.val: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 
    
```

2. deletion():
    Let w be the node to be deleted
- Perform standard BST delete for w.
- Starting from w, travel up and find the first unbalanced node. Let z be the first unbalanced node, y be the larger height child of z, and x be the larger height child of y. Note that the definitions of x and y are different from insertion here.
- Re-balance the tree by performing appropriate rotations on the subtree rooted with z. There can be 4 possible cases that needs to be handled as x, y and z can be arranged in 4 ways. Following are the possible 4 arrangements:
    - y is left child of z and x is left child of y (Left Left Case)
    - y is left child of z and x is right child of y (Left Right Case)
    - y is right child of z and x is right child of y (Right Right Case)
    - y is right child of z and x is left child of y (Right Left Case)

Here is the code snippet for the deletion part

```sh
def delete(self, root, key): 
		if not root: 
			return root 
		elif key < root.val: 
			root.left = self.delete(root.left, key) 
		elif key > root.val: 
			root.right = self.delete(root.right, key) 
		else: 
			if root.left is None: 
				temp = root.right 
				root = None
				return temp 
			elif root.right is None: 
				temp = root.left 
				root = None
				return temp 
			temp = self.getMinValueNode(root.right) 
			root.val = temp.val 
			root.right = self.delete(root.right, temp.val) 
		if root is None: 
			return root 

		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) 

		balance = self.getBalance(root) 

		# Step 4 - If the node is unbalanced, 
		# then try out the 4 cases 
		# Case 1 - Left Left 
		if balance > 1 and self.getBalance(root.left) >= 0: 
			return self.rightRotate(root) 

		# Case 2 - Right Right 
		if balance < -1 and self.getBalance(root.right) <= 0: 
			return self.leftRotate(root) 

		# Case 3 - Left Right 
		if balance > 1 and self.getBalance(root.left) < 0: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and self.getBalance(root.right) > 0: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

    
```

# Time Complexities:
1.	Search	O(logn,base=2)
2.	Insert  O(logn,base=2)
3.	Delete	O(logn,base=2)

# Applications:
AVL trees are used for frequent insertion. One of the examples I know of is it is used in Memory management subsystem of linux kernel to search memory regions of processes during preemption.
