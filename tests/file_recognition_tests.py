import unittest
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from src.find_format import recognize_format


class TestFileRecognizer(unittest.TestCase):
    def test_video_formats(self):
        self.assertEqual(recognize_format("movie.mp4"), "VIDEO")
        self.assertEqual(recognize_format("clip.avi"), "VIDEO")

    def test_audio_formats(self):
        self.assertEqual(recognize_format("song.mp3"), "AUDIO")
        self.assertEqual(recognize_format("sound.wav"), "AUDIO")

    def test_image_formats(self):
        self.assertEqual(recognize_format("photo.jpg"), "GFX")
        self.assertEqual(recognize_format("picture.png"), "GFX")

    def test_text_formats(self):
        self.assertEqual(recognize_format("document.txt"), "TEXT")
        self.assertEqual(recognize_format("notes.pdf"), "TEXT")

    def test_project_formats(self):
        self.assertEqual(recognize_format("video_edit.prproj"), "PROJECT")
        self.assertEqual(recognize_format("animation.aep"), "PROJECT")

    def test_unknown_formats(self):
        self.assertEqual(recognize_format("archive.unknown"), "UNKNOWN")
        self.assertEqual(recognize_format("no_extension"), "UNKNOWN")


if __name__ == '__main__':
    unittest.main()
