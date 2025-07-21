class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;

        int left = 0;
        int right = m * n - 1; //how many elements in the matrix

        while(left <= right){
            int middle = left + (right-left) / 2;

            int row = middle / n; //gives us row index
            int col = middle % n; //gives us col index
            int midVal = matrix[row][col];

            if(midVal == target){
                return true;
            }
            if(midVal < target){
                left = middle + 1;
            }
            if(midVal > target){
                right = middle - 1;
            }
        }

        return false;
    }
}