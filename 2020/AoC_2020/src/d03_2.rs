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
    let vert = data.len();

    let mut product: u128  = 1;

    for (dr, dd) in [(1,1), (3,1), (5,1), (7,1), (1,2)].iter() {
        
        let mut trees = 0;
        let mut vert_index = 0;
        let mut horiz_index = 0;

        while vert_index < vert {
            if *data.get(vert_index).unwrap().trees.get(horiz_index).unwrap() {
                trees += 1;
            }
            horiz_index += dr;
            if horiz_index >= horiz {
                horiz_index -= horiz;
            }

            vert_index += dd;
        }

        product *= trees;
    }

    println!("{}", product);
}

pub fn main(input: String) {	
	let parsed: Vec<LineData> = input.lines()
			.map(|s| s.to_string())
			.map(|line| line.parse())
			.filter_map(Result::ok)
			.collect();

    consume(parsed);
}