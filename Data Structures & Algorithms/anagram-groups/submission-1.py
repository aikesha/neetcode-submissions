class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = dict()
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in my_dict:
                my_dict[sorted_word] = []
            my_dict[sorted_word].append(word)
        
        group = []
        for key, values in my_dict.items():
            group.append(values)
        return group


        