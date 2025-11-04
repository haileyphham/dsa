class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        set_arr = set(arr)
        missing_numbers = []
        count = 1

        while len(missing_numbers) <= k:
            if count not in set_arr:
                missing_numbers.append(count)
            count += 1

        return missing_numbers[k-1]
            