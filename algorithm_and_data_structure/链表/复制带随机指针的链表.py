# Definition for a Node.
class Node:
    def __init__(self, x, next, random:):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return
        # 创建一个哈希表，key是原节点，value是新节点
        d = dict()
        cur = head
        # 将原节点和新节点放入哈希表中
        while cur:
            new_node = Node(cur.val, None, None)
            d[cur] = new_node
            cur = cur.next
        # 遍历原链表，设置新节点的next和random
        cur = head
        while cur:
            if cur.next:
                d[cur].next = d[cur.next]
            if cur.random:
                d[cur].random = d[cur.random]
            cur = cur.next
        return d[head]
