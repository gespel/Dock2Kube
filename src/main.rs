mod analyzer;
use crate::analyzer::dockerfile_analyzer::DockerfileAnalyzer;

fn main() {
    let analyzer: DockerfileAnalyzer = DockerfileAnalyzer::new("Dockerfile");
    println!("{:?}", analyzer.get_images());
}


