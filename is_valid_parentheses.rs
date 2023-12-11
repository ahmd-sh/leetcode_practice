use std::collections::HashMap;

fn is_valid_parentheses(s: String) -> bool {
    let mut hm = HashMap::new();
    hm.insert(')', '(');
    hm.insert(']', '[');
    hm.insert('}', '{');

    if s.starts_with(|c| hm.contains_key(&c)) {
        return false;
    }

    let mut st = Vec::new();

    for c in s.chars() {
        match hm.get(&c) {
            Some(&expected) => {
                if st.last() == Some(&expected) {
                    st.pop();
                } else {
                    return false;
                }
            }
            None => st.push(c),
        }
    }

    st.is_empty()
}

fn main() {
    let s = String::from("()[]{}");
    println!("Result: {:?}", is_valid_parentheses(s));
}
