class Solution {
    public boolean isPalindrome(String s) {

        String cleanedString = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
        char[] charArray = cleanedString.toCharArray();
        int left = 0;
        int right = charArray.length - 1;
        while(left < right){
            if(charArray[left] == charArray[right]){
                left += 1;
                right -= 1;
            }
            else{
                return false;
            }
        }
        return true;
    }
}