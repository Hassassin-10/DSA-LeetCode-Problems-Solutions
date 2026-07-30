class Solution:
    def minimumPushes(self, word: str) -> int:
        cost = 0
        for i in range(len(word)):
            cost += (i//8)+1
        return cost