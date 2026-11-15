
import matplotlib.pyplot as plt

# Simulation results
simulations = ["Two-Node", "Three-Node", "Five-Student"]
pdr = [100, 100, 99.65]

# Create PDR graph
plt.figure(figsize=(8, 5))
plt.bar(simulations, pdr)

plt.title("Packet Delivery Ratio Comparison")
plt.xlabel("Network Simulation")
plt.ylabel("PDR (%)")
plt.ylim(95, 101)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("pdr_comparison.png", dpi=300)
plt.show()
# Packet Loss Ratio
plr = [0, 0, 0.35]

plt.figure(figsize=(8, 5))
plt.bar(simulations, plr)

plt.title("Packet Loss Ratio Comparison")
plt.xlabel("Network Simulation")
plt.ylabel("PLR (%)")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("plr_comparison.png", dpi=300)
plt.show()
# Throughput Comparison
throughput = [40.96, 40.96, 1022.63]

plt.figure(figsize=(8, 5))
plt.bar(simulations, throughput)

plt.title("Throughput Comparison")
plt.xlabel("Network Simulation")
plt.ylabel("Throughput (Kbps)")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("throughput_comparison.png", dpi=300)
plt.show()
# Average End-to-End Delay Comparison
delay = [14.096, 14.096, 134.446]

plt.figure(figsize=(8, 5))
plt.bar(simulations, delay)

plt.title("Average End-to-End Delay Comparison")
plt.xlabel("Network Simulation")
plt.ylabel("Average Delay (ms)")
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("delay_comparison.png", dpi=300)
plt.show()
