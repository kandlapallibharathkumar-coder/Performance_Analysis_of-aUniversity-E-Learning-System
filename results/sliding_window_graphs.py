import matplotlib.pyplot as plt

# Simulation results
window_sizes = [4, 8, 16]
throughput = [474.02, 944.57, 995.11]
delay = [21.634, 21.661, 54.829]

# Graph 1: Throughput
plt.figure(figsize=(8, 5))
plt.plot(window_sizes, throughput, marker='o')
plt.title("TCP Sliding Window: Throughput Comparison")
plt.xlabel("TCP Window Size (Packets)")
plt.ylabel("Throughput (Kbps)")
plt.xticks(window_sizes)
plt.grid(True)
plt.tight_layout()
plt.savefig("sliding_window_throughput.png", dpi=300)
plt.close()

# Graph 2: Average End-to-End Delay
plt.figure(figsize=(8, 5))
plt.plot(window_sizes, delay, marker='o')
plt.title("TCP Sliding Window: Delay Comparison")
plt.xlabel("TCP Window Size (Packets)")
plt.ylabel("Average End-to-End Delay (ms)")
plt.xticks(window_sizes)
plt.grid(True)
plt.tight_layout()
plt.savefig("sliding_window_delay.png", dpi=300)
plt.close()

print("Sliding Window graphs generated successfully.")
print("Created: sliding_window_throughput.png")
print("Created: sliding_window_delay.png")
