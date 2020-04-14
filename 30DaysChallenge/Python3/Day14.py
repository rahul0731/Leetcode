class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        offset = 0 
        N = len(s)
        #dirction = [-1 , 1]
        
        for direction, amount in shift:
            if direction == 0:
                offset += amount
            else:
                offset -= amount
                
        offset %= N
        return s[offset:] + s[:offset]
        
