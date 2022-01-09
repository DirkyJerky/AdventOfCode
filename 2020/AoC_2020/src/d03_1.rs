use std::str::FromStr;

struct LineData {
    pub trees: Vec<bool>
}

impl FromStr for LineData {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(LineData {
            trees: s.chars().map(|c| c == '#').collect()
        })
    }
}

fn consume(data: Vec<LineData>) {  
    let horiz = data.get(0).unwrap().trees.len();

    let mut trees = 0;
    let mut index = 0;

    for line in data {
        if *line.trees.get(index).unwrap() {
            trees += 1;
        }
        index += 3;
        if index >= horiz {
            index -= horiz;
        } 
    }

    println!("{}", trees);
}

pub fn main(input: String) {
	let parsed: Vec<LineData> = input.lines()
			.map(|s| s.to_string())
			.map(|line| line.parse())
			.filter_map(Result::ok)
			.collect();

    consume(parsed);
}
