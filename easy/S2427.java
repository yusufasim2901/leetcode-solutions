class Solution {
    public int commonFactors(int a, int b) {
        int countour = 0;
        int c = Math.min(a, b);
        for (int i = 1; i <= c; i++) {
            if (a % i == 0 && b % i == 0) {
                countour++;
            }
        }
        return countour;
    }
}