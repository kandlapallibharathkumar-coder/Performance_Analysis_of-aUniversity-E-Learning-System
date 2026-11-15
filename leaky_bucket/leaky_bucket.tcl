# ==========================================
# LEAKY BUCKET ALGORITHM SIMULATION
# Event-driven model using NS-2 Tcl scheduler
# ==========================================

set ns [new Simulator]

# Create trace file
set tracefile [open "leaky_bucket.tr" w]

# Bucket configuration
set bucketCapacity 4
set leakInterval 0.5

# Simulation variables
set bucketCount 0
set packetID 0
set accepted 0
set dropped 0
set transmitted 0

# Log events
proc logEvent {message} {
    global ns tracefile

    set currentTime [$ns now]
    set output "$currentTime $message"

    puts $output
    puts $tracefile $output
}

# Handle incoming packets
proc incomingPacket {} {
    global bucketCapacity bucketCount
    global packetID accepted dropped

    incr packetID

    if {$bucketCount < $bucketCapacity} {
        incr bucketCount
        incr accepted

        logEvent "Packet $packetID accepted. Queue size: $bucketCount"
    } else {
        incr dropped

        logEvent "Packet $packetID dropped. Bucket is full."
    }
}

# Transmit packets at a constant rate
proc leakPacket {} {
    global ns bucketCount transmitted leakInterval

    if {$bucketCount > 0} {
        incr transmitted
        incr bucketCount -1

        logEvent "Packet transmitted. Queue size: $bucketCount"
    }

    set currentTime [$ns now]

    if {$currentTime < 5.0} {
        set nextTime [expr {$currentTime + $leakInterval}]
        $ns at $nextTime "leakPacket"
    }
}

# Display final results
proc finish {} {
    global ns tracefile
    global accepted dropped transmitted bucketCount

    logEvent "Simulation completed"

    puts "\n================================"
    puts "       LEAKY BUCKET RESULTS"
    puts "================================"

    puts "Packets accepted: $accepted"
    puts "Packets dropped: $dropped"
    puts "Packets transmitted: $transmitted"
    puts "Packets remaining: $bucketCount"

    puts "Total incoming packets: [expr {$accepted + $dropped}]"

    puts "================================"

    close $tracefile
    exit 0
}

# Schedule incoming packets
foreach arrival {
    0.1 0.2 0.3 0.4 0.5
    0.6 1.2 1.3 1.4 2.5
    3.0 3.1 4.0
} {
    $ns at $arrival "incomingPacket"
}

# Start packet leakage
$ns at 0.5 "leakPacket"

# End simulation
$ns at 6.0 "finish"

# Run simulation
$ns run
