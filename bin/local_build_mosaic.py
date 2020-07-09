import sys

try:
    from PIL import Image, ImageFilter
except ImportError:
    print("error:", sys.argv[0], "requires Pillow - install it via 'pip install Pillow'")
    sys.exit(2)

edge_len = int(sys.argv[1])
output_filename = sys.argv[2]

size = edge_len*100

outputImage = Image.new('RGB', [size, size])
index = 0
for i in range(edge_len):
    for j in range(edge_len):
        inputImage = Image.open("{:04d}_sharp.jpg".format(index+1))
        box = ((i)*100, (j)*100, (i+1)*100, (j+1)*100)
        region = inputImage.crop(box)
        outputImage.paste(region, box)
        index=index+1

outputImage.save(output_filename, 'JPEG')
