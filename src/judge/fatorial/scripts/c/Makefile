SRC=$(wildcard *.c)
CFLAGS=-lm -O2 -static

main: ${SRC}
	gcc ${CFLAGS} $^ -o $@ -lm
	@echo BIN=$@

