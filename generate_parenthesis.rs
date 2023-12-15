fn generate_parenthesis(n: i32) -> Vec<String> {
    let mut res: Vec<String> = vec![];

    fn bt(res: &mut Vec<String>, s: String, open: i32, closed: i32) {
        if open == 0 && closed == 0 {
            res.push(s);
            return;
        }
        if open == closed {
            bt(res, s.clone() + "(", open - 1, closed);
        } else {
            if open > 0 {
                bt(res, s.clone() + "(", open - 1, closed);
            }
            if closed > 0 {
                bt(res, s.clone() + ")", open, closed - 1);
            }
        }
        
    }
    
    bt(&mut res, String::from(""), n, n);
    res
}

fn main() {
    let n = 3;
    println!("{:?}", generate_parenthesis(n));
}
