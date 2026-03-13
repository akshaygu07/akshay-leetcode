class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = {}
        
        # First pass: count frequencies
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Second pass: find the first character with a count of 1
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
                
        return -1
