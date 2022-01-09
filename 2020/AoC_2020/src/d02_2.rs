use lazy_static::lazy_static;
use regex::Regex;

fn parse_line(line: &str) -> (usize, usize, char, String) {
	lazy_static! {
		static ref RE: Regex = Regex::new(r"^(\d+)\-(\d+) (.): (.+)$").unwrap();
	}
	
	let captures = RE.captures(line).unwrap();
	
	(captures.get(1).unwrap().as_str().parse().unwrap(), captures.get(2).unwrap().as_str().parse().unwrap(),
		captures.get(3).unwrap().as_str().parse().unwrap(), str::to_owned(captures.get(4).unwrap().as_str()))
}

fn validate((lower, upper, chr, string): (usize, usize, char, String)) -> bool {
	let string: Vec<char> = string.chars().collect();
	
	string.get(lower-1).map(|c| c == &chr).unwrap_or_default() ^
		string.get(upper-1).map(|c| c == &chr).unwrap_or_default()
}

pub fn main(input: String) {	

	let parsed: Vec<_> = input.lines()
			.map(|s| s.to_string())
			.map(|line| parse_line(&line))
			.map(validate)
			.filter(|b| *b)
			.collect();
			
    println!("{:?}", parsed.len());
}
