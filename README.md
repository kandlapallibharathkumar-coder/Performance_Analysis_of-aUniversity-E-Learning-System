# Network Performance Analysis of a University E-Learning System

## Project Overview
This project uses NS-2 (Network Simulator 2) to analyse network performance in a university e-learning environment. It studies how increasing student traffic affects network congestion, packet loss, throughput and delay.

## Objectives
- Simulate communication between students, routers and servers.
- Analyse network performance under different student loads.
- Compare TCP and UDP traffic.
- Study congestion and sliding-window behaviour.
- Demonstrate Go-Back-N and Leaky Bucket algorithms.
- Generate performance graphs and a project report.

## Technologies
- Ubuntu Linux
- NS-2.35
- Tcl scripting
- Python 3
- Matplotlib
- Git and GitHub

## Project Modules
1. Basic network simulation
2. Three-node network
3. Multiple-student simulation
4. TCP vs UDP comparison
5. Congestion analysis
6. TCP sliding-window analysis
7. Go-Back-N simulation
8. Leaky Bucket simulation

## How to Run
Run commands from the project directory:

```bash
ns simulations/first_network.tcl
ns simulations/three_node.tcl
ns multi_student/multiple_students.tcl
ns tcp_udp/tcp_udp_comparison.tcl
ns congestion/student_load.tcl
ns sliding_window/sliding_window.tcl
ns go_back_n/go_back_n.tcl
ns leaky_bucket/leaky_bucket.tcl
