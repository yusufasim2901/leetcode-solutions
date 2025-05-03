class Solution {
    public int sumOfTheDigitsOfHarshadNumber(int x) {
    int deger = x;
    int toplam = 0;
    while(x > 0)
    {
        toplam += x % 10;
         x /= 10;
    }
    if(deger % toplam == 0)
    {
        return toplam;
    }
    else
        return -1;
    
    }   
}