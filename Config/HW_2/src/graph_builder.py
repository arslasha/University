class GraphBuilder:
    def build_graph(self, dependencies):
        mermaid_code = "graph TD\n"
        for package, deps in dependencies.items():
            for dep in deps:
                mermaid_code += f"    {package} --> {dep}\n"
        return mermaid_code
