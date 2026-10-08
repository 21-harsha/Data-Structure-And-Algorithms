class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.Q = [0] * 5

    def enqueue(self, x):
        if self.rear == 4:
            print("Queue Overflow")
            return

        if self.front == -1:
            self.front = 0

        self.rear = self.rear + 1
        self.Q[self.rear] = x

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return

        x = self.Q[self.front]
        self.front = self.front + 1

        return x

    def peek(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
            return

        return self.Q[self.front]

    def display(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue is empty")
            return

        for i in range(self.front, self.rear + 1):
            print(self.Q[i])


q = Queue()

while True:
    print("\n--- Ticket Booking Counter ---")
    print("1. Add Customer (Enqueue)")
    print("2. Serve Customer (Dequeue)")
    print("3. Next Customer (Peek)")
    print("4. Display Queue")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        ticket = int(input("Enter Customer/Ticket Number: "))
        q.enqueue(ticket)
        print("Customer added:", ticket)

    elif ch == 2:
        ticket = q.dequeue()
        if ticket is not None:
            print("Customer served:", ticket)

    elif ch == 3:
        ticket = q.peek()
        if ticket is not None:
            print("Next customer:", ticket)

    elif ch == 4:
        q.display()

    elif ch == 5:
        break

    else:
        print("Invalid choice!")