# E-Learning Network Simulation

set ns [new Simulator]

# Create trace file
set nf [open out.tr w]
$ns trace-all $nf

# Create network nodes
set student [$ns node]
set server [$ns node]

# Connect nodes
$ns duplex-link $student $server 1Mb 10ms DropTail

# Create UDP agent
set udp [new Agent/UDP]
$ns attach-agent $student $udp

# Create receiver
set sink [new Agent/Null]
$ns attach-agent $server $sink

# Connect sender and receiver
$ns connect $udp $sink

# Create CBR traffic
set cbr [new Application/Traffic/CBR]
$cbr set packetSize_ 512
$cbr set interval_ 0.1
$cbr attach-agent $udp

# Start and stop traffic
$ns at 0.5 "$cbr start"
$ns at 4.5 "$cbr stop"

# Finish simulation
$ns at 5.0 "finish"

proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    puts "Network simulation completed!"
    exit 0
}

$ns run
