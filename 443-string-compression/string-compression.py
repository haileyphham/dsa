class Solution:
    def compress(self, chars: List[str]) -> int:
        # read pointer and write pointer
        n = len(chars)
        write = 0
        read = 0
        
        while read < n: #starting the pointers
            char = chars[read]
            count = 0
        
            while read < n and chars[read] == char:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1
        
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write