class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''s = s.lower()
        new_s = ""
        for ch in s:
            if ch.isalnum():
                new_s += ch
        return new_s == new_s[::-1]'''  # O(n) time, O(n) space

        #Can we do it O(1) exytra space?
        #s = s.lower() --> make O(n) extra space
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1  # O(n) time, O(1) space
        return True
        

    