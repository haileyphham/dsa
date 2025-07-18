class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> duplicates = new HashSet<>(); 
        int start = 0;
        int subLength = 0;

        for(int i=0; i< s.length(); i++){
            char current = s.charAt(i);

            while (duplicates.contains(current)) {
                duplicates.remove(s.charAt(start));
                start++;
            }
            duplicates.add(current);
            subLength = Math.max(subLength, i - start + 1);
        }
        return subLength;
    }
}
