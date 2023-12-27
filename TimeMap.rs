use std::collections::HashMap;

struct TimeMap {
    time_map: HashMap::<String, Vec<(String, i32)>>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TimeMap {

    fn new() -> Self {
        Self {
            time_map: HashMap::new()
        }
    }
    
    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.time_map.entry(key).or_default().push((value, timestamp));
    }
    
    fn get(&self, key: String, timestamp: i32) -> String {
        let mut value = String::new();

        if let Some(t_list) = self.time_map.get(&key) {
            let (mut l, mut r) = (0, t_list.len());

            while l < r {
                let m = l + (r - l) / 2;
                if timestamp < t_list[m].1 {
                    r = m;
                } else {
                    value = t_list[m].0.clone();
                    l = m + 1;
                }
            }
        }
        value
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap::new();
 * obj.set(key, value, timestamp);
 * let ret_2: String = obj.get(key, timestamp);
 */
