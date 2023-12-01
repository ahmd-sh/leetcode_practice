fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
    let mut i = 0;
    let mut j = numbers.len() as i32 - 1;

    while i < j {
        let current_sum = numbers[i as usize] + numbers[j as usize];
        if current_sum == target {
            return vec![i+1, j+1];
        } else if current_sum > target {
            j -= 1;
        } else {
            i += 1;
        }
    }
    vec![]
}

fn main() {
    let numbers = vec![2, 7, 11, 15];
    let target = 9;
    let result = two_sum(numbers, target);

    if result.is_empty() {
        println!("No two sum solution");
    } else {
        println!("[{}, {}]", result[0], result[1]);
    }
}