# NETWORK PERFORMANCE ANALYSIS OF A UNIVERSITY E-LEARNING SYSTEM

## ABSTRACT

The rapid growth of online education has increased the demand for reliable and efficient network communication. University e-learning systems provide services such as online classes, video lectures, learning management systems, student portals and online examinations. A large number of students accessing these services simultaneously can generate heavy network traffic, resulting in congestion, packet loss, increased delay and reduced network performance.

This project focuses on analysing the network performance of a university e-learning environment using the Network Simulator 2 (NS-2). Different network scenarios are designed to study communication between students, routers and servers under varying traffic conditions.

The project evaluates important network performance metrics, including Packet Delivery Ratio (PDR), Packet Loss Ratio (PLR), throughput and average end-to-end delay. Experiments include basic network topologies, multiple student traffic generation, TCP and UDP comparison, congestion analysis and TCP sliding-window behaviour.

In addition, event-driven Tcl models are developed to demonstrate the Go-Back-N Automatic Repeat reQuest (ARQ) protocol and the Leaky Bucket traffic-shaping algorithm. These models illustrate reliable packet transmission, retransmission after packet loss and traffic regulation.

The simulation results are analysed using AWK and Python with Matplotlib to generate graphical comparisons. The experiments demonstrate how increasing network load affects packet delivery and delay, how TCP window size influences throughput, and how traffic-control mechanisms manage packet transmission.

The project provides an experimental understanding of network performance and communication mechanisms relevant to university e-learning environments.

**Keywords:** NS-2, E-Learning, Network Performance, TCP, UDP, Congestion, Sliding Window, Go-Back-N ARQ, Leaky Bucket, Throughput.
# 1. INTRODUCTION

## 1.1 Background

Online education has become an important part of modern university education. Universities use e-learning platforms to provide online lectures, video content, digital learning materials, online examinations and student information services.

These applications depend on computer networks to exchange information between students, faculty members and centralized servers. When many students access these services simultaneously, network traffic increases and may affect communication quality.

Network performance depends on several factors, including available bandwidth, network topology, traffic load, packet transmission rate and congestion.

## 1.2 Network Performance Analysis

Network performance analysis is the process of evaluating how efficiently data travels through a communication network.

This project focuses on four important performance metrics:

1. Packet Delivery Ratio (PDR): The percentage of transmitted packets successfully received at the destination.
2. Packet Loss Ratio (PLR): The percentage of transmitted packets that fail to reach the destination.
3. Throughput: The amount of successfully received data per unit of time.
4. Average End-to-End Delay: The average time taken by packets to travel from the source to the destination.

These metrics help identify performance problems under different network conditions.

## 1.3 Role of Network Simulation

Network simulation allows researchers to study communication networks without requiring expensive physical network infrastructure.

Network Simulator 2 (NS-2) is used in this project to create network topologies, configure communication protocols, generate traffic and analyse packet-level events.

Tcl scripts define the simulation scenarios, while AWK is used to extract performance statistics from trace files. Python and Matplotlib are used to generate graphs for visual analysis.

## 1.4 Project Overview

The project models a university e-learning network consisting of student nodes, routers and a server.

Different experiments are conducted by varying the number of students, network traffic and TCP window size. TCP and UDP communication are also compared.

Additional event-driven Tcl models demonstrate Go-Back-N ARQ and the Leaky Bucket algorithm to study reliable transmission and traffic shaping.

The results provide insights into how network traffic and communication mechanisms influence the performance of an e-learning environment.
# 2. PROBLEM STATEMENT

University e-learning systems depend on computer networks to deliver online classes, video lectures, digital learning resources and examination services.

When a large number of students access these services simultaneously, the network may experience increased traffic, congestion, packet loss and communication delays. These issues can affect the reliability and quality of online learning services.

Without proper performance analysis, it becomes difficult to understand how network load and communication protocols influence the overall network behaviour.

Therefore, this project aims to simulate a university e-learning network using NS-2 and analyse its performance under different network conditions. It also demonstrates selected communication and traffic-control algorithms to understand their role in improving network communication.

# 3. OBJECTIVES

The main objectives of this project are:

1. To design and simulate a university e-learning network using NS-2.
2. To study communication between student nodes, routers and servers.
3. To analyse network performance under different numbers of simultaneous students.
4. To calculate Packet Delivery Ratio, Packet Loss Ratio, throughput and average end-to-end delay.
5. To compare TCP and UDP communication under a configured traffic scenario.
6. To study the effect of TCP sender window size on network throughput and delay.
7. To demonstrate reliable packet transmission using the Go-Back-N ARQ algorithm.
8. To demonstrate traffic shaping using the Leaky Bucket algorithm.
9. To extract simulation statistics using AWK.
10. To generate performance graphs using Python and Matplotlib.
11. To identify the effects of increasing network traffic on e-learning network performance.
# 4. EXISTING SYSTEM

