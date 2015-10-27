for i in range(16):
    print "And(a=a["+str(i)+"], b=notsel, out=w"+str(i)+"1);"
    print "And(a=sel, b=b["+str(i)+"], out=w"+str(i)+"2);"
    print "Or(a=w"+str(i)+"1, b=w"+str(i)+"2, out=out["+str(i)+"]);"
