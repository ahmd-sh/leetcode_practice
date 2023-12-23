use std::cmp::Ordering::{Equal, Less, Greater};

fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
    let max_piles = *piles.iter().max().unwrap() as usize;
    let (mut l, mut r, mut k) = (1, max_piles, max_piles);

    while l <= r {
        let m = l + (r - l) / 2;
        let hours: usize = piles.iter()
            .map(|&num_bananas| ((num_bananas - 1) as usize / m) + 1)
            .sum();
        
        match hours.cmp(&(h as usize)) {
            Less | Equal => {
                k = k.min(m);
                r = m - 1;
            },
            Greater => l = m + 1, 
        }
    }
    k as i32
}

fn main() {
    let piles: Vec<i32> = vec![3,6,7,11];
    let h = 8;
    println!("{:?}", min_eating_speed(piles, h));
}
