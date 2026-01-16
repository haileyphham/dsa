class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        create a monotonic stack, while the temps are less than the previous,
        we can add its *index* onto the stack. while we reach a temp that is
        greater than the last, we can pop an elem from the stack and 
        current_index - stack_index = how many days until it gets warm

        '''

        answer = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)

        return answer


        




        