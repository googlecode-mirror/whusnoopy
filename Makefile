default : all

all : .base .dospy

clean :
	@make -C base clean
	@make -C dospy clean
	@rm -rf bin

install : all
	@rm -rf bin
	@mkdir bin

.base :
	make -C base

.dospy : 
	make -C dospy
