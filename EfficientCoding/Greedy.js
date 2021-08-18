function coin_change(amount,coins){
    console.log("Amount to be given ",amount);
    coin_chosen=0;
    console.log(coins)
    if(coins.includes(amount)){
        return amount;
    }
    for(let i=0;i<coins.length;i++){
        if(coins[i]<amount){
            coin_chosen=coins[i]
        }
        else{
            break;
        }
    }
    console.log("Coin chosen ",coin_chosen);
    remaining_change=amount-coin_chosen;
    console.log("Amount remaning ",remaining_change);
    return ""+coin_chosen+","+coin_change(remaining_change,coins);
}
data=coin_change(8,[1,3,5,6]).split(",");
data.forEach(coin=>console.log(coin));
