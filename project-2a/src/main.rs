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
        characters.sort_by(|a,b| b.cmp(a));

        let mut has_three_unique : bool = false;
        let mut has_two_unique : bool = false;

        let mut prev_char: char = '_';
        let mut found: u32 = 0;
        let sorted_string: String = characters.clone().into_iter().collect();

        for character in characters {
            if prev_char == character {
                found = found + 1;
            } else {
                if found == 2 {
                    has_two_unique = true;
                }
                if found == 3 {
                    has_three_unique = true;
                }
                found = 1;
            }

            prev_char = character;
        }

        if found == 2 {
            has_two_unique = true;
        }
        if found == 3 {
            has_three_unique = true;
        }

        if has_two_unique {
            let current: u32 =  match results.get_mut(&2) {
                Some(val) => *val + 1,
                None => 1
            };
            results.insert(2, current);
        }
        if has_three_unique {
            let current: u32 =  match results.get_mut(&3) {
                Some(val) => *val + 1,
                None => 1
            };
            results.insert(3, current);
        }
        
        println!("String: {} {} {}", sorted_string, has_two_unique, has_three_unique);
    }
    let two_values = match results.get(&2) {
        Some(val) => *val,
        None => 0
    };

    let three_values = match results.get(&3) {
        Some(val) => *val,
        None => 0
    };

    println!("{}",two_values);
    println!("{}",three_values);
    println!("{}",two_values * three_values);

    Ok(())
}