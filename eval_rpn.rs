use std::collections::HashMap;

fn eval_rpn(tokens: Vec<String>) -> i32 {
    let mut ops: HashMap<&str, fn(i32, i32) -> i32> = HashMap::new();
    ops.insert("+", |a, b| a + b);
    ops.insert("-", |a, b| a - b);
    ops.insert("*", |a, b| a * b);
    ops.insert("/", |a, b| a / b);

    let mut stack: Vec<i32> = Vec::new();

    for token in tokens {
        match ops.get(token.as_str()) {
            Some(&op) => {
                let a = stack.pop().expect("Invalid RPN expression");
                let b = stack.pop().expect("Invalid RPN expression");
                stack.push(op(b, a));
            },
            None => stack.push(token.parse::<i32>().expect("Invalid token")),
        }
    }

    *stack.last().expect("Invalid RPN expression")
}

fn main() {
    let tokens = vec![
        "2".to_string(),
        "1".to_string(),
        "+".to_string(),
        "3".to_string(),
        "*".to_string(),
    ];
    println!("Result: {}", eval_rpn(tokens));
}
