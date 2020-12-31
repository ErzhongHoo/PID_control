import matplotlib.pyplot as plt


h = 0.2    # 初始水位高度
kp = 0.5
z = []

for t in range(100):	
    if h <= 1:    # 目标高度为1m
        z.append(h)
        error = 1 - h    # 误差高度
        extra = kp*error    # 误差后加水
        print("t="+str(t))
        print("h="+str(h))
        print("error="+str(error))
        print("extra="+str(extra))
        print("              ")

        h = h + extra    
        t = t + 1	

i = range(len(z))
plt.figure(figsize=(8,6),dpi = 80)
plt.plot(i,z,color="blue",linewidth=1.0,linestyle="-")
plt.show()
