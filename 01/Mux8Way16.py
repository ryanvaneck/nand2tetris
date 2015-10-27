for bus in ['a','b','c','d', 'e', 'f', 'g', 'h']:
    for i in range(16):
        ind = str(i)
        if bus == 'a':
            s1 = 'notsel0';
            s2 = 'notsel1';
            s3 = 'notsel2';
        elif bus == 'e':
            s1 = 'notsel0';
            s2 = 'notsel1';
            s3 = 'sel[2]';
        elif bus == 'c':
            s1 = 'notsel0';
            s2 = 'sel[1]';
            s3 = 'notsel2'
        elif bus == 'g':
            s1 = 'notsel0';
            s2 = 'sel[1]';
            s3 = 'sel[2]';
        elif bus == 'b':
            s1 = 'sel[0]';
            s2 = 'notsel1';
            s3 = 'notsel2';
        elif bus == 'f':
            s1 = 'sel[0]';
            s2 = 'notsel1';
            s3 = 'sel[2]';
        elif bus == 'd':
            s1 = 'sel[0]';
            s2 = 'sel[1]';
            s3 = 'notsel2';
        elif bus == 'h':
            s1 = 'sel[0]';
            s2 = 'sel[1]';
            s3 = 'sel[2]';

        print "And(a=" + bus + "[" + ind + "], b=" + s1 + ", out=w"+ bus + ind + ");"
        print "And(a=w" + bus + ind + ", b=" + s2 + ", out=x" + bus + ind + ");"
        print "And(a=x" + bus + ind + ", b=" + s3 + ", out=y" + bus + ind + ");"

print

for i in range(16):
    ind = str(i)
    print "Or(a=ya" + ind + ", b=yb" + ind + ", out=ab" + ind + ");"
    print "Or(a=ab" + ind + ", b=yc" + ind + ", out=abc" + ind + ");"
    print "Or(a=abc" + ind + ", b=yd" + ind + ", out=abcd" + ind + ");"
    print "Or(a=abcd" + ind + ", b=ye" + ind + ", out=abcde" + ind + ");"
    print "Or(a=abcde" + ind + ", b=yf" + ind + ", out=abcdef" + ind + ");"
    print "Or(a=abcdef" + ind + ", b=yg" + ind + ", out=abcdefg" + ind + ");"
    print "Or(a=abcdefg" + ind + ", b=yh" + ind + ", out=out[" + ind + "]);"


