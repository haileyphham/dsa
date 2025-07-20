class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        int result = 0;
        for(String s : tokens){
            if(s.equals("+") || s.equals("-") || s.equals("*") || s.equals("/")){
                int second = stack.pop();
                int first = stack.pop();

                if(s.equals("+")){
                    result = first + second;
                }
                if(s.equals("-")){
                    result = first - second;
                }
                if(s.equals("*")){
                    result = first * second;
                }
                if(s.equals("/")){
                    result = first / second;
                }
                stack.push(result);
                
            }
            else{
                int num = Integer.parseInt(s);
                stack.push(num);
            }
        }
        return stack.pop();
    }
}


