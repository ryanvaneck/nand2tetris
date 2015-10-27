#for i in range(16):
#    print "And(a=notzx, b=x["+str(i)+"], out=xb"+str(i)+");"
#print

#for i in range(16):
#    print "And(a=notzy, b=y["+str(i)+"], out=yb"+str(i)+");"
#print

print "Not(in=zy, out=notzy);"
print "Not(in=zx, out=notzx);"

print "And16(",
for i in range(16):
    print "a["+str(i)+"]=notzx, b["+str(i)+"]=x["+str(i)+"],",
print "out=xa);"
print

print "And16(",
for i in range(16):
    print "a["+str(i)+"]=notzy, b["+str(i)+"]=y["+str(i)+"],",
print "out=ya);"
print

print "Not16(in=xa, out=notxa);"
print "Not16(in=ya, out=notya);"


print "Mux16(a=xa, b=notxa, sel=nx, out=xb);"
print "Mux16(a=ya, b=notya, sel=ny, out=yb);"

print "Add16(a=xb, b=yb, out=addC);"
print "And16(a=xb, b=yb, out=andC);"

print "Mux16(a=addC, b=andC, sel=f, out=d);"

print "Not16(in=d, out=notd);";

print "Mux16(a=d, b=notd, sel=no, out=out);"

print "Or8Way(in[0..7]=out[0..7], out=zra);"
print "Or8Way(in[8..15]=out[8..15], out=zrb);"
print "Or(a=zra, b=zrb, out=zr);"

"""
print "Or8Way(",
for i in range(8):
    print "in["+str(i)+"]=out["+str(i)+"],",
print "out=zra);"
print "Or8Way(",
for i in range(7,15):
    print "in["+str(i)+"]=out["+str(i)+"],",
print "out=zrb);"
"""

print "And(a=true, b=out[15], out=ng);"

"""
for i in range(16):
    print "Not(in=xb"+str(i)+", out=notxb"+str(i)+");"
print

for i in range(16):
    print "Not(in=yb"+str(i)+", out=notyb"+str(i)+");"
print

for i in range(16):
    print "Mux(a=xb"+str(i)+", b=notxb"+str(i)+", sel=nx, out=xc"+str(i)+");"
print

for i in range(16):
    print "Mux(a=yb"+str(i)+", b=notyb"+str(i)+", sel=ny, out=yc"+str(i)+");"
print

print "Add16(",
for i in range(16):
    print "a["+str(i)+"]=xc"+str(i)+", ",
    print "b["+str(i)+"]=yc"+str(i)+", ",
print "out=addD);"

for i in range(16):
    print "Mux(a=addD"+str(i)+", b=andD"+str(i)+", sel=f, out=out1-"+str(i)+");"
print

for i in range(16):
    print "Not16(in=out1-"+str(i)+", out=notout1-"+str(i)+");"
print

for i in range(16):
    print "Mux(a=out1-"+str(i)+", b=notout1-"+str(i)+", sel=no, out=out["+str(i)+"]);"
print 

print "And(a=out[0], b=true, out=ng);"

print "Or16(a=out, b[0..16]=false, out=zr);"


165   Add(a=xc0, b=yc0, out=addD0);
166   Add(a=xc1, b=yc1, out=addD1);
167   Add(a=xc2, b=yc2, out=addD2);
168   Add(a=xc3, b=yc3, out=addD3);
169   Add(a=xc4, b=yc4, out=addD4);
170   Add(a=xc5, b=yc5, out=addD5);
171   Add(a=xc6, b=yc6, out=addD6);
172   Add(a=xc7, b=yc7, out=addD7);
173   Add(a=xc8, b=yc8, out=addD8);
174   Add(a=xc9, b=yc9, out=addD9);
175   Add(a=xc10, b=yc10, out=addD10);
176   Add(a=xc11, b=yc11, out=addD11);
177   Add(a=xc12, b=yc12, out=addD12);
178   Add(a=xc13, b=yc13, out=addD13);
179   Add(a=xc14, b=yc14, out=addD14);
180   Add(a=xc15, b=yc15, out=addD15);
181
182 //  And16(a=xc, b=yc, out=andD);
183
184   Add(a=xc0, b=yc0, out=andD0);
185   Add(a=xc1, b=yc1, out=andD1);
186   Add(a=xc2, b=yc2, out=andD2);
187   Add(a=xc3, b=yc3, out=andD3);
188   Add(a=xc4, b=yc4, out=andD4);
189   Add(a=xc5, b=yc5, out=andD5);
190   Add(a=xc6, b=yc6, out=andD6);
191   Add(a=xc7, b=yc7, out=andD7);
192   Add(a=xc8, b=yc8, out=andD8);
193   Add(a=xc9, b=yc9, out=andD9);
194   Add(a=xc10, b=yc10, out=andD10);
195   Add(a=xc11, b=yc11, out=andD11);
196   Add(a=xc12, b=yc12, out=andD12);
197   Add(a=xc13, b=yc13, out=andD13);
198   Add(a=xc14, b=yc14, out=andD14);
199   Add(a=xc15, b=yc15, out=andD15);
"""
