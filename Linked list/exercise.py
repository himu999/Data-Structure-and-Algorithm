class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data1, data2):
        if self.head is None:
            raise Exception('Linked List is empty')

        itr = self.head

        while itr:
            if itr.data == data1:
                itr.next = Node(data2, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print(self):

        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        s = ""
        while itr:
            s += str(itr.data)+"-->"
            itr = itr.next
        print(s)


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
