// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        fn dfs(root: Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
            match root {
                Some(node) => {
                    let (l_diameter, l_max_depth) = dfs(node.borrow().left.clone());
                    let (r_diameter, r_max_depth) = dfs(node.borrow().right.clone());

                    (
                        l_diameter.max(r_diameter) + 1,
                        l_max_depth.max(r_max_depth.max(l_diameter + r_diameter)),
                    )
                },
                None => (0, 0),
            }
        }
        dfs(root).1

        // // Python approach, translated to Rust
        // let mut res = 0;
        // fn dfs(root: Option<Rc<RefCell<TreeNode>>>, res: &mut i32) -> i32 {
        //     match root {
        //         Some(node) => {
        //             let node_borrow = node.borrow();
        //             let left = dfs(node_borrow.left.clone(), res);
        //             let right = dfs(node_borrow.right.clone(), res);

        //             *res = (*res).max(left + right + 2);
        //             1 + left.max(right)
        //         },
        //         None => -1,
        //     }
        // }
        // dfs(root, &mut res);
        // res
    }
}
