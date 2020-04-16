from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        
        @lru_cache(None)
        def isValid(index, depth):
            if index == N:
                if depth == 0:
                    return True
                else:
                    return False
            if depth < 0:
                return False
            
            if s[index] == '(':
                return isValid(index + 1, depth + 1)
            elif s[index] == ')':
                return isValid(index + 1 ,depth - 1)
            else:
                return isValid(index +1 ,depth +1) or isValid(index + 1 ,depth) or isValid(index + 1 ,depth - 1)
           
        return isValid(0,0)
