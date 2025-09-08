class Solution {
    public boolean isValidSudoku(char[][] board) {

        HashSet<Character>[] rows = new HashSet[9];
        HashSet<Character>[] cols = new HashSet[9];
        HashSet<Character>[] boxes = new HashSet[9];

        for(int i = 0; i<9; i++){
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            boxes[i] = new HashSet<>();
        }

        for(int r = 0; r<9; r++){
            for(int c = 0; c<9; c++){
                char current = board[r][c];

                if(current == '.'){
                    continue;
                }
                int b = (r/3)*3+(c/3);

                if(rows[r].contains(current)||cols[c].contains(current)||boxes[b].contains(current)){
                    return false;
                }

                rows[r].add(current);
                cols[c].add(current);
                boxes[b].add(current);
                
            }
        }
        return true;
    }
}


/*Notes:
each row cannot resuse 1-9
each coulum cannot reuse 1-9
each 3X3 box cannot reuse 1-9

naive:
for each cell, we rescan each row, column and 3x3 to see if it shows up in any of these spaces.
if . skip 

nXn board O(n^2 * n) 9^3

optimal:
HashSet--> check if seen : row, column, 3X3

(one run through)

if . skip,

for each filled cell, if the ro is already true, than that means weve seen if before and then we will duplicate and return false.
else: we set it to true and continue on

time o(n^2)


*/