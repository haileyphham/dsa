class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        for(int stone:stones){
            maxHeap.add(stone);
        }
        while(maxHeap.size()>1){
            int y = maxHeap.poll();
            int x = maxHeap.poll();
            if(x!=y){
                y = y-x;
                maxHeap.add(y);
            }
        }
        if(maxHeap.isEmpty()){
            return 0;
        }
        return maxHeap.peek();

    }
}

