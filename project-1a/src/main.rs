use std::fs::File;
use std::io::{BufRead, BufReader, Result};

fn main() -> Result<()> {
    let file = File::open("input.txt")
    	.expect("Couldn't Open");

    let mut result = 0;

    for line in BufReader::new(file).lines() {
        let line: i32 = line.unwrap().trim().parse().expect("Couldn't parse");
        result += line;
    }

    println!("{}",result);

    Ok(())
}