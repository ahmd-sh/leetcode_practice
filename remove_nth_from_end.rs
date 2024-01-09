// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode { val: 0, next: head.clone() });
        let (mut left, mut right) = (dummy.as_mut(), head);

        for x in 0..n {
            right = right.unwrap().next;
        }

        while let Some(r) = right {
            left = left.next.as_mut().unwrap();
            right = r.next;
        }

        left.next = left.next.take().unwrap().next.take();
        dummy.next
    }
}
