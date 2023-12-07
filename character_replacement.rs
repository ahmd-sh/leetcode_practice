use std::collections::HashMap;

fn character_replacement(s: String, k: i32) -> i32 {
    let s: Vec<char> = s.chars().collect();
    let (mut l,mut res,mut max_f) = (0,0,0);
    let mut hm: HashMap<char, u64> = HashMap::new();

    for r in 0..s.len(){
      *hm.entry(s[r]).or_default() += 1;
      max_f = max_f.max(*hm.get(&s[r]).unwrap());

      if (r-l+1) - max_f as usize > k as usize {
        *hm.get_mut(&s[l]).unwrap() -= 1;
        l += 1;
      }

      res = res.max(r-l+1);
    }
    res as i32
}

fn main() {
    let s = String::from("AABABBA");
    let k = 2;
    let res = character_replacement(s, k);

    println!("{}", res);
}
