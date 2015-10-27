// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.


@i
M=0 // set i to 0
@sum
M=0 // set sum to 0

@0
D=M   //set D to R0
@END
D;JEQ //if R0==0 goto END
@1
D=M   //set D to R1
@END
D;JEQ //if R1==0 goto END

(LOOP)
  @0
  D=M // D=R0
  @sum
  M=D+M // sum = sum + R0
  @i
  M=M+1 // i=i+1
  @i
  D=M // D=i
  @1
  D=M-D // D=i-R1
  @END
  D;JEQ // if (R1-i) == 0 goto END
  @LOOP
  0;JMP
(END)
  @test
  M=1
  @sum
  D=M // D = sum
  @2
  M=D // R2 = D
  @END
  0;JMP
