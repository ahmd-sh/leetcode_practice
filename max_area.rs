fn max_area(height: Vec<i32>) -> i32 {
    let mut res = 0;
    let mut i = 0;
    let mut j = height.len() as i32 - 1;

    while i < j {
        let area = (j - i) * i32::min(height[i as usize], height[j as usize]);
        // OR do area calculation in the max fn below
        // for better memory but worse runtime
        res = i32::max(res, area);

        if height[i as usize] < height[j as usize] {
            i += 1;
        } else {
            j -= 1;
        }
    }

    res
}

fn main() {
    let height = vec![1,8,6,2,5,4,8,3,7];
    let res = max_area(height);

    println!("{}", res);
}