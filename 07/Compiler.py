import re, sys, os

C_ARTH = "arth"
A_EQ = 'eq'
A_GT = 'gt'
A_LT = 'lt'
A_ADD = 'add'
A_SUB = 'sub'
A_NEG = 'neg'
A_AND = 'and'
A_OR = 'or'
A_NOT = 'not'
ARTH_COMMANDS = [A_EQ, A_GT, A_LT, A_ADD, A_SUB, A_NEG, A_AND, A_OR, A_NOT]

C_PUSH = 'push'
C_POP =  'pop'

C_LABEL =     'label'
C_GOTO =      'goto'
C_IF =   'if-goto'
C_FUNCTION =  'function'
C_RETURN =    'return'
C_CALL =      'call'

SEG_CONST = 'constant'
SEG_LOCAL = 'local'
SEG_ARG = 'argument'
SEG_THIS = 'this'
SEG_THAT = 'that'
SEG_TEMP = 'temp'
SEG_POINTER = 'pointer'
SEG_STATIC = 'static'

arthToJumps = {
        A_EQ : ("D;JEQ","D;JNE"),
        A_LT : ("D;JLT","D;JGE"),
        A_GT : ("D;JGT","D;JLE")
}
arthToOperators = {
        A_ADD : "+",
        A_SUB : "-",
        A_OR  : "|",
        A_AND : "&"
}
segmentToKeyword = {
        SEG_LOCAL : "LCL",
        SEG_ARG : "ARG",
        SEG_THIS : "THIS",
        SEG_THAT : "THAT"
}


compJumpCount = 0
contJumpCount = 0
def getValidCommand(line):
    stripped = line.strip()
    if stripped[0:2] == "//" or stripped == "":
        return None
    else:
        return stripped

def getCommandType(command):
    firstWord = re.match("(\w+)",command).groups(1)[0]
    if firstWord in ARTH_COMMANDS:
        return C_ARTH
    return firstWord


def getArg1(command):
    return re.findall("(\w+)", command)[1]

def getArg2(command):
    arg = re.findall("(\w+)", command)[2]
    if arg:
        return int(arg)

def getNextCompJump():
    global compJumpCount
    compJumpCount += 1
    return "comp" + str(compJumpCount)

def getNextContJump():
    global contJumpCount
    contJumpCount += 1
    return 'cont' + str(contJumpCount)

def translateArth(command, commandType):
    result = []
    if commandType == C_ARTH:
        verb = re.match("(\w+)", command).groups(1)[0]
        if verb in [A_EQ,A_LT,A_GT]:
            result = ['@SP','M=M-1','A=M','D=M','A=A-1','D=M-D']
            pos = getNextCompJump()
            result.append('@'+ pos)
            result.append(arthToJumps[verb][0])
            neg = getNextCompJump()
            result.append('@' + neg)
            result.append(arthToJumps[verb][1])

            result.append("")
            result.append('(' + pos + ')')
            contJump = getNextContJump()
            result += ['@SP', 'M=M-1', 'A=M','M=-1', '@SP','M=M+1', '@'+contJump, '0;JMP']

            result.append("")
            result.append('(' + neg + ')')
            result += ['@SP','M=M-1', 'A=M', 'M=0','@SP','M=M+1', '@'+contJump, '0;JMP']

            result.append("")
            result.append('(' + contJump + ')')

        elif verb in [A_ADD,A_SUB,A_AND,A_OR]:
            result += ['@SP', 'A=M-1', 'D=M', 'A=A-1']
            result.append("D=M" + arthToOperators[verb] + 'D')
            result += ['M=D', '@0', 'M=M-1']

        elif verb in [A_NEG,A_NOT]:
            result += ['@SP', 'M=M-1', 'A=M','D=M']
            result.append('D=' +  ("-" if verb == A_NEG else "!") + 'D')
            result += ['M=D', '@0', 'M=M+1']

    return result

def translatePushPop(commandType, segment, index, stripped_filename):
    result = []
    if commandType == C_PUSH:

        if segment == SEG_CONST:
            result.append("@"+ str(index))
            result.append('D=A')
            result += ['@SP','A=M','M=D','@SP','M=M+1']

        elif segment in [SEG_LOCAL, SEG_ARG, SEG_THIS, SEG_THAT]:
            #take indexth from seg and push it onto stack
            result.append('@' + segmentToKeyword[segment])
            result.append('A=M')
            for i in range(index):
                result.append('A=A+1')
            result.append('D=M')
            result += ['@SP','A=M','M=D','@SP','M=M+1']

        elif segment == SEG_TEMP: #push temp x
            result.append(translateSegment(segment, index))
            result.append('D=M')
            result += ['@SP','A=M','M=D','@SP','M=M+1']

        elif segment == SEG_POINTER:
            result.append('@'+str(3+index))
            result.append('D=M')
            result += ['@SP','A=M','M=D','@SP','M=M+1']

        elif segment == SEG_STATIC:
            result.append(translateSegment(segment, index, stripped_filename))
            result.append('D=M')
            result += ['@SP','A=M','M=D','@SP','M=M+1']

        elif segment == C_LABEL:
            pass
        elif segment == C_GOTO:
            pass
        elif segment == C_IF:
            pass


    else: #POP
        result += ['@SP','M=M-1','A=M','D=M']
        result.append(translateSegment(segment, index, stripped_filename))
        if segment not in [SEG_TEMP, SEG_POINTER, SEG_STATIC]:
            result.append('A=M')
            for i in range(index):
                result.append('A=A+1')
        result.append('M=D')

    return result

def translateSegment(segment, index, stripped_filename):
    if segment == SEG_TEMP:
        return '@' + str(5 + index)
    elif segment == SEG_POINTER:
        return '@' + str(3 + index)
    elif segment == SEG_STATIC:
        return '@' + stripped_filename + '.' + str(16+index)
    else:
        return '@' + segmentToKeyword[segment]

def getVMPaths(path):
    vm_paths = []
    paths = [os.path.join(path,fn) for fn in next(os.walk(path))[2]]
    for p in paths:
        if re.match(".*\.vm",p):
            vm_paths.append(p)
    return vm_paths

def getStrippedFilename(filename):
    result = ''
    reversed = filename[::-1]
    if reversed[0] == "/":
        reversed = reversed[:-1]
        result = re.findall("([^/]+)", reversed)[0][::-1]
    elif "." in reversed:
        reversed = re.findall("([^/]+)", reversed)[1]
        result = reversed[::-1]
    else:
        result = re.findall("([^/]+)", reversed)[0][::-1]
    print "stripped_filename: " + result
    return result

def main(filenameOrDir):
    if filenameOrDir[-3:] != ".vm":
        vm_paths = getVMPaths(filenameOrDir)
    else:
        vm_paths = [filenameOrDir]
    if vm_paths == []:
        print "invalid input: " + filenameOrDir
        return
    stripped_filename = getStrippedFilename(vm_paths[0])
    asm_filename = stripped_filename + '.asm'
    print asm_filename
    asm = file(asm_filename, 'w')
    result = []

    for vm_file in vm_paths:
        for line in file(vm_file, 'r'):
            validCommand = getValidCommand(line)

            if validCommand:
                result.append("//" + validCommand)
                commandType = getCommandType(validCommand)

                if commandType == C_ARTH:
                    result += translateArth(validCommand, commandType)

                if commandType in [C_PUSH,C_POP]:
                    result += translatePushPop(commandType, getArg1(validCommand), getArg2(validCommand), stripped_filename)

    for item in result:
        print>>asm, item


main(sys.argv[1])
