import matplotlib.pyplot as plt

loss = [0.05, 0.10, 0.20]
throughput = [4066.57, 3812.34, 3397.76]
plt.plot(loss, throughput, marker='o')
plt.xlabel('Packet Loss Probability')
plt.ylabel('Throughput')
plt.title('TCP Tahoe Throughput Simulation 500 Packets')
plt.savefig('tcp_tahoe_throughput.png')
plt.show()

plt.close()