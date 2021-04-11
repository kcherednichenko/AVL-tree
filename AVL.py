class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


root = None


def height(node):
    if node is None:
        return 0
    else:
        return node.height


class AVL:
    def __init__(self):
        self.node = None

    def right_rotation(self, y):
        x = y.left
        t = x.right
        x.right = y
        y.left = t
        y.height = max(height(y.left), height(y.right)) + 1
        x.height = max(height(x.left), height(x.right)) + 1
        return x

    def left_rotation(self, x):
        y = x.right
        t = y.left
        y.left = x
        x.right = t
        x.height = max(height(x.left), height(x.right)) + 1
        y.height = max(height(y.left), height(y.right)) + 1
        return y

    def get_balance(self, node):
        if node is None:
            return 0
        return height(node.left) - height(node.right)

    def insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        else:
            return node
        node.height = 1 + max(height(node.left), height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and key < node.left.key:
            return self.right_rotation(node)
        if balance < -1 and key > node.right.key:
            return self.left_rotation(node)
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)
        return node

    def min_(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self.delete(node.left, key)
        elif key > node.key:
            node.right = self.delete(node.right, key)
        else:
            if (node.left is None) or (node.right is None):
                temp = node.left if node.left else node.right
                if temp is None:
                    temp = node
                    node = None
                else:
                    node = temp
            else:
                temp = self.min_(node.right)
                node.key = temp.key
                node.right = self.delete(node.right, temp.key)
        if node is None:
            return node
        node.height = 1 + max(height(node.left), height(node.right))
        balance = self.get_balance(node)
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotation(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotation(node.left)
            return self.right_rotation(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotation(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotation(node.right)
            return self.left_rotation(node)
        return node

    def exists(self, node, x):
        if node is None:
            return False
        if node.key == x:
            return True
        if x < node.key:
            return self.exists(node.left, x)
        else:
            return self.exists(node.right, x)

    def next(self, x, root):
        last = None
        cur = root
        while cur is not None:
            if x >= cur.key:
                cur = cur.right
            elif x < cur.key:
                last = cur
                cur = cur.left
        return last

    def prev(self, x, root):
        last = None
        cur = root
        while cur is not None:
            if x > cur.key:
                last = cur
                cur = cur.right
            elif x <= cur.key:
                cur = cur.left
        return last

    def is_AVLTree(self, node):
        if node is None:
            return True
        left_height = height(node.left)
        right_height = height(node.right)

        if abs(left_height - right_height) <= 1 and self.is_AVLTree(node.left) and self.is_AVLTree(node.right):
            return True

        return False


if __name__ == "__main__":
    a = AVL()
    operations_amount = int(input())
    for i in range(operations_amount):
        s, x = [j for j in input().split()]
        x = int(x)
        if s == "insert":
            root = a.insert(root, x)
        elif s == "delete":
            root = a.delete(root, x)
        elif s == "exists":
            if a.exists(root, x):
                print("true")
            else:
                print("false")
        elif s == "next":
            ans = a.next(x, root)
            if ans is None:
                print("none")
            else:
                print(ans.key)
        elif s == "prev":
            ans = a.prev(x, root)
            if ans is None:
                print("none")
            else:
                print(ans.key)
