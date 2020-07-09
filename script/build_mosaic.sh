mkdir raw
mkdir proc
cd raw
wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0001.jpg
wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0002.jpg
wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0003.jpg
wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0004.jpg
cd ..
python bin/sharpen_image.py raw/0001.jpg proc/0001_sharp.jpg
python bin/sharpen_image.py raw/0002.jpg proc/0002_sharp.jpg
python bin/sharpen_image.py raw/0003.jpg proc/0003_sharp.jpg
python bin/sharpen_image.py raw/0004.jpg proc/0004_sharp.jpg
cd proc
python ../bin/local_build_mosaic.py 2 mosaic.jpg
cd ..
