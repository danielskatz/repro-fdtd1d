mkdir raw
mkdir proc
wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0001.jpg -O raw/0001.jpg
wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0002.jpg -O raw/0002.jpg
wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0003.jpg -O raw/0003.jpg
wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0004.jpg -O raw/0004.jpg
python3 bin/sharpen_image.py raw/0001.jpg proc/0001_sharp.jpg
python3 bin/sharpen_image.py raw/0002.jpg proc/0002_sharp.jpg
python3 bin/sharpen_image.py raw/0003.jpg proc/0003_sharp.jpg
python3 bin/sharpen_image.py raw/0004.jpg proc/0004_sharp.jpg
python3 bin/local_build_mosaic.py 2 proc/mosaic.jpg proc/0001_sharp.jpg proc/0002_sharp.jpg proc/0003_sharp.jpg proc/0004_sharp.jpg
