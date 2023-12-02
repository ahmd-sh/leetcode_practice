fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
    let mut nums = nums;
    let l = nums.len();
    let mut res = Vec::new();

    if l < 3 {
        return res;
    }

    nums.sort_unstable();

    for i in 0..l {
        if i > 0 && nums[i] == nums[i - 1] {
            continue;
        }
        
        let mut j = i + 1; 
        let mut k = l - 1;
        
        while j < k {
            let ts = nums[i] + nums[j] + nums[k];
            if ts > 0 {
                k -= 1;
            } else if ts < 0 {
                j += 1;
            } else {
                res.push(vec![nums[i], nums[j], nums[k]]);
                j += 1;
                while nums[j] == nums[j-1] && j < k {
                    j += 1
                }
            }
        }
    }

    res
}

fn main() {
    let nums = vec![-1,0,1,2,-1,-4];
    let res = three_sum(nums);

    let formatted_res: Vec<String> = res
        .iter()
        .map(|inner_vec| {
            let numbers: Vec<String> = inner_vec.iter().map(|n| n.to_string()).collect();
            format!("[{}]", numbers.join(", "))
        })
        .collect();

    println!("[{}]", formatted_res.join(", "));
}