class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''my_dict = dict()
        for word in strs:
            sorted_word = "".join(sorted(word)) #O(k log k)
            if sorted_word not in my_dict:
                my_dict[sorted_word] = []
            my_dict[sorted_word].append(word)
        
        return list(my_dict.values())'''

        my_dict = dict()
        for word in strs:
            counts = [0] * 26
            for ch in word:
                counts[ord(ch) - ord('a')] += 1
            key = tuple(counts)
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(word)
        
        return list(my_dict.values())



        