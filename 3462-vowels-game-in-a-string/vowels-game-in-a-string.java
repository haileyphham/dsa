class Solution {
    public boolean doesAliceWin(String s) {
        int countVowels = 0;
        char[] stringArray = s.toCharArray();
        for(int i=0; i<stringArray.length; i++){
            if(stringArray[i] == 'a' || stringArray[i]  == 'e' || stringArray[i]  == 'i' || stringArray[i]  == 'o' || stringArray[i]  == 'u'){
                countVowels += 1;
            }
            if(countVowels >= 1){
                return true;
            }
        }
        return false;
        
    }
}


//removes nonempty substring from s that contins an odd/even number of vowels
//first player who cannot make a move loses
//true for alice, false for bob
//substring used twopointers/ sliding window