Traditional university e-learning systems rely on network infrastructure to provide online classes, digital learning materials, student portals and examination services.

In many environments, network performance is monitored only when users experience problems such as slow access, interrupted video lectures or delayed responses from servers. Without systematic testing, identifying the causes of these problems can be difficult.

Some limitations of the existing approach include:

1. Limited analysis of network behaviour under different traffic loads.
2. Difficulty identifying congestion when many students access services simultaneously.
3. Lack of detailed comparison of packet delivery, packet loss, throughput and delay.
4. Limited understanding of how communication protocols affect network performance.
5. Difficulty testing different network configurations using physical infrastructure.

These limitations create a need for a simulation-based approach to analyse network performance under controlled conditions.
# 5. PROPOSED SYSTEM

The proposed system uses Network Simulator 2 (NS-2) to analyse the performance of a university e-learning network under different network conditions.

The simulated network consists of student nodes, routers and a central server. Different traffic scenarios are created to study communication between students and the server.

The proposed system includes the following activities:

1. Designing basic network topologies using NS-2.
2. Simulating multiple students accessing a common server.
3. Analysing network performance using PDR, PLR, throughput and average end-to-end delay.
4. Comparing TCP and UDP traffic under a configured simulation scenario.
5. Evaluating the effect of TCP sender window size on throughput and delay.
6. Demonstrating Go-Back-N ARQ using an event-driven Tcl model.
7. Demonstrating the Leaky Bucket algorithm using an event-driven Tcl model.
8. Extracting simulation statistics from trace files using AWK.
9. Generating graphical representations using Python and Matplotlib.

The proposed approach provides a controlled environment for studying network behaviour. It helps identify the effects of increasing student traffic and understand the role of communication and traffic-control mechanisms in an e-learning network.
# 6. SYSTEM ARCHITECTURE

The proposed e-learning network architecture consists of student nodes, a central router and an e-learning server.

## 6.1 Network Components

1. Student Nodes: Represent students accessing online lectures, learning materials and other e-learning services.
2. Router: Connects student nodes to the central server and forwards network packets.
3. E-Learning Server: Represents the centralized server that provides online learning services.
4. Communication Links: Connect the network nodes and define bandwidth and propagation delay.

## 6.2 Network Communication

Students generate network traffic using configured communication protocols. The packets travel through the router and reach the e-learning server.

In the multiple-student and congestion experiments, several student nodes share a common router-to-server link. This shared link is used to study the effects of increasing network traffic.

## 6.3 Architecture Overview

The basic communication structure is:

Student Nodes → Router → E-Learning Server

The network topology is modified across experiments to evaluate different traffic conditions, communication protocols and network performance characteristics.
# 7. TOOLS AND TECHNOLOGIES USED

The project uses the following tools and technologies for network simulation, performance analysis and visualization.

## 7.1 Network Simulator 2 (NS-2)

NS-2.35 is used to design network topologies, configure communication protocols, generate network traffic and simulate packet transmission.

## 7.2 Tcl

Tcl scripting is used to define network nodes, communication links, traffic sources, simulation events and protocol behaviour.

## 7.3 AWK

GNU AWK is used to process NS-2 trace files and calculate network performance statistics such as packet delivery ratio, packet loss ratio, throughput and average end-to-end delay.

## 7.4 Python

Python is used to process experimental results and generate graphical representations of network performance.

## 7.5 Matplotlib

Matplotlib is a Python visualization library used to create graphs for comparing network performance across different simulation scenarios.

## 7.6 Ubuntu Linux

Ubuntu Linux is used as the operating environment for executing NS-2 simulations, processing trace files and running analysis scripts.

## 7.7 Oracle VirtualBox

Oracle VirtualBox provides the virtual machine environment in which Ubuntu Linux and the required project tools are installed.
# 8. METHODOLOGY

The project follows a simulation-based methodology to analyse the performance of a university e-learning network.

## 8.1 Network Design

A network topology consisting of student nodes, routers and an e-learning server is designed using NS-2. Different configurations are created to represent basic communication and multiple-student environments.

## 8.2 Traffic Generation

UDP and TCP traffic are generated using appropriate traffic applications. Constant Bit Rate (CBR) traffic is used for UDP experiments, while FTP traffic is used for TCP experiments.

## 8.3 Simulation Execution

