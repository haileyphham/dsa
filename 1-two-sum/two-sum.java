class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> Sums = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (Sums.containsKey(complement)) {
                return new int[]{Sums.get(complement), i};
            }
            Sums.put(nums[i], i);
        }
        return new int[]{};
            
    }
}