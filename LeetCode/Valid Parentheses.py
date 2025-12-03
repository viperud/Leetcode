class Solution:
    def isValid(self, s: str) -> bool:
        oss = []
        for c in s:
            if c in '({[':
                oss.append(c)

            elif c in ')}]':
                if (not oss) or (c == ')' and oss[-1] != '(') or (c == '}' and oss[-1] != '{') or (c == ']' and oss[-1] != '['):
                    return False
                oss.pop()
        if oss:
            return False
        else:
            return True