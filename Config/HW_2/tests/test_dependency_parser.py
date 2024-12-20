import unittest
from src.dependency_parser import DependencyParser

class TestDependencyParser(unittest.TestCase):
    def setUp(self):
        self.parser = DependencyParser("https://repo.maven.apache.org/maven2/", max_depth=2)

    def test_parse_pom(self):
        pom_content = """
        <project>
            <dependencies>
                <dependency>
                    <groupId>org.example</groupId>
                    <artifactId>example-lib</artifactId>
                </dependency>
            </dependencies>
        </project>
        """
        dependencies = self.parser.parse_pom(pom_content)
        self.assertEqual(dependencies, ["org.example:example-lib"])
