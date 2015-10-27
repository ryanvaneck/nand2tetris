(CHECK)

  @count //reset count
  M=0

  @24576
  D=M
  @WHITE
  D;JEQ //if D==0 goto WHITE
  @BLACK
  D;JNE //if D>0 goto BLACK

  @CHECK
  0;JMP

(WHITE)

  @SCREEN
  M=0 // set M[16384] to 0
  @SCREEN
  D=A  // set D to 16384

  @count
  A=M+D
  M=0

  @count  // increment count by 1
  M=M+1

  @24576
  D=M
  @BLACK
  D;JNE

  @8191
  D=A
  @count
  D=D-M
  @CHECK
  D;JLT

  @WHITE
  0;JMP

(BLACK)
  @SCREEN
  M=-1 // set M[16384] to -1
  @SCREEN
  D=A  // set D to 16384

  @count
  A=M+D
  M=-1

  @count  // increment count by 1
  M=M+1

  @8191
  D=A
  @count
  D=D-M
  @CHECK
  D;JLT

  @BLACK  //else goto BLACK
  0;JMP
