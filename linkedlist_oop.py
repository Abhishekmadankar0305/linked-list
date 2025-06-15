class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        try:
            if n <= 0:
                raise ValueError("Index should be 1 or greater.")

            if not self.head:
                raise IndexError("Cannot delete from an empty list.")

            if n == 1:
                print(f"Deleting node at position {n} with value {self.head.data}")
                self.head = self.head.next
                return

            current = self.head
            count = 1
            while current and count < n - 1:
                current = current.next
                count += 1

            if not current or not current.next:
                raise IndexError("Index out of range.")

            print(f"Deleting node at position {n} with value {current.next.data}")
            current.next = current.next.next

        except (ValueError, IndexError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    ll = LinkedList()
    for value in [10, 20, 30, 40, 50]:
        ll.add_node(value)

    print("Initial Linked List:")
    ll.print_list()

    ll.delete_nth_node(3)
    print("After deleting 3rd node:")
    ll.print_list()

    ll.delete_nth_node(10)
    ll.delete_nth_node(1)
    print("After deleting 1st node:")
    ll.print_list()

    empty_list = LinkedList()
    empty_list.delete_nth_node(1)
