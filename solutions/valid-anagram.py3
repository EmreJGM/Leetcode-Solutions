class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        seen_s = {}

        for ch_s in s:
            if ch_s in seen_s:
                seen_s[ch_s] += 1
            else:
                seen_s[ch_s] = 1

        for ch_t in t:
            if ch_t in seen_s:
                seen_s[ch_t] -= 1
            else:
                return False
    
        for val in seen_s.values():
            if val != 0:
                return False
        return True
