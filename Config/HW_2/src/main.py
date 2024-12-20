import argparse
from src.dependency_parser import DependencyParser
from src.graph_builder import GraphBuilder
import os

def main():
    parser = argparse.ArgumentParser(description="Dependency Visualizer")
    parser.add_argument("--path-to-program", required=True, help="Path to graph visualization tool")
    parser.add_argument("--package-name", required=True, help="Name of the Maven package to analyze (format: groupId:artifactId)")
    parser.add_argument("--output-file", required=True, help="Path to the output Mermaid file")
    parser.add_argument("--max-depth", type=int, default=3, help="Maximum depth of dependency analysis")
    parser.add_argument("--repo-url", default="https://repo.maven.apache.org/maven2/", help="URL of the Maven repository")

    args = parser.parse_args()

    # Проверяем, существует ли путь для выходного файла, создаем при необходимости
    output_dir = os.path.dirname(args.output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Инициализация и выполнение анализа зависимостей
    parser = DependencyParser(args.repo_url, args.max_depth)
    try:
        dependencies = parser.get_dependencies(args.package_name)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Построение графа
    builder = GraphBuilder()
    mermaid_code = builder.build_graph(dependencies)

    # Сохранение в файл
    with open(args.output_file, "w") as output_file:
        output_file.write(mermaid_code)

    print(f"Dependency graph saved to {args.output_file}")

if __name__ == "__main__":
    main()
