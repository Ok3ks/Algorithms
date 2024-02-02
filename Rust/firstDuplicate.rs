
""" Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number 
for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, 
return the number for which the second occurrence has a smaller index than the second occurrence of the other number does.
If there are no such elements, return -1"""

use std::collections::HashSet;

fn solution(a: Vec<i32>) -> i32 {
  let mut S = HashSet::new();
  for i in &a {
    if S.contains(i) { return *i; }
    S.insert(i);
  } 
  return -1;
}

