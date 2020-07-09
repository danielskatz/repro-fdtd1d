import sys

try:
    from PIL import Image, ImageFilter
except ImportError:
    print("error:", sys.argv[0], "requires Pillow - install it via 'pip install Pillow'")
    sys.exit(2)

edge_size = int(sys.argv[1])
outputImage_name = sys.argv[2]

outputImage = Image.new('RGB', [400, 400])
index = 0
for i in range(edge_size):
    for j in range(edge_size):
        inputImage = Image.open(sys.argv[index+3])
        box = ((i)*200, (j)*200, (i+1)*200, (j+1)*200)
        region = inputImage.crop(box)
        outputImage.paste(region, box)
        index=index+1

outputImage.save(outputImage_name, 'JPEG')
