use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashSet;

fn main() {
    // File hosts must exist in current path before this produces output
    if let Ok(lines) = read_lines("./input.txt") {
        // Consumes the iterator, returns an (Optional) String
        let mut rucksacks: Vec<HashSet<char>> = Vec::new();

        let mut sum1=0;
        let mut sum2=0;
        for line in lines {
            if let Ok(l) = line {
                //lt first = &l[..l.len()/2];
                //let second = &l[l.len()/2..];
                let mid = l.len()/2;
                rucksacks.push(l.chars().into_iter().collect());

                let a: HashSet<char> = l[..mid].chars().into_iter().collect();
                let b: HashSet<char> = l[mid..].chars().into_iter().collect();
                for i in  a.intersection(&b) {
                    sum1+=calc_priority(*i);
                }
            }
        }

        while rucksacks.len()!=0 {
            for i in intersection(vec![rucksacks.pop().unwrap(),rucksacks.pop().unwrap(),rucksacks.pop().unwrap()]){
                sum2+=calc_priority(i);
            }
        }

        println!("{}", sum1);
        println!("{}", sum2);
    }
}

fn intersection(mut sets: Vec<HashSet<char>>) -> HashSet<char> {
    if sets.is_empty() {
        return HashSet::new();
    }
    
    if sets.len() == 1 {
        return sets.pop().unwrap();
    }
    
    let mut result = sets.pop().unwrap();
    result.retain(|item| {
        sets.iter().all(|set| set.contains(item))
    });
    result
}

fn calc_priority(c: char) -> u32 {
    if c>='a' {
        return  c as u32 + 1 - 'a' as u32;
    } else {
        return c as u32 + 27 - 'A' as u32;
    }
}
/*
fn str_hash(str: &str) -> &mut HashSet<char> {
    let mut a: HashSet<char>;
    for c in str.chars()
}*/

    // The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
