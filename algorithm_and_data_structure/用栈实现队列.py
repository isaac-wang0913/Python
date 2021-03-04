class MyQueue:
    # 两个栈来回倒腾
    # 时间复杂度：push、empty：O(1)；pop、peek：O(n)
    # 空间复杂度：empty：O(1)；push、pop、peek：O(n)
    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.stack1 = []
    #     self.stack2 = []
    #
    # def push(self, x: int) -> None:
    #     """
    #     Push element x to the back of queue.
    #     """
    #     self.stack1.append(x)
    #
    # def pop(self) -> int:
    #     """
    #     Removes the element from in front of queue and returns that element.
    #     """
    #     while self.stack1:
    #         self.stack2.append(self.stack1.pop())
    #     res = self.stack2.pop()
    #     while self.stack2:
    #         self.stack1.append(self.stack2.pop())
    #     return res
    #
    # def peek(self) -> int:
    #     """
    #     Get the front element.
    #     """
    #     while self.stack1:
    #         self.stack2.append(self.stack1.pop())
    #     res = self.stack2[-1]
    #     while self.stack2:
    #         self.stack1.append(self.stack2.pop())
    #     return res
    #
    # def empty(self) -> bool:
    #     """
    #     Returns whether the queue is empty.
    #     """
    #     if not self.stack1:
    #         return True
    #     return False

    # 时间复杂度：均为O(1)
    # 空间复杂度：push为O(n)，其他为O(1)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack1:
            self.front = x
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            self.front = None
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.stack2:
            return self.stack2[-1]
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack1 and not self.stack2:
            return True
        return False
