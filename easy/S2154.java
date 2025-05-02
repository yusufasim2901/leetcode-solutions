import java.util.HashSet;
import java.util.Set;

class Solution {
    public int findFinalValue(int[] nums, int original) {
        Set<Integer> seen = new HashSet<>();
        for (int num : nums) {
            seen.add(num);
        }
        while (seen.contains(original)) {
            original *= 2;
        }
        return original;
    }
}
