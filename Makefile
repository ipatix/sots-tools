.PHONY: all bin2asm csmidi midfix4agb preproc wav2agb install

all: bin2asm csmidi midfix4agb preproc wav2agb
	@echo "*** Building Succeeded ***"

bin2asm preproc wav2agb midi2agb:
	# tools to be built with regular makefiles
	make -C $@


install:
ifeq ($(shell uname -o),GNU/Linux)
	cp bin2asm/bin2asm /usr/local/bin
	cp preproc/preproc /usr/local/bin
	cp wav2agb/wav2agb /usr/local/bin
	cp midi2agb/midi2agb /usr/local/bin
else ifeq ($(shell uname -o),Cygwin)
	cp bin2asm/bin2asm.exe /usr/local/bin
	cp preproc/preproc.exe /usr/local/bin
	cp wav2agb/wav2agb.exe /usr/local/bin
	cp midi2agb/midi2agb.exe /usr/local/bin
else
	$(error "Unsupported platform: $(sheel uname -o)")
endif
