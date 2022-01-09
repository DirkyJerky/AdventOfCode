use std::str::FromStr;

#[derive(Default, Debug)]
struct Passport {
    pub byr: Option<String>,
    pub iyr: Option<String>,
    pub eyr: Option<String>,
    pub hgt: Option<String>,
    pub hcl: Option<String>,
    pub ecl: Option<String>,
    pub pid: Option<String>,
    pub cid: Option<String>,
}

impl FromStr for Passport {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut ppt: Passport = Default::default();

        for token in s.split_ascii_whitespace() {
            let mut subtokens = token.split(':');
            match subtokens.next().unwrap_or("") {
                "byr" => {
                    ppt.byr = Some(subtokens.next().unwrap_or("").to_string());
                },
                "iyr" => {
                    ppt.iyr = Some(subtokens.next().unwrap_or("").to_string());
                },
                "eyr" => {
                    ppt.eyr = Some(subtokens.next().unwrap_or("").to_string());
                },
                "hgt" => {
                    ppt.hgt = Some(subtokens.next().unwrap_or("").to_string());
                },
                "hcl" => {
                    ppt.hcl = Some(subtokens.next().unwrap_or("").to_string());
                },
                "ecl" => {
                    ppt.ecl = Some(subtokens.next().unwrap_or("").to_string());
                },
                "pid" => {
                    ppt.pid = Some(subtokens.next().unwrap_or("").to_string());
                },
                "cid" => {
                    ppt.cid = Some(subtokens.next().unwrap_or("").to_string());
                },
                _ => {}
            }
        }

        Ok(ppt)
    }
}

impl Passport {
    pub fn is_valid(&self) -> bool {
        self.byr.is_some() && self.iyr.is_some() 
            && self.eyr.is_some() && self.hgt.is_some()
            && self.hcl.is_some() && self.ecl.is_some() 
            && self.pid.is_some()
    }
}

pub fn main(input: String) {	
	let lines: Vec<String> = input.lines()
			.map(|s| s.to_string())
            .collect();
    
    let mut ppts: Vec<Passport> = Vec::new();

    let mut data = String::new();
    
    for line in lines {
        if line.is_empty() {
            ppts.push(data.parse().unwrap());
            data = String::new();
        } else {
            data.push(' ');
            data.push_str(&line);
        }
    }

    if ! data.is_empty() {
        ppts.push(data.parse().unwrap());
    }
    
    println!("{}", ppts.iter().filter(|p| p.is_valid()).count())
}
