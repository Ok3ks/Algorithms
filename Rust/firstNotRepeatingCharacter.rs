"""Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it.
If there is no such character, return '_'."""

fn solution(s: String) -> char {
    let mut c = [0usize; 256];
    let mut p = [0usize; 256];
    for i in 0..s.len() {
        let b = s.as_bytes()[i] as usize;
        if c[b] == 0 {
            p[b] = i;
        }
        c[b] += 1;
    }
    let mut ch = '_';
    let mut ps = s.len();
    for i in 0..256 {
        if c[i] == 1 && p[i] < ps {
            ps = p[i];
            ch = i as u8 as char;
        }
    }
    ch
}
