class Solution {
    public boolean checkPerfectNumber(int num) {
         if (num <= 1) {
            return false;
        }
        
        int sum = 1;  
        int limit = num / 2;
        for (int i = 2; i <= limit; i++) {
            if (num % i == 0) {
                sum += i;
            }
        }
        
        return sum == num;
    }
}