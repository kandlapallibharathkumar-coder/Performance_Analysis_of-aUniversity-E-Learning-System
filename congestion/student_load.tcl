# Student Load and Network Congestion Analysis

set ns [new Simulator]

set nf [open student_load.tr w]
$ns trace-all $nf

# Configure number of students
set studentCount 15

# Create router and server
set router [$ns node]
set server [$ns node]

# Shared bottleneck link
$ns duplex-link $router $server 1Mb 10ms DropTail

# Create students and configure traffic
for {set i 0} {$i < $studentCount} {incr i} {

    set student($i) [$ns node]

    $ns duplex-link $student($i) $router 2Mb 5ms DropTail

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

$ns at 10.0 "finish"

proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    puts "Student-load simulation completed!"
    exit 0
}

$ns run
