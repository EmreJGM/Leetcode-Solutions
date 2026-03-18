class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""

        for i in range(len(strs[0])):
            letter = strs[0][i]

            for strr in strs[1:]:
                if i >= len(strr) or strr[i] != letter:
                    return prefix
            
            prefix += letter
        
        return prefix