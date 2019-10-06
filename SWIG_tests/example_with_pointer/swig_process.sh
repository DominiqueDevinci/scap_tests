swig -python example.i
gcc -O2 -fPIC -c example.c
gcc -O2 -fPIC -c example_wrap.c -I/usr/include/python3.6
gcc -shared example.o example_wrap.o -o _example.so