Tcl scripts define the network topology, link bandwidth, propagation delay, traffic configuration and simulation duration. NS-2 executes these scripts and generates trace files containing packet-level events.

## 8.4 Performance Measurement

AWK scripts process the generated trace files to calculate the following metrics:

1. Packet Delivery Ratio (PDR).
2. Packet Loss Ratio (PLR).
3. Throughput.
4. Average End-to-End Delay.

## 8.5 Algorithm Demonstration

Separate event-driven Tcl models using the NS-2 event scheduler demonstrate Go-Back-N ARQ and the Leaky Bucket algorithm.

The TCP Sliding Window experiment evaluates the effect of different TCP NewReno sender window sizes.

## 8.6 Result Visualization

Python and Matplotlib are used to generate graphs from the experimental results. These graphs help compare network performance under different simulation conditions.

## 8.7 Result Analysis

The measured values and generated graphs are examined to understand how student traffic, congestion, communication protocols and TCP window sizes influence network performance.
# 9. IMPLEMENTATION

The project is implemented using NS-2.35, Tcl scripting, AWK and Python. Multiple simulation scenarios and algorithm demonstrations are developed to evaluate network behaviour.

## 9.1 Basic Network Simulation

A basic network is created to study communication between a student node and an e-learning server. UDP and CBR traffic are configured to generate packets. A three-node topology with a router is also simulated.

## 9.2 Multiple Student Simulation

Five student nodes are connected to a common router, which forwards packets to the e-learning server. Each student generates UDP traffic. This experiment studies communication when multiple students access the server simultaneously.

## 9.3 TCP and UDP Comparison

TCP NewReno with an FTP application and UDP with a CBR application are configured in the same network scenario. Their packet transmission, throughput and average delay are measured. The results represent the configured traffic applications and are not a universal comparison of TCP and UDP.

## 9.4 Network Congestion Analysis

The number of student nodes is varied across four scenarios: 2, 5, 10 and 15 students. All students share a common 1 Mbps router-to-server link. The experiment examines how increasing traffic affects packet delivery, packet loss, throughput and delay.

## 9.5 TCP Sliding Window Analysis

TCP NewReno is configured with different sender window sizes: 4, 8 and 16. The resulting throughput and average delay are measured to study the effect of the configured TCP window size.

## 9.6 Go-Back-N ARQ Demonstration

An event-driven Tcl model is developed using the NS-2 event scheduler. It demonstrates a sliding transmission window, cumulative acknowledgements, packet loss, timeout and retransmission of outstanding packets.

## 9.7 Leaky Bucket Demonstration

An event-driven Tcl model demonstrates traffic regulation using a bucket with a fixed capacity and a configured packet leakage interval. Incoming packets are accepted or dropped depending on the available bucket capacity.

The Go-Back-N and Leaky Bucket modules are algorithm demonstrations using the NS-2 event scheduler, rather than complete packet-level network implementations.

# 10. RESULTS AND PERFORMANCE ANALYSIS

The simulation results are analysed using packet trace files generated by NS-2. AWK scripts are used to calculate network performance metrics, while Python and Matplotlib are used to generate graphical comparisons.

## 10.1 Basic Network Performance

The basic two-node and three-node simulations completed successfully without packet loss.

| Performance Metric | Two-Node | Three-Node |
|---|---:|---:|
| Packets Received | 40 | 40 |
| Packets Dropped | 0 | 0 |
| PDR (%) | 100 | 100 |
| PLR (%) | 0 | 0 |
| Throughput (Kbps) | 40.96 | 40.96 |
| Average Delay (ms) | 14.096 | 14.096 |

**Observation:** Both topologies delivered all generated packets. The additional router in the three-node topology did not change the measured results in this configuration.

## 10.2 Multiple Student Network Results

Five student nodes communicate with a common e-learning server through a shared router.

| Performance Metric | Result |
|---|---:|
| Packets Sent | 2255 |
| Packets Received | 2247 |
| Packets Dropped | 8 |
| PDR (%) | 99.65 |
| PLR (%) | 0.35 |
| Throughput (Kbps) | 1022.63 |
| Average Delay (ms) | 134.446 |

**Observation:** A small number of packets were dropped, and average delay increased compared with the basic simulations. This indicates the effect of shared network traffic.

## 10.3 TCP and UDP Comparison

TCP NewReno with FTP traffic and UDP with CBR traffic were evaluated in the same network scenario.

