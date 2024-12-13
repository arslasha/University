import requests
import xml.etree.ElementTree as ET


class DependencyParser:
    def __init__(self, repo_url, max_depth):
        self.repo_url = repo_url.rstrip("/")
        self.max_depth = max_depth

    def get_dependencies(self, package_name, current_depth=0):
        if current_depth >= self.max_depth:
            return {}

        # Разбиваем package_name на groupId и artifactId
        try:
            group_id, artifact_id = package_name.split(":")
        except ValueError:
            raise ValueError(f"Invalid package name format: {package_name}. Expected 'groupId:artifactId'.")

        # Получаем последнюю версию пакета
        latest_version = self.get_latest_version(group_id, artifact_id)
        if not latest_version:
            print(f"Could not determine latest version for {package_name}.")
            return {}

        # Формируем URL для POM файла
        pom_url = f"{self.repo_url}/{group_id.replace('.', '/')}/{artifact_id}/{latest_version}/{artifact_id}-{latest_version}.pom"
        print(f"Fetching POM file: {pom_url}")  # Отладка

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

    def get_latest_version(self, group_id, artifact_id):
        metadata_url = f"{self.repo_url}/{group_id.replace('.', '/')}/{artifact_id}/maven-metadata.xml"
        print(f"Fetching metadata: {metadata_url}")  # Отладка

        try:
            response = requests.get(metadata_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching metadata for {group_id}:{artifact_id}: {e}")
            return None

        try:
            root = ET.fromstring(response.text)
            return root.find(".//release").text
        except ET.ParseError as e:
            print(f"Error parsing metadata XML: {e}")
            return None

    def parse_pom(self, pom_content):
        dependencies = []
        try:
            root = ET.fromstring(pom_content)

            # Обработка секции <dependencies>
            for dep in root.findall(".//dependencies/dependency"):
                group_id = dep.find("groupId").text
                artifact_id = dep.find("artifactId").text
                dependencies.append(f"{group_id}:{artifact_id}")

            # Обработка секции <dependencyManagement>
            for dep in root.findall(".//dependencyManagement/dependencies/dependency"):
                group_id = dep.find("groupId").text
                artifact_id = dep.find("artifactId").text
                dependencies.append(f"{group_id}:{artifact_id}")

            # Обработка родительского POM (<parent>)
            parent = root.find(".//parent")
            if parent is not None:
                parent_group_id = parent.find("groupId").text
                parent_artifact_id = parent.find("artifactId").text
                parent_version = parent.find("version").text
                parent_pom_url = f"{self.repo_url}/{parent_group_id.replace('.', '/')}/{parent_artifact_id}/{parent_version}/{parent_artifact_id}-{parent_version}.pom"
                print(f"Fetching parent POM file: {parent_pom_url}")

                try:
                    response = requests.get(parent_pom_url)
                    response.raise_for_status()
                    parent_content = response.text
                    dependencies += self.parse_pom(parent_content)
                except requests.exceptions.RequestException as e:
                    print(f"Error fetching parent POM: {e}")

            print(f"Parsed dependencies: {dependencies}")  # Отладка
        except ET.ParseError as e:
            print(f"Error parsing POM: {e}")
        return dependencies
