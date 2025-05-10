class Solution {
    public String winningPlayer(int x, int y) {
        int count = 0;
        while(x >= 1 && y >= 4)
        {
            count = count + 1;
            x = x - 1;
            y = y - 4;
        }
        return count % 2 == 0? "Bob" : "Alice";
    
    }


}