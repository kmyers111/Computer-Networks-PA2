"""

Implements TCP Tahoe congestion control behavior.
based on the class example  

Features:
- Initialization of congestion control variables
- Slow start
- Congestion avoidance
- Fast retransmit after 3 duplicate ACKs
- Timeout recovery
"""

class TCPTahoe:
    def __init__(self):
        # Initial congestion window
        self.cwnd = 1.0

        # Slow start threshold
        self.ssthresh = 32.0

        # Maximum allowed congestion window
        self.max_cwnd = 50.0

        # Oldest unacknowledged packet
        self.una = 0

        # Next packet number to send
        self.next_seq = 1

        # Duplicate ACK counter
        self.dup_ack = 0

        # Last ACK seen
        self.last_ack = -1

        # Metrics
        self.sent = 0
        self.received = 0
        self.retransmissions = 0

    def on_ack(self, ack_num):
        """
        Process an incoming ACK.
        """

        # If this ACK is older than una, ignore it
        if ack_num < self.una:
            return

        # If this ACK is the same as the last one, count as duplicate ACK
        if ack_num == self.last_ack:
            self.dup_ack += 1

            # Fast retransmit on 3 duplicate ACKs
            if self.dup_ack == 3:
                self.fast_retransmit()
            return

        # New ACK received, reset duplicate ACK counter
        self.dup_ack = 0
        self.last_ack = ack_num

        # Slow start: increase by 1 for each ACK
        if self.cwnd < self.ssthresh:
            self.cwnd = self.cwnd + 1

        # Congestion avoidance: increase by 1/cwnd
        elif self.cwnd < self.max_cwnd:
            self.cwnd = self.cwnd + (1 / self.cwnd)

        # Update una to next expected ACK
        self.una = ack_num + 1

    def fast_retransmit(self):
        """
        Tahoe fast retransmit after 3 duplicate ACKs.
        """
        self.ssthresh = max(self.cwnd / 2, 2)
        self.cwnd = 1
        self.retransmissions += 1
        self.dup_ack = 0

    def on_timeout(self):
        """
        Tahoe timeout and recovery behavior.
        """
        self.ssthresh = max(self.cwnd / 2, 2)
        self.cwnd = 1
        self.retransmissions += 1
        self.dup_ack = 0

    def send_packet(self):
        """
        Simulate sending one packet.
        """
        packet_id = self.next_seq
        self.next_seq += 1
        self.sent += 1
        return packet_id
