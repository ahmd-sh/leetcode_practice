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
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(node) = root.clone() {
            let mut node_borrow = node.borrow_mut();
            let left = node_borrow.left.take();
            let right = node_borrow.right.take();

            node_borrow.left = right;
            node_borrow.right = left;

            Self::invert_tree(node_borrow.left.clone());
            Self::invert_tree(node_borrow.right.clone());
        }
        root
    }
}

// // More memory efficient:
// root.map(|node| {
//     {
//       let mut node_ref = node.borrow_mut();
//       let left = node_ref.left.take();
//       let right = node_ref.right.take();
//       node_ref.right = Solution::invert_tree(left);
//       node_ref.left = Solution::invert_tree(right);
//     }
//     node
// })
