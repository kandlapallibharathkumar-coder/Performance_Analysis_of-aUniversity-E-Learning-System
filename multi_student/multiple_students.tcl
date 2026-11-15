
# Multiple Students E-Learning Network

set ns [new Simulator]

# Create trace file
set nf [open multiple_students.tr w]
$ns trace-all $nf

# Create router and server
set router [$ns node]
set server [$ns node]

# Create five student nodes
for {set i 0} {$i < 5} {incr i} {
    set student($i) [$ns node]
}

# Connect students to router
for {set i 0} {$i < 5} {incr i} {
    $ns duplex-link $student($i) $router 2Mb 5ms DropTail
}

# Router to server link (shared bottleneck)
$ns duplex-link $router $server 1Mb 10ms DropTail

# Configure traffic for each student
for {set i 0} {$i < 5} {incr i} {

    set udp($i) [new Agent/UDP]
    $ns attach-agent $student($i) $udp($i)

    set sink($i) [new Agent/Null]
    $ns attach-agent $server $sink($i)

    $ns connect $udp($i) $sink($i)

    set cbr($i) [new Application/Traffic/CBR]
    $cbr($i) set packetSize_ 512
    $cbr($i) set interval_ 0.02
    $cbr($i) attach-agent $udp($i)

    $ns at 0.5 "$cbr($i) start"
    $ns at 9.5 "$cbr($i) stop"
}

# Finish simulation
$ns at 10.0 "finish"

proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    puts "Multiple-student simulation completed!"
    exit 0
}

$ns run
