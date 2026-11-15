
# Three-node E-learning Network

set ns [new Simulator]

# Create trace file
set nf [open three_node.tr w]
$ns trace-all $nf

# Create nodes
set student1 [$ns node]
set router [$ns node]
set server [$ns node]

# Create network links
$ns duplex-link $student1 $router 2Mb 5ms DropTail
$ns duplex-link $router $server 2Mb 5ms DropTail

# Create UDP sender
set udp [new Agent/UDP]
$ns attach-agent $student1 $udp

# Create receiver
set sink [new Agent/Null]
$ns attach-agent $server $sink

# Connect sender and receiver
$ns connect $udp $sink

# Configure CBR traffic
set cbr [new Application/Traffic/CBR]
$cbr set packetSize_ 512
$cbr set interval_ 0.1
$cbr attach-agent $udp

# Schedule traffic
$ns at 0.5 "$cbr start"
$ns at 4.5 "$cbr stop"

# Finish simulation
$ns at 5.0 "finish"

proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    puts "Three-node simulation completed!"
    exit 0
}

$ns run

