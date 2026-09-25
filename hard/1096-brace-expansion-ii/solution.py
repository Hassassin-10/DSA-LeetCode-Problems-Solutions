class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def union(a, b):
            return a | b

        def concat(a, b):
            return {x + y for x in a for y in b}

        def parse_expr(i):
            # expr := term (',' term)*
            res, i = parse_term(i)

            while i < n and expression[i] == ',':
                right, i = parse_term(i + 1)
                res = union(res, right)

            return res, i

        def parse_term(i):
            # term := factor factor*
            res = {""}

            while i < n and expression[i] not in "},":
                cur, i = parse_factor(i)
                res = concat(res, cur)

            return res, i

        def parse_factor(i):
            if expression[i] == '{':
                res, i = parse_expr(i + 1)
                return res, i + 1   # skip '}'

            # lowercase letter
            return {expression[i]}, i + 1

        result, _ = parse_expr(0)
        return sorted(result)
