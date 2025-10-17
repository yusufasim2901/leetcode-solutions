int sumOfMultiples(int n) {
    bool isDividing[n + 1];

    for(int i = 0 ; i <= n ; i++) isDividing[i] = false;

    int range[] = {3,5,7};
    for(int i = 0 ; i < 3 ; i++){
        int curr = range[i];
        for(int j = curr ; j <= n ; j += curr){
            isDividing[j] = true;
        }
    }
    int total = 0;
    for(int i = 1; i <= n ; i++){
        if(isDividing[i]) total += i;
    }

    return total;
}
