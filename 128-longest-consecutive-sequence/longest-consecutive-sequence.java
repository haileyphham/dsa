class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numCheck = new HashSet<>();
        
        for(int num : nums){
            numCheck.add(num);
        }
        int maxStreak = 0;
        for(int num : numCheck){
            if(!(numCheck.contains(num-1))){
                int currNum = num;
                int streak = 1;

                while(numCheck.contains(currNum+1)){
                    currNum += 1;
                    streak += 1;
                }
                maxStreak = Math.max(maxStreak, streak);
            }
        }
        return maxStreak;
    }

}

//unsorted int arr
//len of longest consecutive elements 

