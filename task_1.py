class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def insertion_sort(self):
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self._sorted_insert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def _sorted_insert(self, head, node):
        if head is None or node.data < head.data:
            node.next = head
            head = node
        else:
            current = head
            while current.next and current.next.data < node.data:
                current = current.next
            node.next = current.next
            current.next = node
        return head

    @staticmethod
    def merge_sorted_lists(list1, list2):
        dummy = Node()
        tail = dummy

        l1 = list1.head
        l2 = list2.head

        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 if l1 else l2

        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list

def main():
    llist1 = LinkedList()
    llist1.insert_at_end(5)
    llist1.insert_at_end(1)
    llist1.insert_at_end(3)

    print("First list before sorting:")
    llist1.print_list()
    llist1.insertion_sort()
    print("First list after sorting:")
    llist1.print_list()

    llist2 = LinkedList()
    llist2.insert_at_end(8)
    llist2.insert_at_end(2)
    llist2.insert_at_end(4)

    print("Second list before sorting:")
    llist2.print_list()
    llist2.insertion_sort()
    print("Second list after sorting:")
    llist2.print_list()

    merged_list = LinkedList.merge_sorted_lists(llist1, llist2)
    print("Merged sorted list:")
    merged_list.print_list()

    merged_list.reverse()
    print("Reversed merged list:")
    merged_list.print_list()

if __name__ == "__main__":
    main()
