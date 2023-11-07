import argparse
import os
from PIL import Image, ImageMath

def process_image(image_path, flag_path, output_path):
    image = Image.open(image_path)
    flag = Image.open(flag_path)
    flag = flag.resize(image.size)
    image = image.convert("RGB")
    flag = flag.convert("RGB")
    image_r, image_g, image_b = image.split()
    flag_r, flag_g, flag_b = flag.split()
    new_r = ImageMath.eval("convert((a & 254) | (b & 1), 'L')", a=image_r, b=flag_r)
    new_g = ImageMath.eval("convert((a & 254) | (b & 1), 'L')", a=image_g, b=flag_g)
    new_b = ImageMath.eval("convert((a & 254) | (b & 1), 'L')", a=image_b, b=flag_b)
    hidden_image = Image.merge("RGB", (new_r, new_g, new_b))
    hidden_image.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Plane Sight(Image Processing Tool)")
    parser.add_argument("image path", help="Path to the input image file")
    parser.add_argument("flag path", help="Path to the flag image file")
    parser.add_argument("output path", nargs='?', default="hidden_flag.png", help="Path to save the resulting image (default: hidden_flag.png)")

    args = parser.parse_args()

    process_image(args.image_path, args.flag_path, args.output_path)

if __name__ == "__main__":
    main()
