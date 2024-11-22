import matplotlib.pyplot as plt 
import numpy as np 
h = 1
A = .095
m=1.5
c=4186

k=h*A/(m*c)

x = np.linspace(0,4000, 1000)
def T(x):
    return 40*np.e**(-k*x)-18
x_minutes = x / 60
y=[]
for i in range(len(x)):
    y.append(T(i))
i=0
import matplotlib.pyplot as plt 
import numpy as np 


h = 10 
A = 0.095  
m = 1.5  
c = 4186  


k = h * A / (m * c)


x = np.linspace(0, 4000, 6000)  


def T(x):
    return 40 * np.e**(-k * x) - 18


x_minutes = x / 60  


y = T(x)


plt.plot(x_minutes, y)
plt.xlabel("Time (minutes)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Change Over Time")
plt.grid(True)
plt.show()
