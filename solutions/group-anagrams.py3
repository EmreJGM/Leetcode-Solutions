class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupings = {}

        for strr in strs:
            freq = [0] * 26
            for char in strr:
                freq[ord(char) - ord("a")] += 1
            key = tuple(freq)

            if key in groupings:
                groupings[key].append(strr)
            else:
                groupings[key] = [strr]       
        return list(groupings.values())