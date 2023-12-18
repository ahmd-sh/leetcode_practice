fn car_fleet(target: i32, position: Vec<i32>, speed: Vec<i32>) -> i32 {
    let mut pair: Vec<(f64, f64)> = position
            .iter()
            .map(|x| *x as f64)
            .zip(speed.iter().map(|x| *x as f64))
            .collect();
    pair.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
    let mut stack = vec![];

    for (p, s) in pair.iter().rev() {
        stack.push((target as f64 - p) / s);
        if stack.len() >= 2 && stack.last() <= stack.get(stack.len() - 2) {
            stack.pop();
        }
    }
    stack.len() as i32
}

fn main() {
    let target = 12;
    let position = vec![10,8,0,5,3];
    let speed = vec![2,4,1,1,3];
    println!("{:?}", car_fleet(target, position, speed));
}
