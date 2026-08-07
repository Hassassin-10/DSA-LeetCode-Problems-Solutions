# Smallest Divisible Digit Product II

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

 
Example 1:


Input: num = "1234", t = 256

Output: "1488"

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.


Example 2:


Input: num = "12355", t = 50

Output: "12355"

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.


Example 3:


Input: num = "11111", t = 26

Output: "-1"

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.


 
Constraints:


	2 <= num.length <= 2 * 105
	num consists only of digits in the range ['0', '9'].
	num does not contain leading zeros.
	1 <= t <= 1014

## Solution

**Language:** Python  
**Runtime:** 0 ms  
**Memory:** 19.6 MB  
**Submitted:** 2026-08-07T13:19:07.647Z  

```py
            rem[i + 1] = rem[i] // math.gcd(rem[i], int(num_list[i]))
                break
                pos = i
            if num_list[i] == "0":
        num_list = list(num)
        for i in range(n):

        pos = n - 1
        rem[0] = t
        rem = [0] * (n + 1)

        n = len(num)
            return "-1"
        if temp > 1:

                temp //= i
            while temp % i == 0:
        for i in range(2, 10):
        temp = t
    def smallestNumber(self, num: str, t: int) -> str:
class Solution:

```

---

[View on LeetCode](https://leetcode.com/problems/smallest-divisible-digit-product-ii/)