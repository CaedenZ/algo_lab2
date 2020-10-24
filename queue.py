class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = self.tail = None

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    # Method to add an item to the queue
    def EnQueue(self, val):
        newNode = ListNode(val)

        if self.tail is None:
            self.head = self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

        # Method to remove an item from queue

    def DeQueue(self):

        if self.isEmpty():
            return None
        temp = self.head
        self.head = temp.next

        if self.head is None:
            self.tail = None

        return temp.val
