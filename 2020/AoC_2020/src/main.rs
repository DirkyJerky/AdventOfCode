use std::io::Read;
use std::env;
use std::fs::File;
use std::path::Path;
mod d01_1;
mod d01_2;
mod d02_1;
mod d02_2;
mod d03_1;
mod d03_2;
mod d04_1;
mod d04_2;
mod d05_1;
mod d05_2;
mod d06_1;
mod d06_2;
mod d07_1;
mod d07_2;
mod d08_1;
mod d08_2;
mod d09_1;
mod d09_2;
mod d10_1;
mod d10_2;
mod d11_1;
mod d11_2;
mod d12_1;
mod d12_2;
mod d13_1;
mod d13_2;
mod d14_1;
mod d14_2;
mod d15_1;
mod d15_2;
mod d16_1;
mod d16_2;
mod d17_1;
mod d17_2;
mod d18_1;
mod d18_2;
mod d19_1;
mod d19_2;
mod d20_1;
mod d20_2;
mod d21_1;
mod d21_2;
mod d22_1;
mod d22_2;
mod d23_1;
mod d23_2;
mod d24_1;
mod d24_2;
mod d25_1;
mod d25_2;
mod d26_1;
mod d26_2;
mod d27_1;
mod d27_2;
mod d28_1;
mod d28_2;
mod d29_1;
mod d29_2;
mod d30_1;
mod d30_2;
mod d31_1;
mod d31_2;

fn main() {
    let args: Vec<String> = env::args().collect();

	if args.len() < 3 {
		die(&args[0]);
	}
	
	let day: usize = args[1].to_string().parse().unwrap_or_else(|_| die(&args[0]));
	
	let num: usize = args[2].to_string().parse().unwrap_or_else(|_| die(&args[0]));
	
	let input_path_str = format!("/tmp/day{}.txt", day);
	let input_path = Path::new(input_path_str.as_str());
	
	if !input_path.is_file() { 
		eprintln!("Input file {} does not exist", input_path.to_str().expect("failed path.to_str"));
		die(&args[0]);
	}
	
	let mut file = File::open(input_path).expect("failed to open input file");
	
	let mut content = String::new();
	file.read_to_string(&mut content).expect("failed to read file to string");
	
	match num {
		1 => {
			match day {
				1 => {
					d01_1::main(content);
				},
				2 => {
					d02_1::main(content);
				},
				3 => {
					d03_1::main(content);
				},
				4 => {
					d04_1::main(content);
				},
				5 => {
					d05_1::main(content);
				},
				6 => {
					d06_1::main(content);
				},
				7 => {
					d07_1::main(content);
				},
				8 => {
					d08_1::main(content);
				},
				9 => {
					d09_1::main(content);
				},
				10 => {
					d10_1::main(content);
				},
				11 => {
					d11_1::main(content);
				},
				12 => {
					d12_1::main(content);
				},
				13 => {
					d13_1::main(content);
				},
				14 => {
					d14_1::main(content);
				},
				15 => {
					d15_1::main(content);
				},
				16 => {
					d16_1::main(content);
				},
				17 => {
					d17_1::main(content);
				},
				18 => {
					d18_1::main(content);
				},
				19 => {
					d19_1::main(content);
				},
				20 => {
					d20_1::main(content);
				},
				21 => {
					d21_1::main(content);
				},
				22 => {
					d22_1::main(content);
				},
				23 => {
					d23_1::main(content);
				},
				24 => {
					d24_1::main(content);
				},
				25 => {
					d25_1::main(content);
				},
				26 => {
					d26_1::main(content);
				},
				27 => {
					d27_1::main(content);
				},
				28 => {
					d28_1::main(content);
				},
				29 => {
					d29_1::main(content);
				},
				30 => {
					d30_1::main(content);
				},
				31 => {
					d31_1::main(content);
				},
				_ => {
					eprintln!("day = 1..31");
					die(&args[0]);
				}
			}
		},
		2 => {
			match day {
				1 => {
					d01_2::main(content);
				},
				2 => {
					d02_2::main(content);
				},
				3 => {
					d03_2::main(content);
				},
				4 => {
					d04_2::main(content);
				},
				5 => {
					d05_2::main(content);
				},
				6 => {
					d06_2::main(content);
				},
				7 => {
					d07_2::main(content);
				},
				8 => {
					d08_2::main(content);
				},
				9 => {
					d09_2::main(content);
				},
				10 => {
					d10_2::main(content);
				},
				11 => {
					d11_2::main(content);
				},
				12 => {
					d12_2::main(content);
				},
				13 => {
					d13_2::main(content);
				},
				14 => {
					d14_2::main(content);
				},
				15 => {
					d15_2::main(content);
				},
				16 => {
					d16_2::main(content);
				},
				17 => {
					d17_2::main(content);
				},
				18 => {
					d18_2::main(content);
				},
				19 => {
					d19_2::main(content);
				},
				20 => {
					d20_2::main(content);
				},
				21 => {
					d21_2::main(content);
				},
				22 => {
					d22_2::main(content);
				},
				23 => {
					d23_2::main(content);
				},
				24 => {
					d24_2::main(content);
				},
				25 => {
					d25_2::main(content);
				},
				26 => {
					d26_2::main(content);
				},
				27 => {
					d27_2::main(content);
				},
				28 => {
					d28_2::main(content);
				},
				29 => {
					d29_2::main(content);
				},
				30 => {
					d30_2::main(content);
				},
				31 => {
					d31_2::main(content);
				},
				_ => {
					eprintln!("day = 1..31");
					die(&args[0]);
				}
			}
		},
		_ => {
			eprintln!("num = 1 | 2");
			die(&args[0]);
		}
	}
}

fn die(prog_name: &str) -> ! {
	eprintln!("Usage: {} <day> <num>", prog_name);
	std::process::exit(1);
}
