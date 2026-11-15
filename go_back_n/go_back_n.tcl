
# Go-Back-N ARQ Protocol Simulation
# University E-Learning Network

set ns [new Simulator]

set totalPackets 8
set windowSize 4
set timeout 0.8

set base 0
set nextSeq 0
set expected 0
set timerToken 0

set nf [open go_back_n.tr w]

# Log simulation events
proc log_event {message} {
    global ns nf
    set time [$ns now]
    puts $nf "$time : $message"
    puts "$time : $message"
}

# Start or restart retransmission timer
proc start_timer {} {
    global ns base timerToken timeout totalPackets

    if {$base < $totalPackets} {
        incr timerToken
        set token $timerToken
        $ns at [expr {[$ns now] + $timeout}] "timeout $token"
    }
}

# Send one packet
proc send_packet {seq retrans} {
    global ns expected

    if {$seq == 2 && $retrans == 0} {
        log_event "Packet $seq lost during transmission"
        return
    }

    if {$retrans == 1} {
        log_event "Retransmitting packet $seq"
    } else {
        log_event "Sending packet $seq"
    }

    $ns at [expr {[$ns now] + 0.05}] "receive_packet $seq"
}

# Send packets within the sender window
proc send_window {} {
    global base nextSeq windowSize totalPackets

    while {$nextSeq < $totalPackets &&
           $nextSeq < ($base + $windowSize)} {

        send_packet $nextSeq 0
        incr nextSeq
    }
}

# Receiver processes incoming packets
proc receive_packet {seq} {
    global ns expected

    if {$seq == $expected} {
        log_event "Receiver accepted packet $seq"
        incr expected
    } else {
        log_event "Receiver discarded packet $seq (out of order)"
    }

    set ack [expr {$expected - 1}]
    $ns at [expr {[$ns now] + 0.05}] "receive_ack $ack"
}

# Sender processes cumulative ACK
proc receive_ack {ack} {
    global base nextSeq totalPackets

    if {$ack >= $base} {
        log_event "ACK received for packet $ack"

        set base [expr {$ack + 1}]

        if {$base == $totalPackets} {
            log_event "All packets acknowledged successfully"
            finish
            return
        }

        send_window
        start_timer
    } else {
        log_event "Duplicate ACK received: $ack"
    }
}

# Timeout and Go-Back-N retransmission
proc timeout {token} {
    global base nextSeq timerToken totalPackets

    if {$token != $timerToken || $base >= $totalPackets} {
        return
    }

    log_event "TIMEOUT: Go-Back-N retransmission started"

    for {set i $base} {$i < $nextSeq} {incr i} {
        send_packet $i 1
    }

    start_timer
}

# Finish simulation
proc finish {} {
    global ns nf
    log_event "Go-Back-N simulation completed"
    $ns flush-trace
    close $nf
    exit 0
}

# Start transmission
$ns at 0.1 {
    log_event "Go-Back-N transmission started"
    send_window
    start_timer
}

$ns run
