class Solution {
    public int climbStairs(int n) {
        if (n < 0) return 0;
        if (n == 0 || n == 1) return 1;

        int a2 = 1;
        int a1 = 1;
        int sonuc = 0;

        for (int i = 2; i <= n; i++) {
            sonuc = a1 + a2; 
            a2 = a1;
            a1 = sonuc;
        }

        return sonuc; 
        






    }
}