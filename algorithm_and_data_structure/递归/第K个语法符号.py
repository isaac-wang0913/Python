class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 0:
            return 0
        if K % 2:
            return self.kthGrammar(N-1, (K+1) / 2)
        else:
            return abs(self.kthGrammar(N-1, K / 2) - 1)
