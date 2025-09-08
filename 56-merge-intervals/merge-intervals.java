class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> {
            return Integer.compare(a[0],b[0]);
        });
        List<int[]> merged = new ArrayList<>();

        int currStart = intervals[0][0];
        int currEnd = intervals[0][1];
        

        for(int i=0; i<intervals.length; i++){

            int nextStart = intervals[i][0];
            int nextEnd = intervals[i][1];

            if(nextStart <= currEnd){
                currEnd = Math.max(currEnd, nextEnd);
            }
            else{
                merged.add(new int[]{currStart, currEnd});

                currStart = nextStart;
                currEnd = nextEnd;

            }
        }
        merged.add(new int[]{currStart, currEnd});

        return merged.toArray(new int[merged.size()][]);
        
    }
}

/*
sorting
brute force: 

at the first interval, scan all other intervals and merge those that overlap, then repeat until notheing overlaps anymore

Arraylist -->*/
