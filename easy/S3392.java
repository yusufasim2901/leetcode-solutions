class Solution {
    public int countSubarrays(int[] nums) {
        int counter = 0;
        for (int i = 0; i <= nums.length - 3; i++) {
            int a = nums[i];
            int b = nums[i + 2];
            double c = nums[i + 1] / 2.0;
            if (a + b == c) {
                counter++;
            }
        }
        return counter;
    }
}