import java.lang.Math; 
class Solution {
    public boolean isThree(int n){
        
        double x = Math.sqrt(n);
        int a = (int)x;
        int counter = 0;
        if(!(x==Math.ceil(x) && x==Math.round(x))){
            return false;

        }
         
         for(int i = a; i > 0 ; i--)
        {
            if(a % i == 0){
                counter = counter + 1;
            }
        } 
        if(counter == 2)
            return true;
        
        else
            return false;
    }  
}