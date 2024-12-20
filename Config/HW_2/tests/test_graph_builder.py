import unittest
from src.graph_builder import GraphBuilder

class TestGraphBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = GraphBuilder()

    def test_build_graph(self):
        dependencies = {
            "packageA": ["packageB", "packageC"],
            "packageB": ["packageD"],
        }
        result = self.builder.build_graph(dependencies)
        expected = """graph TD
    packageA --> packageB
    packageA --> packageC
    packageB --> packageD
"""
        self.assertEqual(result, expected)
