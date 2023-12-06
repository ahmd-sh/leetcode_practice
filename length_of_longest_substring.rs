use std::collections::VecDeque;

fn length_of_longest_substring(s: String) -> i32 {
    let mut uniques: VecDeque<char> = VecDeque::new();
    let mut max_length = 0;

    for c in s.chars() {
        while uniques.contains(&c) {
            uniques.pop_front();
        }
        uniques.push_back(c);
        max_length = max_length.max(uniques.len());
    }

    max_length as i32
}

fn main() {
    let s = String::from("abcabcbb");
    let res = length_of_longest_substring(s);

    println!("{}", res);
}