| Performance Metric | TCP | UDP |
|---|---:|---:|
| Packets Sent | 1626 | 451 |
| Packets Received | 1626 | 451 |
| Packets Dropped | 0 | 0 |
| PDR (%) | 100 | 100 |
| PLR (%) | 0 | 0 |
| Data Received (Bytes) | 897040 | 230912 |
| Throughput (Kbps) | 797.37 | 205.26 |
| Average Delay (ms) | 94.235 | 93.520 |

**Observation:** TCP transmitted more data in this experiment because the FTP application continuously generated data, whereas UDP used a configured CBR traffic rate. These results describe the selected applications and configuration; they do not establish that one protocol is universally faster than the other.

## 10.4 Network Congestion Analysis

The number of student nodes was varied to examine the effect of increasing traffic on the shared 1 Mbps router-to-server link.

| Students | Packets Sent | Received | Dropped | PDR (%) | PLR (%) | Throughput (Kbps) | Delay (ms) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 902 | 902 | 0 | 100 | 0 | 410.51 | 23.192 |
| 5 | 2255 | 2247 | 8 | 99.65 | 0.35 | 1022.63 | 134.446 |
| 10 | 4510 | 2247 | 2263 | 49.82 | 50.18 | 1022.63 | 208.304 |
| 15 | 6765 | 2247 | 4518 | 33.22 | 66.78 | 1022.63 | 209.158 |

**Observation:**

1. Increasing the number of students increased the traffic offered to the network.
2. Packet loss increased significantly in the 10-student and 15-student scenarios.
3. Packet Delivery Ratio decreased as the network became more congested.
4. Average delay increased with higher network load.
5. Throughput reached a similar measured level in the 5-, 10- and 15-student scenarios, indicating that the shared link had reached its effective capacity under these traffic conditions.

**Measurement note:** Throughput values are calculated from received application payload over the configured 9-second traffic interval. The measured value of 1022.63 Kbps is an application-level estimate and should not be interpreted as the physical link exceeding its nominal 1 Mbps capacity.

## 10.5 TCP Sliding Window Analysis

TCP NewReno was evaluated using sender window sizes of 4, 8 and 16.

| Window Size | Packets Sent | Packets Received | Throughput (Kbps) | Average Delay (ms) |
|---:|---:|---:|---:|---:|
| 4 | 967 | 967 | 474.02 | 21.634 |
| 8 | 1926 | 1926 | 944.57 | 21.661 |
| 16 | 2029 | 2029 | 995.11 | 54.829 |

**Observation:**

1. All three configurations achieved 100% packet delivery in the recorded experiment.
2. Throughput increased as the TCP sender window size increased.
3. The window size of 16 achieved the highest measured throughput.
4. Average delay increased for the window size of 16.

These results demonstrate the effect of TCP NewReno's configured sender window size under the selected network conditions.

## 10.6 Go-Back-N ARQ Results

The event-driven Go-Back-N model was configured with eight packets and a transmission window size of four. One packet was deliberately lost during its initial transmission.

| Measurement | Result |
|---|---:|
| Initial Transmission Attempts | 8 |
| Successful Initial Transmissions | 7 |
| Retransmitted Packets | 4 |
| Deliberately Lost Packets | 1 |
| Accepted Packets | 8 |
| Out-of-Order Packets Discarded | 3 |
| ACKs Received | 8 |
| Duplicate ACKs | 3 |
| Timeouts | 1 |
| Total Packets Delivered | 8 |

**Observation:** The model demonstrates cumulative acknowledgements and retransmission of outstanding packets after a timeout. All eight packets were eventually delivered.

## 10.7 Leaky Bucket Results

The event-driven Leaky Bucket model was executed with a bucket capacity of four packets and a configured leakage interval of 0.5 seconds.

| Measurement | Result |
|---|---:|
| Incoming Packets | 13 |
| Accepted Packets | 10 |
| Dropped Packets | 3 |
| Transmitted Packets | 10 |
| Packets Remaining | 0 |

**Observation:** The model demonstrates how a fixed-capacity bucket regulates incoming traffic. Packets arriving when the bucket is full are dropped, while accepted packets are transmitted according to the configured leakage schedule.

## 10.8 Overall Result Analysis

The experiments demonstrate the following findings:

1. Basic network topologies delivered all generated packets under light traffic.
2. Multiple student traffic increased network delay and caused packet loss.
3. TCP and UDP produced different measured results because their configured traffic applications generated data differently.
4. Increasing student traffic beyond the shared link's capacity increased packet loss and reduced packet delivery ratio.
5. Increasing the TCP sender window improved measured throughput in the selected experiment.
6. The Go-Back-N model demonstrated recovery from packet loss through retransmission.
7. The Leaky Bucket model demonstrated traffic regulation using a fixed-capacity buffer.

