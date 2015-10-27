for bus in ['a','b','c','d']:
    for i in range(16):
        if bus == 'a':
            s1 = 'notsel0';
            s2 = 'notsel1';
        elif bus == 'c':
            s1 = 'notsel0';
            s2 = 'sel[1]';
        elif bus == 'b':
            s1 = 'sel[0]';
            s2 = 'notsel1';
        elif bus == 'd':
            s1 = 'sel[0]';
            s2 = 'sel[1]';

        print "And(a=" + bus + "[" + str(i) + "], b=" + s1 + ", out=w"+ bus + str(i) + ");"
        print "And(a=w" + bus + str(i) + ", b=" + s2 + ", out=x" + bus + str(i) + ");\n"

print

for i in range(16):
    print "Or(a=xa" + str(i) + ", b=xb" + str(i) + ", out=y" + str(i) + ");"
    print "Or(a=y" + str(i) + ", b=xc" + str(i) + ", out=z" + str(i) + ");"
    print "Or(a=xd" + str(i) + ", b=z" + str(i) + ", out=out[" + str(i) + "]);"


