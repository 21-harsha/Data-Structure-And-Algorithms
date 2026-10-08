# Library Book Return Management using Stack

class Stack:
    def __init__(self):
        self.top = -1
        self.ST = [0] * 5

    def push(self, x):
        if self.top == 4:
            print("Stack Overflow")
            return

        self.top = self.top + 1
        self.ST[self.top] = x

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return

        y = self.ST[self.top]
        self.top = self.top - 1
        return y

    def peek(self):
        if self.top == -1:
            print("Stack Underflow")
            return

        return self.ST[self.top]

    def display(self):
        if self.top == -1:
            print("Nothing to display...")
            return

        for i in range(self.top, -1, -1):
            print(self.ST[i])


s = Stack()

while True:
    print("\n1. Return Book")
    print("2. Process Returned Book")
    print("3. View Latest Returned Book")
    print("4. Display All Returned Books")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        book_id = int(input("Enter Book ID: "))
        s.push(book_id)

    elif ch == 2:
        book_id = s.pop()
        if book_id is not None:
            print("Processed Book ID:", book_id)

    elif ch == 3:
        book_id = s.peek()
        if book_id is not None:
            print("Latest Returned Book ID:", book_id)

    elif ch == 4:
        s.display()

    elif ch == 5:
        break

    else:
        print("Invalid choice...")