# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head):
        cur = head
        tmp = []
        while cur:
            if cur.child:
                if cur.next:
                    tmp.append(cur.next)
                child = cur.child
                cur.next = child
                child.prev = cur
                cur.child = None
            if not cur.next and tmp:
                node = tmp.pop()
                cur.next = node
                node.prev = cur
            cur = cur.next
        return head
