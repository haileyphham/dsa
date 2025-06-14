class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanMap = new HashMap<>();

        char[] symbol = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        int[] value = {1, 5, 10, 50, 100, 500, 1000};

        for(int i=0; i<symbol.length; i++){
            romanMap.put(symbol[i], value[i]);
        }

        int total = 0;

        for (int i = 0; i < s.length(); i++) {
            int currVal = romanMap.get(s.charAt(i));

            if (i < s.length() - 1 && currVal < romanMap.get(s.charAt(i + 1))) {
                total -= currVal; 
            } else {
                total += currVal; 
            }
        }

        return total;
    }
}


