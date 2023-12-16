fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
    let mut res = vec![0; temperatures.len()];
    let mut stack: Vec<usize> = Vec::new();
    
    for i in 0..temperatures.len() {
        while let Some(&last_idx) = stack.last() {
            if temperatures[last_idx] < temperatures[i] {
                res[last_idx] = i as i32 - last_idx as i32;
                stack.pop();
            } else {
                break;
            }
        }
        stack.push(i)
    }

    res
}

fn main() {
    let temperatures = vec![73,74,75,71,69,72,76,73];
    println!("{:?}", daily_temperatures(temperatures));
}
