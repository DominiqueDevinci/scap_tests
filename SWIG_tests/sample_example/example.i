/* File: example.i 
The python binding is defined here
*/

%module example

%{

/* The #define SWIG_FILE_WITH_INIT line inserts a macro that specifies that the resulting C file should be built as a python extension, inserting the module init code. */

#define SWIG_FILE_WITH_INIT
#include "example.h"

%}

int fact(int n);
