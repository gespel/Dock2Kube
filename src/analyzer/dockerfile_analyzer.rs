use std::{fs};

use regex::Regex;

pub struct DockerfileAnalyzer {
    pub _file_name: String,
    pub file_content: String
}

impl DockerfileAnalyzer {
    pub fn new(file_name: &str) -> Self {
        let file_content = fs::read_to_string(file_name).expect("Unable to read Dockerfile");
        DockerfileAnalyzer {
            _file_name: file_name.to_string(),
            file_content
        }
    }

    pub fn get_images(&self) -> Vec<String> {
        let mut out: Vec<String> = vec![];
        match Regex::new(r"(?m)^FROM\s+([^\s]+)") {
            Ok(re) => {
                for caps in re.captures_iter(self.file_content.as_str()) {
                    if let Some(image_name) = caps.get(1) {
                        //println!("{}", image_name.as_str());
                        out.push(image_name.as_str().to_string());
                    }
                };
            },
            Err(e) => {
                println!("Error while creating the regular expressionfor the FROM! {:?}", e);
            }
        }
        out
    }

    pub fn get_base_image(&self) -> Option<String> {
        let images = self.get_images();
        if let Some(image) = images.first() {
            Some(image.clone())
        }
        else {
            None
        }
    }

    pub fn get_ports(&self) -> Vec<u16> {
        let mut out: Vec<u16> = vec![];

        match Regex::new(r"(?m)^EXPOSE\s+([^\s]+)") {
            Ok(re) => {
                for caps in re.captures_iter(self.file_content.as_str()) {
                    if let Some(image_name) = caps.get(1) {
                        match image_name.as_str().parse::<u16>() {
                            Ok(port) => {
                                out.push(port);
                            }
                            Err(e) => {
                                println!("Error while parsing port number! {:?}", e);
                            }
                        }
                    }
                }
            }
            Err(e) => {
                println!("Error while creating the regular expression for the EXPOSE! {:?}", e);
            }
        }

        out
    }
}