default : all

all : .base

clean :
	@make -C base clean
	@rm -rf bin

install : all
	@rm -rf bin
	@mkdir bin

.base :
	make -C base

