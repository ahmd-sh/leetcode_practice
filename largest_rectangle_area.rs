fn largest_rectangle_area(mut heights: Vec<i32>) -> i32 {
    let mut max_area: i32 = 0;
    let mut stack: Vec<usize> = Vec::new();

    // handle edge case
    heights.push(0);
    heights.insert(0, 0);

    for (i, h) in heights.iter().enumerate() {
        while !stack.is_empty() && heights[*stack.iter().last().unwrap()] > *h {
            let j = stack.pop().unwrap();
            let width = (i - stack[stack.len() - 1] - 1) as i32;
            let size = width * heights[j];
            max_area = max_area.max(size);
        }
        stack.push(i);
    }
    max_area
}

fn main() {
    let target = 12;
    let position = vec![10,8,0,5,3];
    let speed = vec![2,4,1,1,3];
    println!("{:?}", car_fleet(target, position, speed));
}
