.PHONY: all preproc wav2agb midi2agb install git_update

all: preproc wav2agb midi2agb
	@printf "[\e[1;32mBuilding Succeeded\e[0m]\n"

git_update:
	@printf "[\e[1;36mLoading Updates\e[0m]\n"
	git submodule update --recursive --init

preproc wav2agb midi2agb: git_update
	# tools to be built with regular makefiles
	make -C $@


install: all
ifeq ($(shell uname -o),GNU/Linux)
	cp preproc/preproc /usr/local/bin
	cp wav2agb/wav2agb /usr/local/bin
	cp midi2agb/midi2agb /usr/local/bin
else ifeq ($(shell uname -o),Cygwin)
	cp preproc/preproc.exe /usr/local/bin
	cp wav2agb/wav2agb.exe /usr/local/bin
	cp midi2agb/midi2agb.exe /usr/local/bin
else
	$(error "Unsupported platform: $(sheel uname -o)")
endif
	@printf "[\e[1;32mInstallation Succeeded\e[0m]\n"
