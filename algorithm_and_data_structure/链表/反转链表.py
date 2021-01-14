        # 双指针
        # 时间复杂度：O(n)
        # 空间复杂度：O(1)
        cur = head
        pre = None
        while cur:
            tmp = cur.next  # 暂存cur后节点
            cur.next = pre  # 修改next指向
            pre = cur       # 访问下一节点
            cur = tmp       # 访问下一节点
        return pre

        # 递归
