class Solution:
    def isHappy(self, n: int) -> bool:
        def f(x):
            s = 0
            while x > 0:
                s += (x % 10)** 2
                x //= 10
            return s
        
        seen = set()
        while n > 1 and n not in seen:
            seen.add(n)
            n = f(n)
        return n == 1 