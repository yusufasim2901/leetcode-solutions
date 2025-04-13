class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0)
            return false;
        if(x < 10)
            return true;
        if(x == 0)  
            return true;
        String b = Integer.toString(x);
         int left =0;
         int right =b.length() - 1;
         
        while(right > left)
        {
            if (b.charAt(left) != b.charAt(right))
                 return false;
            left = left + 1;
            right = right - 1;
            
           
        }
        return true;    
    }
}