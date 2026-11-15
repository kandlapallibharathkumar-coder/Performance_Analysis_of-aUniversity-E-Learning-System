# TCP vs UDP Performance Comparison
# University E-Learning Network

set ns [new Simulator]

# Create trace file
set nf [open tcp_udp.tr w]
$ns trace-all $nf

# Create network nodes
set tcpStudent [$ns node]
set udpStudent [$ns node]
set router [$ns node]
set server [$ns node]

# Configure network links
$ns duplex-link $tcpStudent $router 2Mb 5ms DropTail
$ns duplex-link $udpStudent $router 2Mb 5ms DropTail
$ns duplex-link $router $server 1Mb 10ms DropTail

# Configure TCP agent
set tcp [new Agent/TCP/Newreno]
$tcp set packetSize_ 512
$ns attach-agent $tcpStudent $tcp

set tcpSink [new Agent/TCPSink]
$ns attach-agent $server $tcpSink

$ns connect $tcp $tcpSink

# Configure FTP application over TCP
set ftp [new Application/FTP]
$ftp attach-agent $tcp

# Configure UDP agent
set udp [new Agent/UDP]
$ns attach-agent $udpStudent $udp

set udpSink [new Agent/Null]
$ns attach-agent $server $udpSink

$ns connect $udp $udpSink

# Configure CBR traffic over UDP
set cbr [new Application/Traffic/CBR]
$cbr set packetSize_ 512
$cbr set interval_ 0.02
$cbr attach-agent $udp

# Schedule traffic
$ns at 0.5 "$ftp start"
$ns at 0.5 "$cbr start"

$ns at 9.5 "$ftp stop"
$ns at 9.5 "$cbr stop"

# Finish simulation
$ns at 10.0 "finish"

proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    puts "TCP vs UDP simulation completed!"
    exit 0
}

$ns run
