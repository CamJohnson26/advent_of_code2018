use std::fs::File;
use std::io::{BufRead, BufReader, Result};
use std::collections::HashMap;

fn main() -> Result<()> {

    let mut results = HashMap::new();

    results.insert(2, 0);
    results.insert(3, 0);

    let file = File::open("input.txt")
        .expect("Couldn't Open");

    for line in BufReader::new(file).lines() {
        let mut characters: Vec<_> = line.unwrap().chars().collect();
        let answer1: String = characters.clone().into_iter().collect();
        let file2 = File::open("input.txt")
            .expect("Couldn't Open");

        for line2 in BufReader::new(file2).lines() {
            let mut mismatches:u32 = 0;
            let mut characters2: Vec<_> = line2.unwrap().chars().collect();
            let answer2: String = characters2.clone().into_iter().collect();
            
            for i in (0..characters.len()) { 
                if characters[i] != characters2[i] {
                    mismatches += 1;
                }
            }

            if mismatches == 1 {
                println!("{} {}", answer1, answer2);
            }
        }

    }

    Ok(())
}