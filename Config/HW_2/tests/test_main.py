import unittest
from unittest.mock import patch
from src.main import main

class TestMain(unittest.TestCase):
    @patch("src.main.DependencyParser.get_dependencies")
    @patch("src.main.open")
    def test_main(self, mock_open, mock_get_dependencies):
        mock_get_dependencies.return_value = {"packageA": ["packageB"]}
        mock_open.return_value = unittest.mock.mock_open()

        with patch("argparse.ArgumentParser.parse_args") as mock_args:
            mock_args.return_value = argparse.Namespace(
                path_to_program="/path/to/visualizer",
                package_name="packageA",
                output_file="/path/to/output.mmd",
                max_depth=2,
                repo_url="https://fake.repo.maven/"
            )
            main()

        mock_open.assert_called_once_with("/path/to/output.mmd", "w")
        mock_get_dependencies.assert_called_once_with("packageA")
