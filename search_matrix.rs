use std::cmp::Ordering::{Equal, Less, Greater};

fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
    for row in &matrix {
        if let Some(&last_element) = row.last() {
            if last_element < target {
                continue;
            } else {
                let (mut l, mut r) = (0, row.len());
                while l < r {
                    let m = l + (r - l) / 2;
                    match target.cmp(&row[m]) {
                        Equal => return true,
                        Less => r = m,
                        Greater => l = m + 1,
                    }
                }
            }
        }
    }
    false
}

fn main() {
    let matrix: Vec<Vec<i32>> = vec![
        vec![1, 3, 5, 7],
        vec![10, 11, 16, 20],
        vec![23, 30, 34, 60],
    ];
    let target = -1;
    println!("{:?}", search_matrix(matrix, target));
}
