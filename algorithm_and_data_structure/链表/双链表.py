# https://leetcode-cn.com/leetbook/read/linked-list/jy291/
# 时间复杂度：
# addAtHead，addAtTail:O(1)
# get，addAtIndex，delete:O(min(k,n−k))，其中k指的是元素的索引
# 空间复杂度：所有的操作都是O(1)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next= None
        self.pre = None

class DoubleLinkList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)     # 哨兵节点
        self.tail = ListNode(0)     # 哨兵节点
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1
        """
        # choose the fastest way: to move from the head
        # or to move from the tail
        if index < 0 or index >= self.size:
            return -1
        if index < self.size - index:
            cur = self.head
            for i in range(index+1):    # 因为哨兵节点的存在 index + 1
                cur = cur.next
        else:
            cur = self.tail
            for i in range(self.size-index):
                cur = cur.pre
        return cur.val


    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index < self.size - index:
            pred = self.head
            for i in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for j in range(self.size-index):
                succ = succ.pre
            pred = succ.pre
        # insert
        addnode = ListNode(val)
        addnode.pre = pred
        addnode.next = succ
        pred.next = addnode
        succ.pre = addnode
        self.size += 1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion,
        the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list
        """
        self.addAtIndex(self.size, val)

    def deleteAtIndex(self, index):
        """
         Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        if index < self.size - index:
            pred = self.head
            for i in range(index):
                pred = pred.next
            succ = pred.next.next

        else:
            succ = self.tail
            for j in range(self.size-index):
                succ = succ.pre
            pred = succ.pre.pre
        pred.next = succ
        succ.pre = pred
        self.size -= 1

if __name__ == '__main__':
    doublelinklist = DoubleLinkList()
    doublelinklist.addAtIndex(0, 0)
    doublelinklist.addAtIndex(1, 1)
    doublelinklist.addAtIndex(2, 2)
    print(doublelinklist.get(0), doublelinklist.get(1), doublelinklist.get(2))
    doublelinklist.deleteAtIndex(1)
    print(doublelinklist.get(1))
    doublelinklist.addAtHead(4)
    print(doublelinklist.get(0))
    doublelinklist.addAtTail(5)
    print(doublelinklist.get(3))
