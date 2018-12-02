use std::fs::File;
use std::io::{BufRead, BufReader, Result};
use std::collections::HashMap;

fn main() -> Result<()> {

    let mut results = HashMap::new();
    let mut result = 0;

    results.insert(0, true);

    loop {
        let mut found = false;

        let file = File::open("input.txt")
            .expect("Couldn't Open");

        for line in BufReader::new(file).lines() {
            let line: i32 = line.unwrap().trim().parse().expect("Couldn't parse");
            result = line + result;
            match results.get(&result) {
                Some(&value) => {println!("{}", &result);found = true; break;}
                _ => {results.insert(result, true);}
            }
        }

        if found {
            break;
        }
    }

    Ok(())
}