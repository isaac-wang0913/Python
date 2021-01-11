# https://leetcode-cn.com/leetbook/read/linked-list/jsumh/
# 单链表：单链表中的每个结点不仅包含值，还包含链接到下一个结点的引用字段
# 索引的时间复杂度：O(n)
# 插入的时间复杂度：O(n)
# 删除的时间复杂度：O(n)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SingleLinkList:
    def __init__(self):
        self.size = 0
        # 哨兵节点被用作伪头始终存在，这样结构中永远不为空，它将至少包含一个伪头
        self.head = ListNode(0) # 哨兵节点

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1
        """
        if index < 0 or index >= self.size:  # index range(0, self.size):
            return -1
        cur = self.head
        for i in range(index+1):    # 因为哨兵节点的存在 index + 1
            cur = cur.next
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
        cur = self.head
        for i in range(index):
            cur = cur.next  # 到需插入index的前一个节点
        addnode = ListNode(val)
        addnode.next = cur.next # 必须保持这个顺序，否则后面的节点会丢失
        cur.next = addnode
        self.size += 1

    def deleteAtIndex(self, index):
        """
         Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.size:
            return
        cur = self.head
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1

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

if __name__ == '__main__':
    singlelinklist = SingleLinkList()
    singlelinklist.addAtIndex(0, 1)
    singlelinklist.addAtIndex(1, 2)
    singlelinklist.addAtIndex(2, 3)
    print(singlelinklist.get(0), singlelinklist.get(1), singlelinklist.get(2))
    singlelinklist.deleteAtIndex(1)
    print(singlelinklist.get(1))
