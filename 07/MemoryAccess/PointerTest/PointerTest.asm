@SP
M=256
@1
M=300
@2
M=400
@3
M=3000
@4
M=3010
//push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@SP
M=M-1
A=M
D=M
@3
M=D
//push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@SP
M=M-1
A=M
D=M
@4
M=D
//push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop this 2
@SP
M=M-1
A=M
D=M
@THIS
A=M
A=A+1
A=A+1
M=D
//push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 6
@SP
M=M-1
A=M
D=M
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
M=D
//push pointer 0
@3
D=M
@SP
A=M
M=D
@SP
M=M+1
//push pointer 1
@4
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
//push this 2
@THIS
A=M
A=A+1
A=A+1
D=M
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
//push that 6
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
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
