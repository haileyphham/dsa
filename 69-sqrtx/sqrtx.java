class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;
        int left = 0;
        int right = x/2;
        int result = 0;

        while(left<=right){
            int middle = left + (right-left) / 2;
            long square = (long) middle * middle;

            if(square == x){
                return middle;
            }
            if(square < x){
                result = middle; 
                left = middle + 1;
            }
            if(square > x){
                right = middle - 1;
            }
        }
        return result;
    }
}

//sorted array from 0-x
//middle, see if middle*middle = x