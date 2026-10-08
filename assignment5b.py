class Node:
    def __init__(self, admission_id):
        self.data = admission_id
        self.left = None
        self.right = None


class Stack:
    def __init__(self):
        self.TOP = -1
        self.st = [0] * 100

    def push(self, x):
        if self.TOP == 99:
            print("Stack Overflow")
            return

        self.TOP += 1
        self.st[self.TOP] = x

    def pop(self):
        if self.TOP == -1:
            print("Stack Underflow")
            return None

        x = self.st[self.TOP]
        self.TOP -= 1
        return x


def insert(root, admission_id):
    new_node = Node(admission_id)

    if root is None:
        return new_node

    temp = root

    while True:
        if admission_id < temp.data:
            if temp.left is None:
                temp.left = new_node
                break
            temp = temp.left

        else:
            if temp.right is None:
                temp.right = new_node
                break
            temp = temp.right

    return root


def inorder(root):
    s = Stack()

    while root is not None or s.TOP != -1:

        while root is not None:
            s.push(root)
            root = root.left

        root = s.pop()
        print(root.data, end=" ")
        root = root.right


def preorder(root):
    s = Stack()

    while root is not None or s.TOP != -1:

        while root is not None:
            print(root.data, end=" ")
            s.push(root)
            root = root.left

        root = s.pop()
        root = root.right


root = None

n = int(input("Enter number of students: "))

for i in range(n):
    admission_id = int(input("Enter Admission ID: "))
    root = insert(root, admission_id)

print("\nStudent Admission Records - Inorder:")
inorder(root)

print("\nStudent Admission Records - Preorder:")
preorder(root)