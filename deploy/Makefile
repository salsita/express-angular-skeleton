.PHONY: deps test

DAEMONIZE=0

deps: TARGET=./targets/deps/go
deps:
	@echo ">>> Installing dependencies"; \
	if [ -x "${TARGET}" ]; then "${TARGET}"; fi

build: TARGET=./targets/build/go
build: deps
	@echo ">>> Building the app"; \
	if [ -x "${TARGET}" ]; then "${TARGET}"; fi

test: TARGET=./targets/test/go
test: DAEMONIZE=1
test: build
	@echo ">>> Running tests"; \
	if [ -x "${TARGET}" ]; then "${TARGET}"; fi

run: TARGET=./targets/run/go
run:
	@echo ">>> Starting the application"; \
	if [ -x "${TARGET}" ]; then "${TARGET}"; fi
