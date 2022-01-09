use lazy_static::lazy_static;
use regex::Regex;
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
        lazy_static! {
            static ref RE_HEIGHT: Regex = Regex::new(r"^(\d+)(cm|in)$").unwrap();
            static ref RE_HCL: Regex = Regex::new(r"^#[0-9a-f]{6}$").unwrap();
            static ref RE_ECL: Regex = Regex::new(r"^(amb|blu|brn|gry|grn|hzl|oth)$").unwrap();
            static ref RE_PID: Regex = Regex::new(r"^\d{9}$").unwrap();
        }
		dbg!(self);
		
        dbg!(self.byr.is_some() && self.iyr.is_some() 
            && self.eyr.is_some() && self.hgt.is_some()
            && self.hcl.is_some() && self.ecl.is_some() 
            && self.pid.is_some())
        &&
        dbg!((1920..=2002).contains(&self.byr.as_ref().unwrap().parse::<usize>().unwrap()))
        && 
        dbg!((2010..=2020).contains(&self.iyr.as_ref().unwrap().parse::<usize>().unwrap()))
        && 
        dbg!((2020..=2030).contains(&self.eyr.as_ref().unwrap().parse::<usize>().unwrap()))
        && 
        dbg!({
            RE_HEIGHT.captures(self.hgt.as_ref().unwrap().as_str()).and_then(|caps| {
				caps.get(2).and_then(|spec| {
					caps.get(1).map(|num| {
						let num = num.as_str().parse::<usize>().unwrap();
						if spec.as_str() == "cm" {
							(150..=193).contains(&num)
						} else {
							(59..=76).contains(&num)
						}
					})
				})
			}).unwrap_or_default()
        })
        && 
		dbg!(RE_HCL.is_match(self.hcl.as_ref().unwrap()))
		&&
		dbg!(RE_ECL.is_match(self.ecl.as_ref().unwrap()))
		&&
		dbg!(RE_PID.is_match(self.pid.as_ref().unwrap()))
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
