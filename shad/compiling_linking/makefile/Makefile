all: hello

hello: main.o hello.o factorial.o
	g++ main.o hello.o factorial.o -o hello
main.o: main.cpp
	g++ -c main.cpp
hello.o: hello.cpp
	g++ -c hello.cpp
factorial.o: factorial.cpp
	g++ -c factorial.cpp
clean:
	rm -rf *o