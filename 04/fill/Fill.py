
print """(CHECK)

  @24576
  D=M
  @WHITE
  D;JEQ //if D==0 goto WHITE
  @BLACK
  D;JGT //if D>0 goto BLACK

(WHITE)"""

for i in range(1):#(16384, 147457, 1):
    print "  @"+str(i)+"\n  M=0"
print "  @CHECK"
print "  0;JMP"

print 

print "(BLACK)"

for i in range(1):#(16384, 147457, 1):
    print "  @"+str(i)+"\n  M=-1"

print "  @CHECK"
print "  0;JMP"

