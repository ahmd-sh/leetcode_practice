#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
    let (mut prev, mut curr) = (None, head);
    while let Some(mut node) = curr {
        curr = node.next;
        node.next = prev;
        prev = Some(node);
    }
    prev
}

fn main() {
    let third = Box::new(ListNode::new(3));
    let second = Box::new(ListNode { val: 2, next: Some(third) });
    let first = Box::new(ListNode { val: 1, next: Some(second) });
    let list = Some(first);

    println!("{:?}", reverse_list(list));
}
