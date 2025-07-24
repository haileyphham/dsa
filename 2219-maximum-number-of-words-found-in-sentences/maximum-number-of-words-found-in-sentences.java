class Solution {
    public int mostWordsFound(String[] sentences) {
        int maxWordCount = 0;
        
        for(int i=0; i<sentences.length; i++){
            int wordCount = 1;
            String myString = sentences[i];
            char[] charArray = myString.toCharArray();
            for(int j=0; j<charArray.length; j++){
                if(charArray[j] == ' '){
                    wordCount += 1;
                }

            }
            if(wordCount>maxWordCount){
                maxWordCount = wordCount;
            }
        }
        return maxWordCount;
        
    }
}