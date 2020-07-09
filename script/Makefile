all: proc/mosaic.jpg

raw :
	mkdir raw

proc :
	mkdir proc

raw/0001.jpg : raw
	cd raw ; wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0001.jpg

raw/0002.jpg : raw
	cd raw ; wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0002.jpg

raw/0003.jpg : raw
	cd raw ; wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0003.jpg

raw/0004.jpg : raw
	cd raw ; wget https://raw.githubusercontent.com/danielskatz/parsl-example/master/data/0004.jpg

proc/0001_sharp.jpg : raw/0001.jpg bin/sharpen_image.py
	python3 bin/sharpen_image.py raw/0001.jpg proc/0001_sharp.jpg

proc/0002_sharp.jpg : raw/0002.jpg bin/sharpen_image.py
	python3 bin/sharpen_image.py raw/0002.jpg proc/0002_sharp.jpg

proc/0003_sharp.jpg : raw/0003.jpg bin/sharpen_image.py
	python3 bin/sharpen_image.py raw/0003.jpg proc/0003_sharp.jpg

proc/0004_sharp.jpg : raw/0004.jpg bin/sharpen_image.py
	python3 bin/sharpen_image.py raw/0004.jpg proc/0004_sharp.jpg

proc/mosaic.jpg : bin/local_build_mosaic.py proc/0001_sharp.jpg proc/0002_sharp.jpg proc/0003_sharp.jpg proc/0004_sharp.jpg
	cd proc; python3 ../bin/local_build_mosaic.py 2 mosaic.jpg
