# Sliding Window Protocol - E-Learning Network

set ns [new Simulator]

# Create trace file
set nf [open sliding_window.tr w]
$ns trace-all $nf

# Create network nodes
set student [$ns node]
set router [$ns node]
set server [$ns node]

# Configure network links
$ns duplex-link $student $router 2Mb 5ms DropTail
$ns duplex-link $router $server 1Mb 10ms DropTail

# Configure TCP agent
set tcp [new Agent/TCP/Newreno]
$tcp set packetSize_ 512
$tcp set window_ 16
$ns attach-agent $student $tcp

# Configure TCP receiver
set sink [new Agent/TCPSink]
$ns attach-agent $server $sink

# Connect sender and receiver
$ns connect $tcp $sink

# Configure FTP application
set ftp [new Application/FTP]
$ftp attach-agent $tcp

# Schedule transmission
$ns at 0.5 "$ftp start"
$ns at 9.5 "$ftp stop"

# Finish simulation
$ns at 10.0 "finish"

proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    puts "Sliding Window simulation completed!"
    exit 0
}

$ns run

