import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>(nums.length);
        for (int i = 0; i < nums.length; i++) {
            if (seen.contains(nums[i])) {
               
                return true;
            }
            
            seen.add(nums[i]);
        }
        
        return false;
    }
}
