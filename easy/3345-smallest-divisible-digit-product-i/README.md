# Smallest Divisible Digit Product I

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

 
Example 1:


Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.


Example 2:


Input: n = 15, t = 3

Output: 16

Explanation:

The digit product of 16 is 6, which is divisible by 3, making it the smallest number greater than or equal to 15 that satisfies the condition.


 
Constraints:


	1 <= n <= 100
	1 <= t <= 10

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.2 MB  
**Submitted:** 2026-08-06T16:23:33.099Z  

```py
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x):
            prod = 1
            while x > 0:
                prod *= x % 10
                x //= 10
            return prod

        while True:
            if digit_product(n) % t == 0:
                return n
            n += 1

```

---

[View on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-i/)