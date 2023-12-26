
fn search_rotated(nums: Vec<i32>, target: i32) -> i32 {
    let (mut l, mut r) = (0, nums.len() - 1);

    while l <= r {
        let m = (l + r) / 2;

        if nums[m] == target {
            return m as i32;
        }

        if nums[m] >= nums[l] {
            if nums[m] < target || nums[l] > target {
                l = m + 1
            } else {
                r = m - 1
            }
        }
        else {
            if nums[m] > target || nums[r] < target {
                r = m - 1
            } else {
                l = m + 1
            }
        }
    }
    -1
}

fn main() {
    let nums: Vec<i32> = vec![4,5,6,7,0,1,2];
    let target = 2;
    println!("{:?}", search_rotated(nums, target));
}
