class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        how many character are not the most frequent one in my window?
        right always moves forward
        left only moves forward when the window becomes invalid
        left pointer, right pointer, frequency map of chars in the window, 
        max_freq = highest frequency of any character in the window
        '''
        left = 0
        freq = {}
        max_freq = 0
        result = 0

        for right in range(len(s)):
            # expand window
            freq[s[right]] = freq.get(s[right], 0) + 1 #adding count to freq of char
            #key: char at right pointer
            #value: (the value for the key or default 0) + 1
            max_freq = max(max_freq, freq[s[right]]) #finding char of max_freq

            # shrink window if invalid
            while (right - left + 1) - max_freq > k: #if the current range(window) - the max_freq char is greater than k, it means that we have to many missing
                freq[s[left]] -= 1 #decreasing the freq for that char bc we gon delete it
                left += 1 #closing the window

            # update result
            result = max(result, right - left + 1) #largest window

        return result




            


        