The generated performance graphs provide a visual comparison of the simulation results and support the observations made in this analysis.
# 11. GRAPHICAL ANALYSIS

Python and Matplotlib are used to visualize the network performance results. Graphs make it easier to compare different simulation scenarios and understand the effects of network traffic.

## 11.1 Basic Network Performance Graphs

The basic performance graphs compare the two-node, three-node and five-student network scenarios.

The graphs represent:

1. Packet Delivery Ratio comparison.
2. Packet Loss Ratio comparison.
3. Throughput comparison.
4. Average End-to-End Delay comparison.

## 11.2 Congestion Analysis Graphs

Four graphs are generated to analyse the effect of increasing the number of students.

1. Congestion PDR Graph: Shows the decrease in packet delivery ratio as the number of students increases.
2. Congestion PLR Graph: Shows the increase in packet loss ratio under higher network load.
3. Congestion Throughput Graph: Shows the measured throughput across different student-load scenarios.
4. Congestion Delay Graph: Shows the variation in average packet delay as network traffic increases.

## 11.3 TCP Sliding Window Graphs

Two graphs are generated to compare TCP NewReno sender window sizes of 4, 8 and 16.

1. Sliding Window Throughput Graph.
2. Sliding Window Average Delay Graph.

## 11.4 Graphical Analysis Summary

The graphs help identify the relationship between network load, packet delivery, packet loss, throughput and delay.

The congestion graphs show that increasing the number of students affects packet delivery and delay. The TCP sliding-window graphs show that changing the sender window size influences throughput and average delay under the selected simulation configuration.
# 12. CONCLUSION

This project successfully demonstrates the performance analysis of a university e-learning network using Network Simulator 2 (NS-2.35).

Different network scenarios were designed to study communication between students, routers and a centralized e-learning server. The experiments evaluated important network performance metrics, including Packet Delivery Ratio, Packet Loss Ratio, throughput and average end-to-end delay.

The multiple-student and congestion experiments demonstrated how increasing network traffic affects packet delivery and communication delay. The TCP and UDP experiment provided a comparison of two communication protocols under the selected traffic configurations. The TCP Sliding Window experiment showed how changing the sender window size influences throughput and delay.

In addition, event-driven Tcl models demonstrated the working principles of Go-Back-N ARQ and the Leaky Bucket algorithm. These models provided an understanding of packet retransmission and traffic regulation.

AWK was used to extract performance statistics from simulation trace files, while Python and Matplotlib were used to generate graphical comparisons.

Overall, the project provided practical experience in network simulation, traffic analysis, communication protocols and performance evaluation. It also demonstrated the importance of analysing network behaviour to understand the reliability and efficiency of university e-learning services.
# 13. FUTURE ENHANCEMENTS

The current project provides a simulation-based analysis of a university e-learning network. Several improvements can be considered in future versions.

1. **Real-Time Network Monitoring:** Integrate monitoring tools to observe network traffic and performance in real time.
2. **Advanced Network Topologies:** Extend the simulation with additional routers, servers and larger network configurations.
3. **Video Streaming Analysis:** Study the effect of network congestion on online lectures and video streaming applications.
4. **Quality of Service (QoS):** Implement priority-based traffic management to improve the delivery of important e-learning services.
5. **Advanced Congestion Control:** Evaluate additional TCP congestion-control mechanisms under different traffic conditions.
6. **Automated Performance Dashboard:** Develop a web-based dashboard to display simulation results and performance graphs.
7. **Larger Student Scenarios:** Evaluate network behaviour with a greater number of students and different bandwidth configurations.
8. **Advanced Simulation Models:** Extend the event-driven algorithm demonstrations into more detailed packet-level network simulations.
# 14. REFERENCES

The following documentation and technical resources were referred to during the development of this project.

1. The Network Simulator 2 (NS-2) Project. Official documentation and user information.  
   https://www.isi.edu/nsnam/ns/

2. Tcl Developer Xchange. Tcl scripting language documentation.  
   https://www.tcl.tk/

3. GNU Project. GNU Awk User's Guide.  
   https://www.gnu.org/software/gawk/manual/

4. Matplotlib Development Team. Matplotlib Official Documentation.  
   https://matplotlib.org/stable/

5. University of Southern California, Information Sciences Institute. Network Simulator 2 (NS-2) documentation and resources.

6. Computer Networks concepts: TCP, UDP, congestion control, sliding window protocols, Go-Back-N ARQ and traffic shaping.

7. Python Software Foundation. Python Official Documentation.  
   https://docs.python.org/3/
