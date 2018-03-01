.PHONY: all bin2asm csmidi midfix4agb preproc wav2agb install

all: bin2asm csmidi midfix4agb preproc wav2agb
	@echo "*** Building Succeeded ***"

bin2asm preproc wav2agb:
	# tools to be built with regular makefiles
	make -C $@


csmidi midfix4agb:
ifeq ($(shell uname -o),GNU/Linux)
	xbuild /p:Configuration=Release $@/$@.sln
else ifeq ($(shell uname -o),Cygwin)
	devenv /build release $@/$@.sln
else
	$(error "Unsupported platform: $(shell uname -o)")
endif

install:
ifeq ($(shell uname -o),GNU/Linux)
	cp bin2asm/bin2asm /usr/local/bin
	cp preproc/preproc /usr/local/bin
	cp wav2agb/wav2agb /usr/local/bin

	cp csmidi/csmidi/bin/Release/csmidi.dll /usr/lib
	cp midfix4agb/midfix4agb/bin/Release/midfix4agb.exe /usr/local/share
	printf '#!/bin/sh\nmono /usr/local/share/midfix4agb.exe "$$@"\n' > /usr/local/bin/midfix4agb
	chmod +x /usr/local/bin/midfix4agb

	cp mid2agb/mid2agb.exe /usr/local/share
	printf '#!/bin/sh\nwine /usr/local/share/mid2agb.exe "$$@"\n' > /usr/local/bin/mid2agb
	chmod +x /usr/local/bin/mid2agb
else ifeq ($(shell uname -o),Cygwin)
	cp bin2asm/bin2asm.exe /usr/local/bin
	cp preproc/preproc.exe /usr/local/bin
	cp wav2agb/wav2agb.exe /usr/local/bin

	cp csmidi/csmidi/bin/Release/csmidi.dll /usr/lib
	cp midfix4agb/midfix4agb/bin/Release/midfix4agb.exe /usr/local/bin
	cp mid2agb/mid2agb.exe /usr/local/bin
else
	$(error "Unsupported platform: $(sheel uname -o)")
endif
