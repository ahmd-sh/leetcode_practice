use std::collections::HashMap;

fn min_window(s: String, t: String) -> String {
    let s: Vec<char> = s.chars().collect();

    if t == String::new() || s.len() < t.len() {
        return String::new();
    }

    let (mut l, mut res, mut res_len) = (0, (-1 as i32, -1 as i32), usize::MAX);
    let mut cntr_t: HashMap<char, u64> = HashMap::new();
    let mut wndw: HashMap<char, u64> = HashMap::new();

    for chr in t.chars() {
        *cntr_t.entry(chr).or_default() += 1;
    }

    let (mut have, need) = (0, cntr_t.len());

    for r in 0..s.len() {
        let chr = s[r];

        *wndw.entry(chr).or_default() += 1;
        have += (wndw.get(&chr) == cntr_t.get(&chr)) as usize;

        while have == need {
            if (r - l + 1) < res_len {
                res = (l as i32, r as i32);
            }
            res_len = res_len.min(r - l + 1);
            *wndw.get_mut(&s[l]).unwrap() -= 1;

            if wndw.get(&s[l]) < cntr_t.get(&s[l]) {
                have -= 1;
            }

            l += 1;
        }
    }

    if res.0 > -1 && res.1 > -1 {
        return s[res.0 as usize..=res.1 as usize]
            .into_iter()
            .collect::<String>();
    }

    String::new()
}

fn main() {
    let s = String::from("ADOBECODEBANC");
    let t = String::from("ABC");
    println!("Result: {}", min_window(s, t));
}
