import matplotlib.pyplot as plt

loss = [0.05, 0.10, 0.20]
jitter = [0.000003, 0.000002, 0.000009]
plt.plot(loss, jitter, marker='o')
plt.xlabel('Packet Loss Probability')
plt.ylabel('Jitter (seconds)')
plt.title('TCP Tahoe jitter Simulation 500 Packets')
plt.savefig('tcp_tahoe_jitter.png')
plt.show()

plt.close()


