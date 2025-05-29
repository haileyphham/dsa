
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> res = new HashMap<>();
        for(String s : strs){
            //convert the string into a character array
            char[] charArray = s.toCharArray();
            Arrays.sort(charArray); // sort the characters alphabetically
            String sorted = new String(charArray); //create a sorted string
            res.putIfAbsent(sorted, new ArrayList<>()); // if not in the hashmap, add with an empty array as the value
            res.get(sorted).add(s); // get the value associated with the sorted string and add the original string
        }
        return new ArrayList<>(res.values());//return array of all the hashmaps values
        
    }
}