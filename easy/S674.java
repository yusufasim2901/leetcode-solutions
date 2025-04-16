class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int biggest = 0;
        int counter = 0;
        for(int i = 0 ; i < nums.length ; i++)
        {
            counter = 0;
            while(i < nums.length - 1 && nums[i] < nums[i + 1] )
            {
                i = i + 1;
                counter = counter + 1;
            }
            if(counter > biggest)
            {
                biggest = counter;
            }
        } return biggest + 1;
    } 
}