# Planesight

## Description

This steganography tool allows you to hide text data within the color channels of an image. The hidden text can be later extracted using appropriate techniques. This can be useful for various applications, including watermarking, secret messages, or simply embedding information in an image.

## Usage

Run the tool from the command line with the following syntax:

```bash
$ python3 image_hiding_tool.py input_image.png flag_image.png output_image.png
```

## How It Works

1. **Input Image**: Provide the path to the input image (`input_image.png`) that you want to hide text in.

2. **Text to Image Conversion**: To hide text in the image, you can use online tools like [text2image.com](https://text2image.com/en/) to convert the text into a PNG image with a transparent background. Make sure that the dimensions of this image match the input image, and avoid using black as the font color as it may not work well.

3. **Usage**: Run the tool using the command line. You need to specify three paths as arguments:
    - `image_path`: Path to the input image.
    - `flag_path`: Path to the PNG image with the hidden text (the flag image).
    - `output_path`: Path to save the resulting image.

4. **Processing**: The tool resizes the flag image to match the input image's dimensions. It converts both images to the 'RGB' mode and splits them into their red, green, and blue color channels.

5. **Hiding Text**: The text is hidden in the color channels by performing bitwise operations. The provided tool uses the expression `"convert((a & 254) | (b & 1), 'L')"` to blend the image and flag in each channel.

6. **Output**: The resulting image is saved as `output_image.png`, and it contains the hidden text.

