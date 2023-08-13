"""
Lista jednokierunkową z poprzedniej listy potrzebną do algorytmów BFS i DFS
"""
class ll_node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = ll_node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = ll_node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = ll_node(data, None)
    def remove_at_beginning(self):
        if self.head is None:
            raise Exception("List is empty")
        removed = self.head.data
        self.head = self.head.next
        return removed


    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = ll_node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_index(self, value):
        curr = self.head
        idx = 0
        while curr is not None:
            if curr.data == value:
                return idx
            curr = curr.next
            idx += 1
        raise ValueError('Value not found in list')
    def clear_list(self):
        self.head = None

"""
Kod drzewa binarnego
"""

class BinarySearchTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        if self.data is None:
            self.data = data

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def build_tree(self, elements):
        for i in range(0, len(elements)):
            self.add_child(elements[i])

    def BFS(self):
        bfs = []
        queue = LinkedList()
        queue.insert_at_end(self)
        while queue.head is not None:
            node = queue.remove_at_beginning()
            bfs.append(node.data)
            if node.left is not None:
                queue.insert_at_end(node.left)
            if node.right is not None:
                queue.insert_at_end(node.right)
        return bfs
    def DFS(self):
        if not self.data:
            return []
        res = []
        stack = []
        stack.append(self)
        while stack:
            node = stack.pop()
            res.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def make_new_tree(self, new_tree_root):
        new_tree = BinarySearchTreeNode(new_tree_root)
        current_node = self
        while current_node.data != new_tree.data:
            if current_node.data < new_tree.data:
                current_node = current_node.right
            elif current_node.data > new_tree.data:
                current_node = current_node.left
        new_tree.left = current_node.left
        new_tree.right = current_node.right
        return new_tree

    def print_tree(self, level = 0):
        if self.right:
            self.right.print_tree(level + 1)
        print(' ' * 4 * level + '->', self.data)
        if self.left:
            self.left.print_tree(level + 1)

    def find_leafs(self, d=0, min_depth=float('inf')):
        leaf_data_depth = []
        if self.left is None and self.right is None:
            if d < min_depth:
                leaf_data_depth = [(self.data, d)]
                min_depth = d
        if self.left:
            leaf_data_depth += self.left.find_leafs(d + 1, min_depth)
        if self.right:
            leaf_data_depth += self.right.find_leafs(d + 1, min_depth)
        return leaf_data_depth

    #ta funckja zwraca liste liści jako krotki, 1 element krotki to wartość liścia, a druga to odległość od korzenia
    def closest_leafs(self):
        leafs = self.find_leafs()
        min_depth = leafs[0][1]
        closest_leafs = []
        for x in leafs:
            if x[1] < min_depth:
                min_depth = x[1]
        for x in leafs:
            if x[1] == min_depth:
                closest_leafs.append(x)
        return closest_leafs


root = BinarySearchTreeNode()
root.build_tree([5, 3, 7, 1, 9, 2, 0, 6, 8, 11, 4])

bfs_list = root.BFS()
print("BFS traversal:", bfs_list)
root.print_tree()
dfs_list = root.DFS()
print("DFS traversal:", dfs_list)

leafs = root.closest_leafs()
l = root.find_leafs()
print(l)
print(leafs)





