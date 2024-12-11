import requests
import xml.etree.ElementTree as ET

class DependencyParser:
    def __init__(self, repo_url, max_depth):
        self.repo_url = repo_url.rstrip("/")
        self.max_depth = max_depth

    def get_dependencies(self, package_name, current_depth=0):
        if current_depth >= self.max_depth:
            return {}

        pom_url = f"{self.repo_url}/{package_name.replace('.', '/')}/maven-metadata.xml"
        try:
            response = requests.get(pom_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {pom_url}: {e}")
            return {}

        pom_content = response.text
        dependencies = self.parse_pom(pom_content)

        result = {package_name: []}
        for dep in dependencies:
            result[package_name].append(dep)
            result.update(self.get_dependencies(dep, current_depth + 1))

        return result

    def parse_pom(self, pom_content):
        dependencies = []
        try:
            root = ET.fromstring(pom_content)
            for dep in root.findall(".//dependency"):
                group_id = dep.find("groupId").text
                artifact_id = dep.find("artifactId").text
                dependencies.append(f"{group_id}:{artifact_id}")
        except ET.ParseError as e:
            print(f"Error parsing POM: {e}")
        return dependencies
