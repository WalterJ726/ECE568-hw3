CFLAGS=-std=gnu++11 -ggdb3 
PROGS=main


all: $(PROGS)
main:main.cpp sha256.cpp sha256.h
	g++ $(CFLAGS) -o main main.cpp sha256.cpp
clean:
	rm -rf *.o main