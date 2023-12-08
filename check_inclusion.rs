use std::collections::HashMap;

fn check_inclusion(s1: String, s2: String) -> bool {
    let mut cntr = HashMap::new();
    let w = s1.len();
    let mut matched = 0;

    for ch in s1.chars() {
        *cntr.entry(ch).or_insert(0) += 1;
    }

    let chars: Vec<char> = s2.chars().collect();

    for i in 0..chars.len() {
        if let Some(count) = cntr.get_mut(&chars[i]) {
            *count -= 1;
            if *count == 0 {
                matched += 1;
            }
        }

        if i >= w {
            if let Some(count) = cntr.get_mut(&chars[i - w]) {
                if *count == 0 {
                    matched -= 1;
                }
                *count += 1;
            }
        }

        if matched == cntr.len() {
            return true;
        }
    }

    false
}

fn main() {
    let s1 = "ab";
    let s2 = "eidbaooo";
    println!("Result: {}", check_inclusion(s1.to_string(), s2.to_string()));
}
