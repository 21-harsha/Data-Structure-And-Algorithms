class Node:
    def __init__(self, book_id):
        self.data = book_id
        self.left = None
        self.right = None


def create():
    x = int(input("Enter Book ID (-1 for no book): "))

    if x == -1:
        return None

    root = Node(x)

    print("Enter left book of", x)
    root.left = create()

    print("Enter right book of", x)
    root.right = create()

    return root


def preorder(root):
    if root is not None:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


print("--- University Library Catalog ---")

root = create()

print("\nPreorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)