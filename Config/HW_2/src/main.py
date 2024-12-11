import argparse
from src.dependency_parser import DependencyParser
from src.graph_builder import GraphBuilder

def main():
    parser = argparse.ArgumentParser(description="Dependency Visualizer")
    parser.add_argument("--path-to-program", required=True, help="Path to graph visualization tool")
    parser.add_argument("--package-name", required=True, help="Name of the Maven package to analyze")
    parser.add_argument("--output-file", required=True, help="Path to the output Mermaid file")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum depth of dependency analysis")
    parser.add_argument("--repo-url", default="https://repo.maven.apache.org/maven2/", help="URL of the Maven repository")

    args = parser.parse_args()

    parser = DependencyParser(args.repo_url, args.max_depth)
    dependencies = parser.get_dependencies(args.package_name)

    builder = GraphBuilder()
    mermaid_code = builder.build_graph(dependencies)

    with open(args.output_file, "w") as output_file:
        output_file.write(mermaid_code)

    print(f"Dependency graph saved to {args.output_file}")

if __name__ == "__main__":
    main()
