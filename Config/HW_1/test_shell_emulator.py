import unittest
from unittest.mock import MagicMock, patch, mock_open
from shell_emulator import ShellEmulator


class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.mock_master = MagicMock()
        self.shell_emulator = ShellEmulator(self.mock_master, "config.toml")
        self.shell_emulator.append_output = MagicMock()

        # Mocking the virtual filesystem
        self.shell_emulator.vfs = MagicMock()
        self.shell_emulator.vfs.namelist.return_value = ["file1.txt", "dir1/", "dir1/file2.txt"]

    @patch("zipfile.ZipFile.open", new_callable=mock_open, read_data="Hello world\nThis is a test file.")
    def test_wc_with_existing_file(self, mock_file):
        self.shell_emulator.command_wc("file1.txt")
        self.shell_emulator.append_output.assert_called_with("2 5 30 file1.txt")

    def test_wc_nonexistent_file(self):
        self.shell_emulator.command_wc("nonexistent.txt")
        self.shell_emulator.append_output.assert_called_with("Error: File not found: nonexistent.txt")

    def test_ls(self):
        self.shell_emulator.cwd = "/"
        self.shell_emulator.command_ls()
        expected_output = "dir1\nfile1.txt"
        self.shell_emulator.append_output.assert_called_with(expected_output)

    def test_cd(self):
        self.shell_emulator.command_cd("dir1")
        self.shell_emulator.append_output.assert_called_with("Changed directory to /dir1")
        self.assertEqual(self.shell_emulator.cwd, "/dir1")

    def test_cd_invalid(self):
        self.shell_emulator.command_cd("invalid_dir")
        self.shell_emulator.append_output.assert_called_with("Error: Directory not found: invalid_dir")
        self.assertEqual(self.shell_emulator.cwd, "/")

    @patch("zipfile.ZipFile.open", new_callable=mock_open, read_data="Hello world\nThis is a test file.")
    def test_wc_with_existing_file(self, mock_file):
        self.shell_emulator.command_wc("file1.txt")
        self.shell_emulator.append_output.assert_called_with("2 5 30 file1.txt")

    def test_unknown_command(self):
        self.shell_emulator.process_command("unknown_command")
        self.shell_emulator.append_output.assert_called_with("Unknown command: unknown_command")
