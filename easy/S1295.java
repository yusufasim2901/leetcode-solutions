class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            int digits = 0;
            int x = nums[i];
            while (x != 0) {
                digits++;
                x /= 10;
            }
            if (digits % 2 == 0) {
                count++;
            }
        }
        return count;
    }
}