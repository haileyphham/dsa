class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        answer[0] = 1;

        //forward pass
        for(int i=1; i < nums.length; i++){
            answer[i] = nums[i-1] * answer[i-1];
        }

        int rightProd = 1;
        //backward pass
        for(int i= nums.length-1 ; i >=0 ; i--){
            answer[i] *= rightProd;
            rightProd *= nums[i];
        }
        return answer;

    }
}

//multiply all products to the left of the index (1 if nothing to the left) store in answer array
//iterate backwards and multiply the num to the right with the answer array. update right product