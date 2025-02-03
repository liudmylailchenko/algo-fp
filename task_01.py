class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(f"{self.data}, {self.next}")


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Previous node is not in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def split(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next

        second = slow.next
        slow.next = None
        return second

    def merge(self, first, second):
        if not first:
            return second
        if not second:
            return first

        if first.data < second.data:
            first.next = self.merge(self, first.next, second)
            return first
        else:
            second.next = self.merge(self, first, second.next)
            return second

    def merge_sort(self):
        if not self.head or not self.head.next:
            return head

        second = self.split(head)

        head = self.merge_sort(head)
        second = self.merge_sort(second)

        return self.merge(self, head, second)
