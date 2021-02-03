class Solution:
    def openLock(self, deadends, target):
        # 广度优先遍历BFS
        queue = ['0000']
        visited = set()
        visited.add('0000')
        count = 0
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                if cur in deadends:     # 如果cur是死亡数字，则不选这条路径
                    continue
                if cur == target:
                    return count
                for i in range(4):
                    up = self.up(cur, i)
                    if up not in visited:
                        queue.append(up)
                        visited.add(up)
                    down = self.down(cur, i)
                    if down not in  visited:
                        queue.append(down)
                        visited.add(down)
            count += 1
        return -1

    def up(self, s, i):
        s = list(s)
        if s[i] == '9':
            s[i] = '0'
        else:
            s[i] = str(int(s[i])+1)
        return ''.join(s)

    def down(self, s, i):
        s = list(s)
        if s[i] == '0':
            s[i] = '9'
        else:
            s[i] = str(int(s[i])-1)
        return ''.join(s)
