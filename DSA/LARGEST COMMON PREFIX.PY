class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        smallest = min(strs)
        largest = max(strs)
        for i in range(len(smallest)):
            if smallest[i] != largest[i]:
               return smallest[:i]
        return smallest
