class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Book inserted at beginning:", data)

    # Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print("Book inserted at end:", data)
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        print("Book inserted at end:", data)

    # Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Library catalog is empty")
            return

        data = self.head.data
        self.head = self.head.next
        print("Book deleted:", data)

    # Display
    def display(self):
        if self.head is None:
            print("Library catalog is empty")
            return

        temp = self.head

        print("Library Catalog:")

        while temp is not None:
            print(temp.data)
            temp = temp.next


l = LinkedList()

while True:
    print("\n--- Library Catalog ---")
    print("1. Insert Book at Beginning")
    print("2. Insert Book at End")
    print("3. Delete Book from Beginning")
    print("4. Display Books")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        book = input("Enter book title: ")
        l.insert_beginning(book)

    elif ch == 2:
        book = input("Enter book title: ")
        l.insert_end(book)

    elif ch == 3:
        l.delete_beginning()

    elif ch == 4:
        l.display()

    elif ch == 5:
        break

    else:
        print("Invalid choice!")