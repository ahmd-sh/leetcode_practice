// 100.00% on LeetCode is a number I thought I'd never see.
fn search(nums: Vec<i32>, target: i32) -> i32 {
    let (mut l, mut r) = (0, nums.len());

    while l < r {
        let m = l + (r - l) / 2;
        match target.cmp(&nums[m]) {
            Equal => return m as i32,
            Less => r = m,
            Greater => l = m + 1,
        }
    }

    -1
}

// My inefficient recursive solution:
// fn bs(nums: &[i32], target: i32, l: usize, u: usize) -> i32 {
//     if l > u {
//         return -1;
//     }
//     let mid = l + (u - l) / 2;
//     if nums[mid] == target {
//         return mid as i32;
//     } else if nums[mid] > target {
//         if mid == 0 {
//             return -1; // Prevents underflow when mid is 0
//         }
//         return bs(nums, target, l, mid - 1);
//     } else {
//         return bs(nums, target, mid + 1, u);
//     }
// }
// fn search(nums: Vec<i32>, target: i32) -> i32 {
//     bs(&nums, target, 0, nums.len()-1)
// }

fn main() {
    let nums = vec![-1, 0, 3, 5, 9, 12];
    let target = 12;
    println!("{:?}", search(nums, target));
}
