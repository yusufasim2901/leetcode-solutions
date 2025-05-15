class Solution {
    public int countDigits(int num) {
        int counter = 0;
        int orgnum = num;
        while(num > 0)
        {
            int digit = num % 10;
            if(orgnum % digit == 0)
                counter = counter + 1;
            num = num / 10;
        }

        return counter;
     }
}