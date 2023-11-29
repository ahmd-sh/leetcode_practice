// Here goes trying to learn Rust

fn valid_palindrome(s: &str) -> bool {
    let mut new_s = String::new();
    
    for c in s.chars() {
        if c.is_alphanumeric() {
            new_s.extend(c.to_lowercase())
        }
    }
    
    new_s == new_s.chars().rev().collect::<String>()
}

fn main() {
    let s = "race a car";
    println!("Is '{}' a palindrome? {}", s, valid_palindrome(s));
}