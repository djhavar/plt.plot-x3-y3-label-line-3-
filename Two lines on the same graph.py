import matplotlib.pyplot as plt

x1 = [1,2,3,4]
y1 = [2,4,1,4]

plt.plot(x1,y1,label="line 1")

x2 = [1,2,3,4]
y2 = [1,1,3,4]

plt.plot(x2,y2,label="line 2")


x3 = [1,2,3,4]
y3 = [1,4,2,4]

plt.plot(x3,y3,label="line 3")

x4 = [1,2,4]
y4 = [1,3,4]

plt.plot(x4,y4,label="line 4")

plt.xlabel('x-axis')


plt.ylabel('y-axis')

plt.title('four lines on same graph')

plt.legend()

plt.show()