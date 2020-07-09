import sys

try:
    from PIL import Image, ImageFilter
except ImportError:
    print("error:", sys.argv[0], "requires Pillow - install it via 'pip install Pillow'")
    sys.exit(2)


if len(sys.argv) != 3:
    print("error - usage:", sys.argv[0], "input_file output_file")
    sys.exit(2)

input_filename = sys.argv[1]
output_filename = sys.argv[2]

#Read image
try:
    im = Image.open(input_filename)
except OSError:
    print("error - can't open file:", input_file)
    sys.exit(2)

#Apply a filter to the image
im_sharp = im.filter(ImageFilter.SHARPEN)

#Save the filtered image to a new file
im_sharp.save(output_filename, 'JPEG')
