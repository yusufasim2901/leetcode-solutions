class Solution {
    static public int toplam(int num){
        int toplam = 0;
        while(num > 0){
            toplam += num % 10;
            num /= 10;
        }
        return toplam;
    } 
    public int addDigits(int num) {
        do{
            num = Solution.toplam(num);
        }while(num >= 10);
        return num;
    }
}