CC=gcc
CFLAGS=-g -Wall
SRCDIR=src/
INCLUDEDIR=include/
BINDIR=bin/
OUT=executable.out
REMOVE=rm -rf

all:
	$(CC) $(CFLAGS) $(SRCDIR)*.c -I$(INCLUDEDIR) -o $(BINDIR)$(OUT)

clean:
	$(REMOVE) $(BINDIR)*
