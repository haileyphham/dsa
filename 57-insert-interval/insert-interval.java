class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> mergedSchedule = new ArrayList<>();

        int i = 0; //scan through index
        int totalLength = intervals.length;

        int newStart = newInterval[0];
        int newEnd = newInterval[1];

        while(i<totalLength && intervals[i][1] < newStart){
        mergedSchedule.add(intervals[i]);
        i++;
        }

        while(i<totalLength && intervals[i][0] <= newEnd){
            newStart = Math.min(newStart, intervals[i][0]);
            newEnd = Math.max(newEnd, intervals[i][1]);
            i++;
        }

        mergedSchedule.add(new int[]{newStart, newEnd});

        while(i<totalLength){
            mergedSchedule.add(intervals[i]);
            i++;
        }
        return mergedSchedule.toArray(new int[mergedSchedule.size()][]);

        
    }
}

/* intervals sorted in **ascending** order
insert new interal into intervals, no overlapping but merge if nessesary
return intervals after insertion
we can make a new array and return it

brute force approach:
add the new interval to the list, sort them, and then do the merging algortism


*/