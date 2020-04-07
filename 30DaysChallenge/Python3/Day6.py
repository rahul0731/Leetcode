class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h =collections.defaultdict(list)
        for s in strs:
            h["".join(sorted(s))].append(s)
        ans = []
        for key in h:
            ans.append(h[key])
            
        return ans
        