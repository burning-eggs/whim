# whim

 Stack based programming language inspired by Forth.
 
 **QUICK DISCLAIMER: COMPILING .whm FILES CURRENTLY DOESNT WORK ON WINDOWS.** 

 Whim is planned to be
 - [x] Compiled
 - [x] Native
 - [x] Stack-Based
 - [ ] Turing-Complete
 - [ ] Statically Typed
 - [ ] Self-Hosted

## Example

 Simple program that prints numbers from 10 to 1 in descending order:

 ```whim
 10 while dup 0 > do
     dup .
    1 -
 end
 ```

## Quick Start

### Simulation

 Simulating a `.whm` simply interprets the program.

 ```console
 $ ./whim.py sim program.whm
 ```

### Compiling

 Compiling a `.whm` file generates assembly code and compiles it with [nasm](https://www.nasm.us).

 ```console
 $ ./whim.py com program.whm
 $ ./program.asm
 ```

## Badges

 [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
