default : all

all : .base .train .calc_auc

clean :
	@make -C base clean
	@make -C train clean
	@make -C calc_auc clean
	@rm -rf bin

install : all
	@rm -rf bin
	@mkdir bin

.base :
	make -C base

.train :
	make -C train

.calc_auc :
	make -C calc_auc
