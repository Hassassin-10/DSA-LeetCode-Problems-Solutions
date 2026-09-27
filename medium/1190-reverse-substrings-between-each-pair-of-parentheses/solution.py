class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        
        for ch in s:
            if ch == '(':
                stack.append("")
            elif ch == ')':
                curr = stack.pop()[::-1]
                stack[-1] += curr
            else:
                stack[-1] += ch
        
        return stack[0]
