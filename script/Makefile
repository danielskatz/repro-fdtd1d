LANGUAGE=python3
FILE_NOS=0001 0002 0003 0004
RAW_FILES=$(FILE_NOS:%=raw/%.jpg)
PROC_FILES=$(FILE_NOS:%=proc/%_sharp.jpg)
SHARPEN = bin/sharpen_image.py
MOSAIC = bin/local_build_mosaic.py
RAW_SOURCE_DIR=https://raw.githubusercontent.com/danielskatz/parsl-example/master/data

.PHONY: clean all
all: proc/mosaic.jpg

clean:
	-rm -rf raw proc

raw:
	mkdir raw

proc:
	mkdir proc

$(RAW_FILES): | raw
	wget $(@:raw/%.jpg=$(RAW_SOURCE_DIR)/%.jpg) -O $@

proc/%_sharp.jpg: raw/%.jpg $(SHARPEN) | proc
	$(LANGUAGE) $(SHARPEN) $(@:proc/%_sharp.jpg=raw/%.jpg) $@

proc/mosaic.jpg: $(MOSAIC) $(PROC_FILES)
	$(LANGUAGE) $(MOSAIC) 2 $@ $(PROC_FILES)
