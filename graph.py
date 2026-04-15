import matplotlib.pyplot as plt

loss = [0.1,0.05, 0.10]
throughput = [1545269.89, 2360865.72, 1992873.72]
plt.plot(loss, throughput, marker='o')
plt.xlabel('Packet Loss Probability')
plt.ylabel('Throughput')
plt.title('TCP Tahoe Throughput')
plt.savefig('tcp_tahoe_throughput.png')
plt.show()

