mod analyzer;
use crate::analyzer::dockerfile_analyzer::DockerfileAnalyzer;

fn main() {
    let analyzer: DockerfileAnalyzer = DockerfileAnalyzer::new("Dockerfile");
    
    if let Some(base_image) = analyzer.get_base_image() {
        println!("{}", base_image);
    }
    else {
        println!("No base image was found!");
    }

    for port in analyzer.get_ports() {
        println!("Found port to be exposed: {}", port);
    }
}


