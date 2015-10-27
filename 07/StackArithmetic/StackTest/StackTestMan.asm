//push constant 17
  @17  //A=17
  D=A  //D=17
  @SP  //A=SP
  A=M  //A=M[SP]
  M=D  //M=17
  @SP  //A=SP
  M=M+1//M[SP]++

//push constant 17
  @17
  D=A  //D=17
  @SP
  A=M  //A=M[256]
  M=D  //M[256]=17
  @SP
  M=M+1//M[SP]++ M[0]=257

//eq
  //if M[SP-2] == M[SP-1]:
  //      set M[SP-2] -1
  //else:
  //      set M[SP-2] 0
  //set SP SP-2
@SP
M=M-1  // M=257
A=M    // A=257
D=M    // D=M[257] ==17
A=A-1  // A=256
D=M-D  // D = M[257] - D   17-17
@equal
D;JEQ
@notequal
D;JNE

(equal0)
@SP
M=M-1
A=M
M=-1
@SP
M=M+1
@cont0
0;JMP

(notequal0)
@SP
M=M-1
M=0
@SP
M=M+1
@cont0
0;JMP

(cont0)
//push constant 31
  @31
  D=A
  @SP
  A=M
  M=D
  @SP
  M=M+1

//push constant 53
  @53
  D=A
  @SP
  A=M
  M=D
  @SP
  M=M+1
//add
@SP
M=M-1
A=M
D=M
A=A+1
D=D+M
A=A-1
M=D
@0

