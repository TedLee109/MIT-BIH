import matplotlib.pyplot as plt
import numpy as np

def turn_byte(a):
    for i in range(8-len(a)):
        a = '0' + a
    return(a)

f = open('210.dat','rb').read()
cha=[]
for i in range(300,3000,3):
    a1, a2, a3 = bin(f[i]), bin(f[i+1]), bin(f[i+2])
    a1, a2, a3 = a1[2:], a2[2:], a3[2:]
    a1, a2, a3 = turn_byte(a1), turn_byte(a2), turn_byte(a3)
    channel_1=a2[4:]+a1[:4]+a1[4:]
    channel_2 = a2[:4]+a3[:4]+a3[4:]
    cha.append([int(channel_1,2), int(channel_2,2)])

cha = np.array(cha)

plt.figure(figsize=(12,8))

plt.subplot(2,1,1)
plt.title('channel_1')
plt.grid(b=True,which='major',color='#ff0000',linestyle='-')
plt.minorticks_on()
plt.grid(b=True,which='minor',color='#ff0000',linestyle='-')
plt.plot(cha[:,0])

plt.subplot(2,1,2)
plt.title('channel_2')
plt.grid(b=True,which='major',color='#ff0000',linestyle='-')
plt.minorticks_on()
plt.grid(b=True,which='minor',color='#ff0000',linestyle='-')
plt.plot(cha[:,1])

plt.show()

