pub fn main(input: String) {
	let ints: Vec<usize> = input.lines()
			.map(|line| { line.parse::<usize>().unwrap() }).collect();
	
	'o:
	for i in 0..ints.len() {
		for j in i..ints.len() {
			for k in j..ints.len() {
				if ints[i] + ints[j] + ints[k] == 2020 {
					println!("{}", ints[i] * ints[j] * ints[k]);
					break 'o;
				}
			}
		}
	}
}
