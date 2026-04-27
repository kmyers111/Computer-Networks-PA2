import random
import time
from tcp_tahoe import TCPTahoe

def simulate(loss_prob, total_packets=500):
    tcp = TCPTahoe()
    delays = []
    sim_time = 0
    start_time = time.time()
    send_time = sim_time
    delay = sim_time - send_time

    for _ in range(total_packets):
        sim_time += 1
        packet_id = tcp.send_packet()

        time.sleep(0.0001)  # Simulate network delay

        send_time = time.time()

        # Simulate whether packet is lost
        if random.random() < loss_prob:
            tcp.on_timeout()
        else:
            tcp.received += 1
            tcp.on_ack(packet_id)
            delay = time.time() - send_time
            delays.append(delay)

    end_time = time.time()

    total_time = end_time - start_time
    throughput = tcp.received / total_time if total_time > 0 else 0
    
    avg_delay = sum(delays) / len(delays) if delays else 0
    jitter = 0
    
    if len(delays) > 1:
        mean_delay = avg_delay
        variance = sum((d - mean_delay) ** 2 for d in delays) / (len(delays) - 1)
        jitter = variance ** 0.5

    return throughput, avg_delay, jitter, tcp.retransmissions


loss_values = [0.05, 0.10, 0.20]

print("Loss\tThroughput\tAvg Delay\tjitter\tRetransmissions")

for loss in loss_values:
    throughput, avg_delay, jitter, retrans = simulate(loss)
    print(f"{loss:.2f}\t{throughput:.2f}\t\t{avg_delay:.6f}\t{jitter:.6f}\t{retrans}")
