import matplotlib.pyplot as plt

# 引入积分算法,消除稳态误差

target=1
h = 0.2  
kp = 0.5  
ki = 0.09
leak=0.1
errors=0
z = []

for t in range(1000):	
    if h <= target:    # 目标高度为1m
        z.append(h)
        error = target - h   # 误差高度
        errors += error    # 稳态误差积分结果(离散时,积分结果即为加和)
        add = kp*error + ki*(errors)   # 加水
        print("t="+str(t))
        print("h="+str(h))
        print("error="+str(error))
        print("add="+str(add))
        print("              ")

        h = h + add - leak    # 初始高度+加水+漏水
        t = t + 1	

i = range(len(z))
plt.figure(figsize=(8,6),dpi = 80)
plt.plot(i,z,color="blue",linewidth=1.0,linestyle="-")
plt.show()

