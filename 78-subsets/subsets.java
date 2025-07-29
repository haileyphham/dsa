class Solution {
    List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> subsets(int[] nums) {
        backtrack(new ArrayList<>(), 0, nums);
        return result;
        
    }
    private void backtrack(List<Integer> path, int start, int[] nums) {
        result.add(new ArrayList<>(path)); 

        for (int i = start; i < nums.length; i++) {
            path.add(nums[i]);                    
            backtrack(path, i + 1, nums);         
            path.remove(path.size() - 1);        
        }
    }
}