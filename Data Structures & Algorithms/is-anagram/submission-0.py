class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for a, b in zip(s, t):
            s_dict[a] = s_dict.get(a, 0) + 1
            t_dict[b] = t_dict.get(b, 0) + 1
        return s_dict == t_dict

        