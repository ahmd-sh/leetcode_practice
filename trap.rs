fn trap(height: Vec<i32>) -> i32 {
    let mut water = 0;
    let mut i: usize = 0;
    let mut j: usize = height.len() - 1;
    
    let mut left_max = height[i];
    let mut right_max = height[j];

    while i < j {
        if left_max < right_max {
            i += 1;
            left_max = std::cmp::max(left_max, height[i]);
            water += left_max - height[i];
        } else {
            j -= 1;
            right_max = std::cmp::max(right_max, height[j]);
            water += right_max - height[j];
        }
    }

    water
}

fn main() {
    let height = vec![0,1,0,2,1,0,1,3,2,1,2,1];
    let res = trap(height);

    println!("{}", res);
}
