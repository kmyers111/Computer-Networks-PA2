import matplotlib.pyplot as plt

loss = [0.1,0.05, 0.10]
retrans = [1, 4, 8]
plt.plot(loss, retrans, marker='o')
plt.xlabel('Packet Loss Probability')
plt.ylabel('Retransmissions')
plt.title('TCP Tahoe Retransmissions')
plt.savefig('tcp_tahoe_retransmissions.png')
plt.show()
