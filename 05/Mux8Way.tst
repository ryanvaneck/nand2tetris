// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/01/DMux8Way.tst

load Mux8Way.hdl,
output-file Mux8Way.out,
//compare-to Mux8Way.cmp,
output-list sel%B2.3.2 a%B2.1.2 b%B2.1.2 c%B2.1.2 d%B2.1.2 e%B2.1.2 f%B2.1.2 g%B2.1.2 h%B2.1.2;

set b 1,
set sel %B000,
eval,
output;

set b 1,
set sel %B001,
eval,
output;
set a 0,
set sel %B000,
eval,
output;
set h 1,
set sel %B111,
eval,
output;
