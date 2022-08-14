

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ListNode(object):
    def __init__(self):
        self.head = None

    def __len__(self):
        """
        return length of the ListNode

        :return:    length of the ListNode
        """
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    def append(self, val):
        """
        append a value to ListNode
        ---
        if head == None: head = Node
        else tail.next = node
        ---

        :param val:     val of the Node
        """
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            pre = self.head
            while pre.next:
                pre = pre.next
            pre.next = node

    def get(self, index):
        """
        get the node of the given index

        :param index:   index of the node
        :return:        the node
        """
        index = index if index >= 0 else len(self) + index
        if len(self) < index or index < 0:
            return None
        pre = self.head
        while index:
            pre = pre.nex
            index -= 1
        return pre

    def isEmpty(self):
        if self.head.next is None:
            print("Empty List!")
            return 1
        else:
            return 0

    def print_list(self):
        if self.isEmpty():
            exit(0)
        list = []
        pre = self.head
        while pre:
            list.append(pre.val)
            pre = pre.next
        print("print_list:", list)


if __name__ == "__main__":
    node = ListNode()
    node.append(1)
    node.append(2)
    node.append(3)
    node.print_list()

