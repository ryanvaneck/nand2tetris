#!/usr/bin/python
import re
import sys

Acommand = 'A';
Ccommand = 'C';
Lcommand = 'L';

class Code(object):

    dests = {
              '':'000',
              'M':'001',
              'D':'010',
              'MD':'011',
              'A':'100',
              'AM':'101',
              'AD':'110',
              'AMD':'111'
    }

    comps = {
                '0':  '101010',
                '1':  '111111',
                '-1': '111010',
                'D':  '001100',
                'A':  '110000',
                '!D': '001101',
                '!A': '110001',
                '-D': '001111',
                '-A': '110011',
                'D+1':'011111',
                'A+1':'110111',
                'D-1':'001110',
                'A-1':'110010',
                'D+A':'000010',
                'D-A':'010011',
                'A-D':'000111',
                'D&A':'000000',
                'D|A':'010101',
                'M':  '110000',
                '!M': '110001',
                '-M': '110011',
                'M+1':'110111',
                'M-1':'110010',
                'D+M':'000010',
                'D-M':'010011',
                'M-D':'000111',
                'D&M':'000000',
                'D|M':'010101'
    }

    jumps = {
                   '':'000',
                'JGT':'001',
                'JEQ':'010',
                'JGE':'011',
                'JLT':'100',
                'JNE':'101',
                'JLE':'110',
                'JMP':'111'
    }

    def dest(mnemonic):
        return dests[mnemonic]

    def comp(mnemonic):
        return comps[mnemonic]

    def jump(mnemonic):
        return jumps[mnemonic]

def getCommandType(command):
    if command[0] == "@":
        return Acommand
    p = re.compile('[0,D];[A-Z]{3}');
    if p.match(command):
        return Ccommand
    if "=" in command or "+" in command:
        return Ccommand
    if re.compile('\(.*\)').match(command):
        return Lcommand

def getDest(command):
    #dest=comp;jump
    if '=' in command:
        equals_index = command.index('=')
        return command[:equals_index]
    return ''
#dest=comp;jump

def getComp(command):
    if '=' in command:
        ##print current_command
        m = re.match("[ADM]+\=([0-9|&ADM+!-]+)", command)
        ##print m
        ##print m.group(1)
        return m.group(1)
        #return current_command[equals_index + 1 : ]
    if ';' in command:
        m = re.match('([0D]);[A-Z]{3}', command).group(1)
        return m
        #return current_command[:current_command.index(';')]
    return ''

def getJump(command):
    if ';' in command:
        m = re.match('[0D];([0-9A-Z]+)', command).group(1)
        ##print m
        return m
    return ''

def buildST(asmFile):
    result = {'SP':0, 'LCL':1, 'ARG':2, 'THIS':3, 'THAT':4, 'SCREEN':16384,'KBD':24576, 'R0':0,  'R1':1,  'R2':2,  'R3':3,  'R4':4,  'R5':5,  'R6':6,  'R7':7,  'R8':8,  'R9':9,  'R10':10,  'R11':11,  'R12':12,  'R13':13,  'R14':14, 'R15':15}
    commandLine = 0
    for line in asmFile:
        m = re.match("\((.*)\)", line)
        if m:
            result[m.group(1)] = commandLine
        else:
            stripped = line.strip()
            if len(stripped) > 0 and stripped[0] != '/':
                commandLine += 1
    #print result
    return result

def translateFromSymbolToValue(command, st, nextAddress):
    m = re.match("@([0-9]+).*", command.strip())
    if m: #line is in form: @{number}
        return (m.group(1), nextAddress)
    else:
        m = re.match("@(.*)", command.strip())
        if m and m.group(1) in st:
            # line is in form @{symbol} and symbol was found in table
            return (st[m.group(1)], nextAddress)
        elif m:
            #print("line is in form @symbol but symbol not found in table")
            #print command + '#'
            nextAddress += 1
            st[m.group(1)] = nextAddress
            #print "assigning " + m.group(1) + " to address " + str(nextAddress)
            return (nextAddress, nextAddress)

class main(object):

    def __init__(self):
        pass

    filename = sys.argv[1]
    asmFile = file(filename, 'r')
    code = Code()
    words = []
    hackfilename = re.match("(.*)\.asm", filename).group(1) + ".hack"
    hack = file(hackfilename,'w')

    st = buildST((file(filename)))
    nextAddress = 15

    lineNum = 1
    for line in asmFile:
        #print
        line = line.strip()
        if (line != '' and line[0] != '/'):
            #print "processing line number:" + str(lineNum)
            commandType = getCommandType(line)
            result = ''
            #print "#######command: " + line  + "        commandType: " + str(commandType)

            if commandType == Acommand:

                (translated, nextAddress) = translateFromSymbolToValue(line, st, nextAddress)
                #print 'translated:' +  str(translated)
                result = '0' + '{:015b}'.format(int(translated))
                #print 'result:' + str(result)
                words.append(result)
            elif commandType == Ccommand:

                destPart = getDest(line)
                compPart = getComp(line)
                jumpPart = getJump(line)

                a = '0'
                if 'M' in compPart:
                    a = '1'

                #print "a:"+a,

                #print " dest:" + destPart,
                #print " comp:" + compPart,
                #print " jump:" + jumpPart

                result = '111' + a + code.comps[compPart] + code.dests[destPart] + code.jumps[jumpPart]
                #print "result:" + result
                words.append(result)
            if line[0] != '(':
                lineNum += 1



    for line in words:
        pass
        ##print line
    for item in words:
        if item != '':
            #print>>hack, item


main()
