class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        in_stack = set() #removes duplicates

        for c in s:
            counter[c] -= 1 #subtracts how many times we've seen this char by 1
            if c in in_stack:
                continue
    
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                removed = stack.pop()
                in_stack.remove(removed)
    
            stack.append(c)
            in_stack.add(c)
        
        return "".join(stack)

#stack based greedy
#dictonary order (alphabetical ish)