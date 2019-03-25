import matplotlib.pyplot as plt
import networks as nw


"""
x3,y3,ytho3 = nw.baplotter("ba_3_10000.txt",3)

x9,y9,ytho9 = nw.baplotter("ba_9_10000.txt",9)
x27,y27,ytho27 = nw.baplotter("ba_27_10000.txt",27)
x81,y81,ytho81 = nw.baplotter("ba_81_10000.txt",81)
x243,y243,ytho243 = nw.baplotter("ba_243_1000.txt",243)
x729,y729,ytho729 = nw.baplotter("ba_729_1000.txt",729)

"""
x1,y1,ytheo1 = nw.baplotter("ba_1_10000.txt",3)
x3,y3,ytho3 = nw.baplotter("ba_3_10000.txt",3)
x9,y9,ytho9 = nw.baplotter("ba_9_10000.txt",9)
x27,y27,ytho27 = nw.baplotter("ba_27_10000.txt",27)
x81,y81,ytho81 = nw.baplotter("ba_81_10000.txt",81)
x243,y243,ytho243 = nw.baplotter("ba_243_1000.txt",243)
x729,y729,ytho729 = nw.baplotter("ba_729_1000.txt",729)

plt.scatter(x1,y1, s= 1, label = "m = 1")
plt.scatter(x3,y3,s=1,label= "m = 3",)
#plt.scatter(x3,ytho3, s = 5)
plt.scatter(x9,y9,s=1, label = "m = 9")
#plt.scatter(x9,ytho9, s = 1,)
plt.scatter(x27,y27,s=1,label = "m = 27")
#plt.scatter(x27,ytho27, s = 1, )
plt.scatter(x81,y81,s=1,label = "m = 81")
#plt.scatter(x81,ytho81, s = 1, )
plt.scatter(x243,y243,s=1,label = "m = 243")
#plt.scatter(x243,ytho243, s = 1, )
plt.scatter(x729,y729,s=1,label = "m = 729")
#plt.scatter(x729,ytho729, s = 1, )
plt.xlabel("$log(k)$",fontsize = 12)
plt.ylabel("$log(p(k)$", fontsize = 12)
plt.legend()
plt.grid()
plt.savefig("nologbin_ba.png")
plt.show()

