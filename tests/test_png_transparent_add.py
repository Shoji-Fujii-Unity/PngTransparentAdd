import tempfile
import unittest
from pathlib import Path

from PIL import Image

from png_transparent_add import add_transparency_to_png


class PngTransparentAddTests(unittest.TestCase):
    def test_adds_transparency_based_on_top_left_pixel_and_tolerance(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            input_path = Path(tmpdir) / "input.png"
            output_path = Path(tmpdir) / "output.png"

            image = Image.new("RGBA", (3, 2), (255, 255, 255, 255))
            image.putpixel((0, 0), (10, 20, 30, 255))
            image.putpixel((1, 0), (11, 21, 31, 255))
            image.putpixel((2, 0), (50, 60, 70, 255))
            image.putpixel((0, 1), (12, 24, 34, 255))
            image.putpixel((1, 1), (100, 110, 120, 255))
            image.putpixel((2, 1), (10, 20, 30, 255))
            image.save(input_path)

            add_transparency_to_png(input_path, output_path, tolerance=5)

            output_image = Image.open(output_path).convert("RGBA")

            self.assertEqual(output_image.getpixel((0, 0)), (10, 20, 30, 0))
            self.assertEqual(output_image.getpixel((1, 0)), (11, 21, 31, 0))
            self.assertEqual(output_image.getpixel((2, 0)), (50, 60, 70, 255))
            self.assertEqual(output_image.getpixel((0, 1)), (12, 24, 34, 0))
            self.assertEqual(output_image.getpixel((1, 1)), (100, 110, 120, 255))
            self.assertEqual(output_image.getpixel((2, 1)), (10, 20, 30, 0))


if __name__ == "__main__":
    unittest.main()
