use std::collections::{BinaryHeap, VecDeque, HashMap};

impl Solution {
    pub fn least_interval(tasks: Vec<char>, n: i32) -> i32 {
        let mut time = 0;
        let mut count = HashMap::new();

        let mut max_heap = BinaryHeap::new();
        let mut deque: VecDeque<(i32,i32)> = VecDeque::new();

        for t in tasks {
            let count = count.entry(t).or_insert(0);
            *count += 1;
        }

        for (key, val) in count.iter() {
            max_heap.push(*val);
        }

        while max_heap.len() > 0 || deque.len() > 0 {
            time += 1;

            if max_heap.len() > 0 {
                let left = max_heap.pop().unwrap() - 1;
                if left != 0 {
                    deque.push_back((left, time + n));
                }
            }

            if deque.len() > 0 && deque[0].1 == time {
                max_heap.push(deque.pop_front().unwrap().0);
            }
        }
        time
    }
}
