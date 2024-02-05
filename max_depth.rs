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
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        match root {
            Some(node) => {
                let node_borrow = node.borrow();

                1 + std::cmp::max(
                    Self::max_depth(node_borrow.left.clone()),
                    Self::max_depth(node_borrow.right.clone()),
                )
            },
            None => 0,
        }
    }
}
