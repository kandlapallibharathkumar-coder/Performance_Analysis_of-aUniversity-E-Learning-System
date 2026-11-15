import matplotlib.pyplot as plt

students = [2, 5, 10, 15]

pdr = [100, 99.65, 49.82, 33.22]
plr = [0, 0.35, 50.18, 66.78]
throughput = [410.51, 1022.63, 1022.63, 1022.63]
delay = [23.192, 134.446, 208.304, 209.158]

# Packet Delivery Ratio
plt.figure(figsize=(8, 5))
plt.plot(students, pdr, marker='o')
plt.title("Packet Delivery Ratio vs Number of Students")
plt.xlabel("Number of Students")
plt.ylabel("PDR (%)")
plt.grid(True)
plt.tight_layout()
plt.savefig("congestion_pdr.png", dpi=300)
plt.show()

# Packet Loss Ratio
plt.figure(figsize=(8, 5))
plt.plot(students, plr, marker='o')
plt.title("Packet Loss Ratio vs Number of Students")
plt.xlabel("Number of Students")
plt.ylabel("PLR (%)")
plt.grid(True)
plt.tight_layout()
plt.savefig("congestion_plr.png", dpi=300)
plt.show()

# Throughput
plt.figure(figsize=(8, 5))
plt.plot(students, throughput, marker='o')
plt.title("Throughput vs Number of Students")
plt.xlabel("Number of Students")
plt.ylabel("Throughput (Kbps)")
plt.grid(True)
plt.tight_layout()
plt.savefig("congestion_throughput.png", dpi=300)
plt.show()

# Average End-to-End Delay
plt.figure(figsize=(8, 5))
plt.plot(students, delay, marker='o')
plt.title("Average End-to-End Delay vs Number of Students")
plt.xlabel("Number of Students")
plt.ylabel("Average Delay (ms)")
plt.grid(True)
plt.tight_layout()
plt.savefig("congestion_delay.png", dpi=300)
plt.show()
