class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        String numString = Integer.toString(x);
        String reversedString= "";
        for ( int i=numString.length()-1; i>=0; i--){
            reversedString += numString.charAt(i);
        }
        return numString.equals(reversedString);
    }
}

