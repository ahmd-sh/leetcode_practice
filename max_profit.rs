fn max_profit(prices: Vec<i32>) -> i32 {
    let mut prof = 0;
    let mut min_price = prices[0];

    for &p in &prices[1..] {
        if p < min_price {
            min_price = p;
        } else {
            prof = prof.max(p - min_price)
        }
    }
    prof
}

fn main() {
    let prices = vec![1,5,6,2,9];
    let res = max_profit(prices);

    println!("{}", res);
}
