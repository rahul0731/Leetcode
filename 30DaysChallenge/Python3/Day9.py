class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def convert(word):
            stack = []
            for c in word:
                if c ==  "#":
                    if len(stack)>0:
                        stack.pop()
                else:
                    stack.append(c)
            return "".join(stack)
        
        return convert(S) == convert(T)