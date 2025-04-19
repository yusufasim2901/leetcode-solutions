class Solution {
    public int fib(int n) {
    if (n == 0){
        return 0;
    }   
    if (n == 1){
        return 1;
    }
    int x1 = 0;
    int temp = 0;
    int x2 = 1;
    int result = 0;
    int result_new =0;
    while(1 < n){
        result = x1 + x2;
        temp = x2;
        x2 = result;
        x1 = temp;
        n = n - 1;
    }
    
      return result;
   
   
 }
}