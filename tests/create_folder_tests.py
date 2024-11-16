import unittest
import tempfile
import os
from unittest.mock import patch
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))
from src.create_folder import CreateFolders

class TestCreateFolders(unittest.TestCase):

    @patch("src.create_folder.filedialog.askdirectory")
    @patch("src.create_folder.os.makedirs")
    @patch("src.create_folder.shutil.move")
    @patch("src.create_folder.walk")
    def test_organize_folder(self, mock_walk, mock_move, mock_makedirs, mock_askdirectory):
        mock_askdirectory.return_value = "/fake/test/directory"

        mock_walk.return_value = iter([(
            "/fake/test/directory",
            None,
            ["video.mp4", "audio.mp3", "image.jpg", "unknown.xyz"]
        )])

        folder_creator = CreateFolders()
        folder_creator.organize_folder("Test_Project")

        expected_folders = [
            "/fake/test/directory/Test_Project",
            "/fake/test/directory/Test_Project/VIDEO",
            "/fake/test/directory/Test_Project/GFX",
            "/fake/test/directory/Test_Project/AUDIO",
            "/fake/test/directory/Test_Project/TEXT",
            "/fake/test/directory/Test_Project/SFX",
        ]

        print("Checking the actual calls to makedirs:")
        for call in mock_makedirs.call_args_list:
            print(f"makedirs called with: {call}")

        for folder in expected_folders:
            found = False
            for call in mock_makedirs.call_args_list:
                if folder in str(call):
                    found = True
                    break
            self.assertTrue(found, f"Expected call for {folder} not found")

        print(f"makedirs call count: {mock_makedirs.call_count}")
        self.assertEqual(mock_makedirs.call_count, len(expected_folders))

        mock_move.assert_any_call(
            "/fake/test/directory/video.mp4",
            "/fake/test/directory/Test_Project/VIDEO/video.mp4",
        )
        mock_move.assert_any_call(
            "/fake/test/directory/audio.mp3",
            "/fake/test/directory/Test_Project/AUDIO/audio.mp3",
        )
        mock_move.assert_any_call(
            "/fake/test/directory/image.jpg",
            "/fake/test/directory/Test_Project/GFX/image.jpg",
        )

        self.assertEqual(mock_move.call_count, 3)

    @patch("src.create_folder.filedialog.askdirectory")
    @patch("src.create_folder.shutil.move")
    @patch("src.create_folder.os.makedirs")
    @patch("src.create_folder.walk")
    def test_empty_directory(self, mock_walk, mock_makedirs, mock_move, mock_askdirectory):
        mock_askdirectory.return_value = "/empty/directory"

        mock_walk.return_value = iter([("/empty/directory", [], [])])

        folder_creator = CreateFolders()
        folder_creator.organize_folder("Empty_Project")
        mock_move.assert_not_called()

    @patch("src.create_folder.filedialog.askdirectory")
    @patch("src.create_folder.shutil.move")
    def test_empty_directory_temp(self, mock_move, mock_askdirectory):
        with tempfile.TemporaryDirectory() as tmpdirname:
            mock_askdirectory.return_value = tmpdirname

            with patch("src.create_folder.walk", return_value=iter([(tmpdirname, [], [])])):
                folder_creator = CreateFolders()
                folder_creator.organize_folder("Empty_Project")

                mock_move.assert_not_called()

            assert os.path.exists(tmpdirname)

if __name__ == "__main__":
    unittest.main()
