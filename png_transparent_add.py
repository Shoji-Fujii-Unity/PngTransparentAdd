import argparse
from pathlib import Path
from typing import Optional

from PIL import Image


def add_transparency_to_png(input_path: Path | str, output_path: Path | str, tolerance: int = 0) -> None:
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    with Image.open(input_path) as image:
        image = image.convert("RGBA")
        width, height = image.size
        base_r, base_g, base_b, _ = image.getpixel((0, 0))

        for y in range(height):
            for x in range(width):
                r, g, b, a = image.getpixel((x, y))
                if (
                    abs(r - base_r) <= tolerance
                    and abs(g - base_g) <= tolerance
                    and abs(b - base_b) <= tolerance
                ):
                    image.putpixel((x, y), (r, g, b, 0))

        output_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(output_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Add transparency to PNG based on the top-left pixel color")
    parser.add_argument("input", help="Path to the input PNG file")
    parser.add_argument("output", help="Path to save the output PNG file")
    parser.add_argument("--tolerance", type=int, default=0, help="Color difference tolerance for similar colors")
    args = parser.parse_args()

    add_transparency_to_png(args.input, args.output, tolerance=args.tolerance)


if __name__ == "__main__":
    main()
