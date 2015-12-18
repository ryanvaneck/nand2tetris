@256
D=A
@SP
M=D
//push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop local 0        // initialize sum = 0
@SP
M=M-1
A=M
D=M
@LCL
A=M
M=D
//label LOOP_START
(LOOP_START)
//push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push local 0
@LCL
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
@SP
A=M-1
D=M
A=A-1
D=M+D
M=D
@0
M=M-1
//pop local 0	   // sum = sum + counter
@SP
M=M-1
A=M
D=M
@LCL
A=M
M=D
//push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
A=M-1
D=M
A=A-1
D=M-D
M=D
@0
M=M-1
//pop argument 0     // counter--
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
//push argument 0
@ARG
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
//if-goto LOOP_START // If counter > 0, goto LOOP_START
@SP
M=M-1
A=M
D=M
@LOOP_START
D;JGT
//push local 0
@LCL
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
