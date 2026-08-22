class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n = 99
        org = n
        sum = 0
        product = 1
        while(n>0):
            digit = n%10
            sum += digit
            product *= digit
            n //= 10
        return org % (sum + product) == 0
